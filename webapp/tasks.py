from functools import wraps
try:
    from io import BytesIO
except ImportError:  # pragma:  no cover
    from cStringIO import StringIO as BytesIO

from flask import Blueprint, abort, g, request
from werkzeug.exceptions import InternalServerError
from celery import states

from webapp.extensions import celery
# from webapp import celery
from webapp.extensions import url_for

text_types = (str, bytes)
try:
    text_types += (unicode,)
except NameError:
    # no unicode on Python 3
    pass

tasks_blueprint = Blueprint('tasks', __name__)


@celery.task
def run_flask_request(environ):
    from .celery_worker import app
    environ_str = {}
    for k, v in environ.items():
        environ_str[k.encode('utf-8')] = v.encode('utf-8')
    if '_wsgi.input' in environ_str:
        environ_str['wsgi.input'] = BytesIO(environ_str['_wsgi.input'])
    # Create a request context similar to that of the original request
    # so that the task can have access to flask.g, flask.request, etc.
    with app.request_context(environ_str):
        # Record the fact that we are running in the Celery worker now
        g.in_celery = True

        # Run the route function and record the response
        try:
            rv = app.full_dispatch_request()
        except:
            # If we are in debug mode we want to see the exception
            # Else, return a 500 error
            if app.debug:
                raise
            rv = app.make_response(InternalServerError())
        return (rv.get_data(), rv.status_code, rv.headers.__dict__)


def async(f):
    """
    This decorator transforms a sync route to asynchronous by running it
    in a background thread.
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        # If we are already running the request on the celery side, then we
        # just call the wrapped function to allow the request to execute.
        if getattr(g, 'in_celery', False):
            return f(*args, **kwargs)

        # If we are on the Flask side, we need to launch the Celery task,
        # passing the request environment, which will be used to reconstruct
        # the request object. The request body has to be handled as a special
        # case, since WSGI requires it to be provided as a file-like object.
        environ = {k: v for k, v in request.environ.items()
                   if isinstance(v, text_types)}
        if 'wsgi.input' in request.environ:
            data = request.get_data()
            environ['_wsgi.input'] = data
        t = run_flask_request.apply_async(args=(environ,))

        # Return a 202 response, with a link that the client can use to
        # obtain task status that is based on the Celery task id.
        if t.state == states.PENDING or t.state == states.RECEIVED or \
                t.state == states.STARTED:
            return '', 202, {'Location': url_for('tasks.get_status', id=t.id)}

        # If the task already finished, return its return value as response.
        # This would be the case when CELERY_ALWAYS_EAGER is set to True.
        return t.info
    return wrapped


@tasks_blueprint.route('/status/<id>', methods=['GET'])
def get_status(id):
    """
    Return status about an asynchronous task. If this request returns a 202
    status code, it means that task hasn't finished yet. Else, the response
    from the task is returned.
    """
    task = run_flask_request.AsyncResult(id)
    if task.state == states.PENDING:
        abort(404)
    if task.state == states.RECEIVED or task.state == states.STARTED:
        return '', 202, {'Location': url_for('tasks.get_status', id=id)}
    print task.info
    return tuple(task.info)

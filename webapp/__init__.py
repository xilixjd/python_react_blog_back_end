# -*- coding: utf-8 -*-

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_whooshalchemyplus import index_all
import flask_whooshalchemyplus

from webapp.extensions import rest_api
from webapp.extensions import db
from webapp.extensions import mail
from webapp.extensions import celery
from webapp.extensions import socketio

from webapp.models.user import User
from webapp.models.blog import Blog
from webapp.models.comment import Comment

from webapp.events import *

from restful import BlogApi
from restful import LoginApi
from restful import UserApi
from restful import LogoutApi
from restful import CommentApi
from restful import BlogTitleApi
from restful import BlogTagApi
from restful import RegisterApi
from restful import CheckMessageApi
from restful import MessageApi
from restful import MentionApi
from restful import ZanApi
from restful import GetImgApi
from restful import SearchApi

from celery import Celery

from config import DevConfig

from gevent import monkey
monkey.patch_all()


# flask_login
login_manager = LoginManager()
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

# socketio = SocketIO()

# celery = Celery(__name__, broker=DevConfig.CELERY_BROKER_URL, backend=DevConfig.CELERY_RESULT_BACKEND)

# Import celery task so that it is registered with the Celery workers
# from webapp.tasks import run_flask_request
# from webapp.send_email import send_asyc_email


def create_app(DevConfig):
    app = Flask(__name__)
    # 跨域加允许 cookies
    cors = CORS(app, resources={
        r'/api/*': {'origins': '*', 'supports_credentials': True}
    })
    app.config.from_object(DevConfig)

    mail.init_app(app)
    mail.app = app
    db.init_app(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()
        # from webapp.app_blueprint import create_fake_data
        # create_fake_data()
        # whoosh_index(app, Blog)
        # whoosh_index(app, Comment)
        # whoosh_index(app, User)
        index_all(app)

    flask_whooshalchemyplus.init_app(app)

    login_manager.init_app(app)
    rest_api.add_resource(BlogApi, '/api/blog', '/api/blog/<int:id>')
    rest_api.add_resource(CommentApi, '/api/blog/<int:blog_id>/comment')
    rest_api.add_resource(BlogTitleApi, '/api/blog/all')
    rest_api.add_resource(BlogTagApi, '/api/blog/tag', '/api/blog/tag/<int:tag_id>')
    rest_api.add_resource(LoginApi, '/api/login')
    rest_api.add_resource(UserApi, '/api/user')
    rest_api.add_resource(LogoutApi, '/api/logout')
    rest_api.add_resource(RegisterApi, '/api/register')
    rest_api.add_resource(CheckMessageApi, '/api/checkMessages')
    rest_api.add_resource(MessageApi, '/api/message', '/api/message/<int:message_id>')
    rest_api.add_resource(MentionApi, '/api/usernameMention')
    rest_api.add_resource(ZanApi, '/api/comment/<int:comment_id>/zan')
    rest_api.add_resource(GetImgApi, '/api/imgs')
    rest_api.add_resource(SearchApi, '/api/search')

    rest_api.init_app(app)

    celery.conf.update(app.config)
    # celery.init_app(app)

    from webapp.app_blueprint import app_blueprint
    app.register_blueprint(app_blueprint)

    from webapp.tasks import tasks_blueprint
    app.register_blueprint(tasks_blueprint)

    from webapp.send_email import emails_blueprint
    app.register_blueprint(emails_blueprint, url_prefix='/emails')

    socketio.init_app(app, message_queue=app.config['CELERY_BROKER_URL'])

    return app


if __name__ == '__main__':
    app = create_app('webapp.config.DevConfig')
    # app.app_context().push()
    # app.run(host='0.0.0.0')
    # gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 module:app
    # celery worker -A webapp.celery_worker.celery --loglevel=info
    socketio.run(app)
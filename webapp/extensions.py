# -*- coding: utf-8 -*-

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
# from flask_celery import Celery
from flask_socketio import SocketIO
from flask import url_for as _url_for, current_app, _request_ctx_stack
from config import DevConfig

from celery import Celery

from redis import Redis

celery = Celery(__name__, broker=DevConfig.CELERY_BROKER_URL, backend=DevConfig.CELERY_RESULT_BACKEND)

# SQLAlchemy
db = SQLAlchemy()

# flask_restful
rest_api = Api()

# flask_mail
mail = Mail()
# celery = Celery()
socketio = SocketIO()
redis = Redis()


def url_for(*args, **kwargs):
    """
    url_for replacement that works even when there is no request context.
    """
    if '_external' not in kwargs:
        kwargs['_external'] = False
    reqctx = _request_ctx_stack.top
    if reqctx is None:
        if kwargs['_external']:
            raise RuntimeError('Cannot generate external URLs without a '
                               'request context.')
        with current_app.test_request_context():
            return _url_for(*args, **kwargs)
    return _url_for(*args, **kwargs)


# 跨域装饰器
# from functools import wraps
# from flask import make_response
#
# def allow_cross_domain(fun):
#     @wraps(fun)
#     def wrapper_fun(*args, **kwargs):
#         rst = make_response(fun(*args, **kwargs))
#         rst.headers['Access-Control-Allow-Origin'] = '*'
#         rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
#         allow_headers = "Referer,Accept,Origin,User-Agent"
#         rst.headers['Access-Control-Allow-Headers'] = allow_headers
#         return rst
#     return wrapper_fun
# def cross_domain(param):
#     response = make_response(param)
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
#     return response
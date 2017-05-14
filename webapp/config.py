# -*- coding: utf-8 -*-
from consts import DB_URI


class DevConfig(object):
    SECRET_KEY = 'xilixjd'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = '349729220@qq.com'
    MAIL_PASSWORD = 'drwmtzmtwmvpcbai'
    MAIL_DEFAULT_SENDER = '349729220@qq.com'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    # CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
    # CELERY_TASK_SERIALIZER = ['*']
    # CELERY_RESULT_SERIALIZER = ['pickle', 'json', 'msgpack', 'yaml']

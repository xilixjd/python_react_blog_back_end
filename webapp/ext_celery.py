# -*- coding: utf-8 -*-
# from celery import Celery
#
# from webapp import create_app
# from webapp.config import DevConfig
#
# def make_celery(app=None):
#     app = app or create_app('webapp.config.DevConfig')
#     celery = Celery(__name__, broker=DevConfig.CELERY_BROKER_URL, backend=DevConfig.CELERY_RESULT_BACKEND)
#     celery.conf.update(app.config)
#     TaskBase = celery.Task
#
#     class ContextTask(TaskBase):
#         abstract = True
#
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
#
#     celery.Task = ContextTask
#     return celery
#
# celery = make_celery()
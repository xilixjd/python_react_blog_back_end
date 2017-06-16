# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from flask import render_template
from flask_mail import Message
from flask import url_for
from flask import jsonify

import time

from consts import blog1_content, blog2_content, blog3_content, blog4_content, blog5_content, blog6_content

from webapp.models.blog import Blog
from webapp.models.tag import Tag
from webapp.tasks import async
from webapp.extensions import mail
from webapp.send_email import send_email


app_blueprint = Blueprint(
    'app',
    __name__,
    template_folder='static'
)

def create_fake_data():
    tag1 = Tag('前端')
    tag1.save()
    tag2 = Tag('后端')
    tag2.save()
    tag3 = Tag('JavaScript')
    tag3.save()
    tag4 = Tag('Python')
    tag4.save()
    tag5 = Tag('面试')
    tag5.save()
    tag6 = Tag('SQL')
    tag6.save()
    tag7 = Tag('读书笔记')
    tag7.save()
    blog1 = Blog('xilixjd', 'MySQL必知必会读书笔记', blog1_content)
    blog1.time = time.time()*1000
    blog1.tags.extend([tag2, tag6, tag7])
    blog1.save()
    # time.sleep(3)
    blog2 = Blog('xilixjd', '单页web应用 JavaScript 从前端到后端', blog2_content)
    blog2.time = time.time()*1000
    blog2.tags.extend([Tag.query.filter_by(title='前端').first(), Tag.query.filter_by(title='后端').first(), Tag.query.filter_by(title='JavaScript').first(), tag7])
    blog2.save()
    # time.sleep(3)
    blog3 = Blog('xilixjd', 'JavaScript 语言精粹', blog3_content)
    blog3.time = time.time()*1000
    blog3.tags.extend([tag1, tag3, tag7])
    blog3.save()
    # time.sleep(3)
    blog4 = Blog('xilixjd', 'JavaScript高级程序设计', blog4_content)
    blog4.time = time.time()*1000
    blog4.tags.extend([tag1, tag3, tag7])
    blog4.save()
    # time.sleep(3)
    blog5 = Blog('xilixjd', '超长干货超多的前端面试汇总', blog5_content)
    blog5.time = time.time()*1000
    blog5.tags.extend([Tag.query.filter_by(title='前端').first(), Tag.query.filter_by(title='面试').first(), Tag.query.filter_by(title='JavaScript').first()])
    blog5.save()
    blog6 = Blog('xilixjd', 'clean-code-javascript', blog6_content)
    blog6.time = time.time()*1000
    blog6.tags.extend([Tag.query.filter_by(title='前端').first(), Tag.query.filter_by(title='JavaScript').first()])
    blog6.save()
    # pass


@app_blueprint.route('/')
def hello_world():
    # create_fake_data()
    lists = Blog.query.whoosh_search('必知必会').all()
    print lists
    return "hello"


@app_blueprint.route('/send')
@async
def send():
    if False:
        result = send_email('test email', ['xilixjd@163.com'], '<a href="www.baidu.com">百度</a>')
    # print result.id
    # print send_asyc_email.AsyncResult(result.id).state
    time.sleep(3)
    # print request.environ
    # print send_asyc_email.AsyncResult(result.id).state
    # print request.args
    # msg = Message(subject='subject',
    #               recipients=['xilixjd@163.com'],
    #               html='html', sender='349729220@qq.com')
    # mail.send(msg)
    return "send"
    # return jsonify({}), 202, {'Location': url_for('tasks.get_status', id=1)}


@app_blueprint.route('/check')
def check():
    # task = send_asyc_email([1, 2]).apply_async()
    # result = send_asyc_email([1, 2]).AsyncResult(task.id)
    return "check"
# @app_blueprint.route('/<path:path>', methods=['GET'])
# def any_root_path(path):
#     return render_template('index.html')


def environ_test(request):
    text_types = (str, bytes, unicode)
    environ = {k: v for k, v in request.environ.items()
               if isinstance(v, text_types)}
    if 'wsgi.input' in request.environ:
        data = request.get_data()
        environ['_wsgi.input'] = data
    return environ
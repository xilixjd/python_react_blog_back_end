# -*- coding: utf-8 -*-
from flask_mail import Message
from flask import Blueprint
from flask import jsonify
from flask import abort
from flask import url_for

from celery import states

from webapp.extensions import celery
from webapp.extensions import mail

from webapp.models import User
from webapp.models import Zan
from webapp.models import Comment
from webapp.models import Message as Message_model

from webapp.events import emit_new_message_to_current_user

import time


emails_blueprint = Blueprint('emails', __name__)


celery.config_from_object('webapp.config.DevConfig')
# 建立一个 celery task
@celery.task(bind=True)
def send_asyc_email(self, msg_obj):
    with mail.app.app_context():
        # result = 1
        # for i in range(2, 5000):
        #     result *= i
        msg = Message(subject=msg_obj['subject'],
                      recipients=msg_obj['recipients'],
                      html=msg_obj['html'], sender='349729220@qq.com')
        mail.send(msg)
        self.update_state(state='PROGRESS',
                          meta={
                              'status': msg_obj['recipients']
                          })
        return {'status': msg_obj['recipients']}


# 可以在相应的 api 中调用以建立一个 celery task 发邮件
def send_email(subject, recipients, html):
    msg = Message(subject=subject,
                  recipients=recipients)
    msg.html = html
    msg_obj = {
        'recipients': msg.recipients,
        'subject': msg.subject,
        'html': msg.html
    }
    return send_asyc_email.apply_async(args=[msg_obj])


# 构建一个 email 视图，查询 celery email 发送情况
@emails_blueprint.route('/status/<id>', methods=['GET'])
def get_status(id):
    if not id:
        abort(404)
    task = send_asyc_email.AsyncResult(id)
    if task.state == states.PENDING:
        abort(404)
    if task.state == states.RECEIVED or task.state == states.STARTED:
        return '', 202, {'Location': url_for('emails.get_status', id=id)}
    return jsonify(task.info.get('status', ''))


@celery.task(bind=True)
def check_messages_async(self, userid):
    user = User.query.get(userid)
    messages = user.messages.all()
    for message in messages:
        message.checked = '1'
        message.save()


@celery.task(bind=True)
def write_zan_model_operation(self, model_obj, zaned, zan_count, href):
    user_id = model_obj['user_id']
    comment_id = model_obj['comment_id']
    if zaned == 0:
        zan_check = Zan.query.filter_by(user_id=user_id, comment_id=comment_id).first()
        if not zan_check:
            zan = Zan(user_id, comment_id)
            zan.create_time = time.time() * 1000
            zan.save()
        c = Comment.query.get(comment_id)
        c.zan_count = zan_count
        c.save()
        author = c.author
        u = User.query.filter_by(username=author).first()
        sender = User.query.get(user_id)
        if u:
            # 判断一下，避免重复点赞，导致重复发消息
            m = Message_model.query.filter_by(href=href+'#comment'+str(c.id),
                                              sender=sender.username).first()
            if not m:
                message = Message_model(sender.username, '赞了你的评论')
                message.href = href + '#comment' + str(c.id)
                message.time = time.time() * 1000
                message.users = u
                message.checked = '0'
                message.message_type = '有评论被赞'
                message.save()
            emit_new_message_to_current_user(u, Message_model)
    else:
        zan = Zan.query.filter_by(user_id=user_id, comment_id=comment_id).first()
        if zan:
            zan.delete()
        c = Comment.query.get(comment_id)
        c.zan_count = zan_count
        c.save()
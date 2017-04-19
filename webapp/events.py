# -*- coding: utf-8 -*-

from webapp.extensions import socketio


# @socketio.on('new_message')
# def on_new_message(msg):
#     print msg


def emit_new_message_to_current_user(user, message):
    unchecked_messages = message.user_unchecked_messages(user.id)
    d = {
        "username": user.username,
        "uncheckedMessagesLen": len(unchecked_messages)
    }
    socketio.emit('new_message', d)


# 用 socket 去 emit mentions 不知道是否需要
# def emit_mentions_by_name(name, User):
#     if name:
#         mentions = User.get_username_by_reg(name)
#         if not len(mentions):
#             socketio.emit('mentions_by_name', [])
#         return socketio.emit('mentions_by_name', mentions)
#     else:
#         mentions = User.get_username_limit5()
#         return socketio.emit('mentions_by_name', mentions)
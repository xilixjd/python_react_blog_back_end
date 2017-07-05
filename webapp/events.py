# -*- coding: utf-8 -*-

from webapp.extensions import socketio

from webapp.models.room import Room
from webapp.models.chess import Chess

from flask_login import current_user

from flask_socketio import join_room
from flask_socketio import leave_room

from flask import session

import json

import time


@socketio.on('joined')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room', '')
    if room is None:
        return
    username = session.get('username', 'unknown')
    if current_user.is_active:
        username = current_user.username
    join_room(room)
    new_room = Room.query.filter_by(username=username, room=room).first()
    if new_room is None:
        new_room = Room(username=username, room=room)
        new_room.save()
    userList = get_room_userlist(room)
    socketio.emit('users', userList)
    socketio.emit('messages', {'message': username + ' has entered the room.'}, room=room)


# disconnect 在双方都准备的时候总是连续触发
# @socketio.on('disconnect')
@socketio.on('leave')
def on_disconnect():
    username = session.get('username', 'unknown')
    if current_user.is_active:
        username = current_user.username
    room = session.get('room')
    leave_room(room)
    the_room = Room.query.filter_by(username=username, room=room).first()
    if the_room and the_room.match_password is not None and the_room.ready == 1:
        socketio.emit('messages', {'message': username + ' has been left the game'},
                      room=room)
    if the_room:
        the_room.delete()
    userList = get_room_userlist(room)
    socketio.emit('users', userList)
    socketio.emit('messages', {'message': username + ' has left the room.'}, room=room)


@socketio.on('chat')
def on_chat(message):
    username = session.get('username')
    if current_user.is_active:
        username = current_user.username
    room = session.get('room')
    if room is None:
        return
    d = {
        'sender': username,
        'timestamp': time.time() * 1000,
        'message': message
    }
    socketio.emit('messages', d, room=room)


@socketio.on('match')
def on_match(msg):
    username = session.get('username')
    if current_user.is_active:
        username = current_user.username
    room = session.get('room')
    if room is None:
        return
    the_room = Room.query.filter_by(room=room, username=username).first()
    if the_room is None:
        return
    ready_rooms = Room.query.filter_by(room=room, ready=1).all()
    if len(ready_rooms) == 0:
        match_password = 'Room({})'.format(username)
        the_room.ready = 1
        the_room.match_password = match_password
        the_room.save()
        join_room(match_password)
        d = {
            'match_password': match_password,
            'status': 'waiting',
            'chess': -1, # 黑子
        }
        socketio.emit('messages', {'message': username + ' is ready!'}, room=room)
        socketio.emit('password', d, room=match_password)
    elif len(ready_rooms) == 1:
        match_password = ready_rooms[0].match_password
        another_username = ready_rooms[0].username
        the_room.ready = 1
        the_room.match_password = match_password
        the_room.save()
        join_room(match_password)
        d = {
            'match_password': match_password,
            'status': 'ready',
            'chess': 1, # 白子
        }
        socketio.emit('messages', {'message': username + ' and ' + another_username + "'s game is begin!"}, room=room)
        socketio.emit('password', d, room=match_password)
        chess = Chess.query.filter_by(room=room).first()
        if chess:
            chess.chess_board=json.dumps(init_chess_arr())
            chess.save()
        else:
            chess = Chess(room=room, chess_board=json.dumps(init_chess_arr()))
            chess.save()
        socketio.emit('resetChessBoard', chess.chess_board, room=room)
    else:
        return


@socketio.on('operate')
def on_operate(obj):
    chess_array = obj['chessArr']
    chess_color = obj['chess']
    username = session.get('username')
    if current_user.is_active:
        username = current_user.username
    room = session.get('room')
    the_room = Room.query.filter_by(room=room, username=username).first()
    if the_room is None:
        return
    ready_rooms = Room.query.filter_by(room=room, ready=1).all()
    if len(ready_rooms) == 2 and the_room.ready == 1:
        chess = Chess.query.filter_by(room=room).first()
        if not chess:
            return
        chess.chess_board = json.dumps(chess_array)
        chess.save()
        d = {
            'chessArr': json.dumps(chess_array),
            'chess': chess_color,
        }
        socketio.emit('chessChange', d, room=room)
    else:
        return


@socketio.on('gameover')
def game_over(chess):
    room = session.get('room')
    socketio.emit('gameover', chess, room=room)


def emit_new_message_to_current_user(user, message):
    unchecked_messages = message.user_unchecked_messages(user.id)
    d = {
        "username": user.username,
        "uncheckedMessagesLen": len(unchecked_messages)
    }
    socketio.emit('new_message', d)


def get_room_userlist(room):
    userlist = []
    rooms = Room.query.filter_by(room=room).all()
    for r in rooms:
        userlist.append(r.username)
    return userlist


def init_chess_arr():
    chess_arr = [[0 for i in range(15)] for j in range(15)]
    return chess_arr

# @socketio.on('connect')
# def test_connect():
#     socketio.emit('my response', {'data': 'Connected'})


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
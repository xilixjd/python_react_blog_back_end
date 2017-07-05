# -*- coding: utf-8 -*-

from .blog import Blog
from .comment import Comment
from .tag import Tag
from .user import User
from .message import Message
from .reply import Reply
from .zan import Zan
from .role import Role
from .room import Room
from .chess import Chess





# roles = db.Table(
#     'role_users',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
# )
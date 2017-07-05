# -*- coding: utf-8 -*-

from webapp.extensions import db

from sqlalchemy.dialects.mysql import LONGTEXT

import time


class Chess(db.Model):
    __tablename__ = 'chess'

    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(100), unique=True)
    chess_board = db.Column(LONGTEXT)
    created_at = db.Column(db.Integer, default=time.time())

    def __init__(self, **kwargs):
        self.room = kwargs['room']
        self.chess_board = kwargs['chess_board']

    def __repr__(self):
        return "<Chess '{}'>".format(self.room)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
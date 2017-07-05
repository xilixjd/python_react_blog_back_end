# -*- coding: utf-8 -*-

from webapp.extensions import db


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(100))
    username = db.Column(db.String(100))
    match_password = db.Column(db.String(100))
    ready = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.room = kwargs['room']

    def __repr__(self):
        return "<Room '{}' User '{}'>".format(self.room, self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
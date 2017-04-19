# -*- coding: utf-8 -*-

from webapp.extensions import db


class Reply(db.Model):
    __tablename__ = 'replys'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.BigInteger)
    sender = db.Column(db.String(255))
    receiver = db.Column(db.String(255))
    content = db.Column(db.String(1000))

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def __init__(self, sender, receiver, contetnt):
        self.sender = sender
        self.receiver = receiver
        self.content = contetnt

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def roll_back():
        db.session.rollback()
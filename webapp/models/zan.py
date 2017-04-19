# -*- coding: utf-8 -*-

from webapp.extensions import db


class Zan(db.Model):
    __tablename__ = 'zans'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    create_time = db.Column(db.BigInteger())
    comment_id = db.Column(db.Integer())
    # '0' 为未点赞
    liked = db.Column(db.Integer, default=1)

    def __init__(self, user_id, comment_id):
        self.user_id = user_id
        self.comment_id = comment_id

    def __repr__(self):
        return "<Zan '{}' '{}'>".format(self.id, self.status)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def roll_back():
        db.session.rollback()
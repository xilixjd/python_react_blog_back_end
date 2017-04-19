# -*- coding: utf-8 -*-

from webapp.extensions import db


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.BigInteger)
    # 1 表示已经查看， 0 表示未查看
    checked = db.Column(db.String(10))
    sender = db.Column(db.String(255))
    content = db.Column(db.String(1000))
    href = db.Column(db.String(1000))
    message_type = db.Column(db.String(1000))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def roll_back():
        db.session.rollback()

    # 查询指定用户的 unchecked messages
    @staticmethod
    def user_unchecked_messages(user_id):
        sql = '''
            SELECT messages.id, messages.sender, messages.checked, messages.content, messages.time
            FROM messages
            WHERE messages.user_id={} AND messages.checked='0'
        '''.format(user_id)
        ret = db.engine.execute(sql).fetchall()
        return [dict(r) for r in ret]
# -*- coding: utf-8 -*-

from webapp.extensions import db

from functools import reduce
from operator import or_

from jieba.analyse.analyzer import ChineseAnalyzer

from flask_security import UserMixin


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __searchable__ = ['username']
    __analyzer__ = ChineseAnalyzer()

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    create_time = db.Column(db.String(255))

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    messages = db.relationship('Message', backref='users', lazy='dynamic')

    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.password = kwargs['password']

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    def check_username_password(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return False
        elif user.password != password:
            return False
        else:
            return True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def roll_back():
        db.session.rollback()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def can(self, permissions):
        if self.roles is None:
            return False
        all_perms = reduce(or_, map(lambda x: x.permissions, self.roles))
        return all_perms & permissions == permissions

    @staticmethod
    def get_username_by_reg(reg):
        sql = '''
            select username
            from users
            where username REGEXP '{}' LIMIT 5
        '''.format(reg)
        ret = db.engine.execute(sql).fetchall()
        return [dict(r)['username'] for r in ret]

    @staticmethod
    def get_username_limit5():
        sql = '''
            select username
            from users
            LIMIT 5
        '''
        ret = db.engine.execute(sql).fetchall()
        return [dict(r)['username'] for r in ret]
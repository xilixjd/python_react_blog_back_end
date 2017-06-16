# -*- coding: utf-8 -*-

from flask_security import RoleMixin

from webapp.extensions import db
from webapp.extensions import Permission


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    permissions = db.Column(db.Integer, default=Permission.LOGIN)
    description = db.Column(db.String(255))

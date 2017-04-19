# -*- coding: utf-8 -*-

from webapp.extensions import db


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Tag '{}'>".format(self.title)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def tag_blogs(tag_id):
        sql_str ='''
        SELECT blogs.id AS id, blogs.time AS time, blogs.author AS author, blogs.title AS title, tags.title AS tags
        FROM blogs, blog_tags, tags
        WHERE {} = blog_tags.tag_id AND blogs.id = blog_tags.blog_id AND tags.id = {}
        '''.format(tag_id, tag_id)
        ret = db.engine.execute(sql_str).fetchall()
        return [dict(r) for r in ret]
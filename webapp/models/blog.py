# -*- coding: utf-8 -*-

from webapp.extensions import db

from sqlalchemy.orm import class_mapper

from sqlalchemy.dialects.mysql import LONGTEXT


tags = db.Table(
    'blog_tags',
    db.Column('blog_id', db.Integer, db.ForeignKey('blogs.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.BigInteger)
    author = db.Column(db.String(255))
    title = db.Column(db.String(255), unique=True)
    content = db.Column(LONGTEXT)

    comments = db.relationship('Comment', backref='blogs', lazy='dynamic')
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('blogs', lazy='dynamic'))

    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content

    def __repr__(self):
        return "<Blog '{}'>".format(self.title)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Transforms a model into a dictionary which can be dumped to JSON."""
        # first we get the names of all the columns on your model
        columns = [c.key for c in class_mapper(self.__class__).columns]
        # then we return their values in a dict
        return dict((c, getattr(self, c)) for c in columns)

    # 返回除了 content, comments 之外的值
    @staticmethod
    def query_title():
        sql_str = '''
        SELECT blogs.id, blogs.time, blogs.author, blogs.title, group_concat(tags.title) tag
        FROM blogs LEFT JOIN blog_tags ON blogs.id=blog_tags.blog_id
        left join tags ON tags.id=blog_tags.tag_id
        group by blogs.id;
        '''
        ret = db.engine.execute(sql_str).fetchall()
        return [dict(r) for r in ret]
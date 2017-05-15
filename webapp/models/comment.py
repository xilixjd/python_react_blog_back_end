# -*- coding: utf-8 -*-

from webapp.extensions import db

from sqlalchemy.orm import class_mapper
from sqlalchemy import func

from jieba.analyse.analyzer import ChineseAnalyzer


class Comment(db.Model):
    __tablename__ = 'comments'
    __searchable__ = ['content']
    __analyzer__ = ChineseAnalyzer()

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.BigInteger)
    author = db.Column(db.String(255))
    content = db.Column(db.String(1000))
    # 回复谁
    receiver = db.Column(db.String(255))
    zan_count = db.Column(db.Integer, default=0)
    # 回复的 comment_id
    reply_to_comment_id = db.Column(db.Integer)

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def __init__(self, author, receiver, content):
        self.author = author
        self.content = content
        self.receiver = receiver

    def __repr__(self):
        return "<Comment '{}'>".format(self.content[:15])

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def roll_back():
        db.session.rollback()

    def to_dict(self):
        """Transforms a model into a dictionary which can be dumped to JSON."""
        # first we get the names of all the columns on your model
        columns = [c.key for c in class_mapper(self.__class__).columns]
        # then we return their values in a dict
        return dict((c, getattr(self, c)) for c in columns)

    @staticmethod
    def total():
        return db.session.query(func.count(Comment.id)).all()[0][0]

    def index_of_comment_in_blog(self):
        '''
        查询某 blog 所属的 comment 是第几条数据，以此来得到分页信息
        :param id:
        :return:
        '''
        sql_str = '''
                SELECT COUNT(*) as count FROM comments
                WHERE comments.blog_id={}
                AND comments.id<={} order by comments.id asc;
                '''.format(self.blog_id, self.id)
        ret = db.engine.execute(sql_str).fetchall()
        try:
            return int([dict(r) for r in ret][0]['count'])
        except:
            return 0



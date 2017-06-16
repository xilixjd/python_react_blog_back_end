# -*- coding: utf-8 -*-
from flask_restful import abort, Resource
from flask_restful import marshal_with

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user

from flask import url_for

from parsers import bloglist_get_parser
from parsers import bloglist_post_parser
from parsers import bloglist_put_parser
from parsers import login_post
from parsers import comment_post_parser
from parsers import comment_get_parser
from parsers import register_post
from parsers import message_post
from parsers import mention_post
from parsers import zan_post
from parsers import img_get
from parsers import search_post
from parsers import comment_delete_parser

from fields import blog_fields
from fields import comment_fields
from fields import blog_title_fields
from fields import tag_blog_fields
from fields import message_fields
from fields import user_fields
from fields import comment_page_fields
from fields import search_fields

import time
import datetime
import re

from webapp.models import Blog
from webapp.models import User
from webapp.models import Comment
from webapp.models import Tag
from webapp.models import Message
from webapp.models import Zan
from webapp.models import Reply

from webapp.extensions import redis
from webapp.extensions import query_search_to_string
from webapp.extensions import Permission

from webapp.events import emit_new_message_to_current_user

from webapp.send_email import send_email
from webapp.send_email import check_messages_async
from webapp.send_email import write_zan_model_operation

from webapp.tasks import async

import requests

import jieba


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class BlogApi(Resource):
    @marshal_with(blog_fields)
    def get(self, id=None):
        if id:
            redis_key = 'blog:{}'.format(id)
            blog_redis = redis.hgetall(redis_key)
            if blog_redis == {}:
                blog = Blog.query.get(id)
                if blog is None:
                    abort(404)
                # 这里可以用 celery
                blog_dict = blog.to_dict()
                redis.hmset(redis_key, blog_dict)
                redis.expire(redis_key, 86400 * 5)
                return blog
            else:
                return blog_redis
        else:
            args = bloglist_get_parser.parse_args()
            pageIdx = args['pageIdx'] or 1
            quantity = args['quantity'] or 20
            author = args['author']
            tag_title = args['tag']
            if tag_title:
                tag = Tag.query.filter_by(title=tag_title).first()
                blogs = tag.blogs.paginate(pageIdx, quantity)
                return blogs.items
            if author:
                blogs = Blog.query.filter_by(author=author).paginate(pageIdx, quantity)
                return blogs.items
            else:
                blogs = Blog.query.order_by(Blog.time.desc()).paginate(pageIdx, quantity)
                return blogs.items

    def post(self):
        args = bloglist_post_parser.parse_args()
        title = args['title']
        content = args['content']
        if current_user is None:
            abort(404)
        author = current_user.username
        new_blog = Blog(author, title, content)
        new_blog.time = int(time.time() * 1000)
        new_blog.save()
        return new_blog, 201

    def put(self, id=None):
        if not id:
            abort(404)

        if current_user is None:
            abort(404)

        blog = Blog.query.get(id)
        if not blog:
            abort(404)
        if blog.author != current_user.username:
            abort(404)

        args = bloglist_put_parser.parse_args()
        if args['title']:
            blog.title = args['title']
        if args['content']:
            blog.content = args['content']

        blog.save()
        return blog, 201

    def delete(self, id=None):
        if not id:
            abort(400)

        if current_user is None:
            abort(404)

        blog = Blog.query.get(id)
        if not blog:
            abort(404)

        if blog.author != current_user.username:
            abort(404)

        blog.delete()
        return "delete success", 204


class BlogTitleApi(Resource):
    @marshal_with(blog_title_fields)
    def get(self):
        # args = blog_title_get_parser.parse_args()
        # pageIdx = args['pageIdx'] or 1
        # quantity = args['quantity'] or 20
        return Blog.query_title()


class BlogTagApi(Resource):
    @marshal_with(tag_blog_fields)
    def get(self, tag_id=None):
        if not tag_id:
            return Tag.query.all()
        # return tag.blogs.all()
        return Tag.tag_blogs(tag_id)


class CommentApi(Resource):
    @marshal_with(comment_page_fields)
    def get(self, blog_id=None):
        if not blog_id:
            abort(404)
        blog = Blog.query.get(blog_id)
        if not blog:
            abort(404)
        args = comment_get_parser.parse_args()
        pageIdx = args['pageIdx'] or 1
        quantity = args['quantity'] or 15
        pageIdx = int(pageIdx)
        quantity = int(quantity)
        comments_total = blog.comments
        comments = comments_total.paginate(pageIdx, quantity).items
        comments_obj = {}
        paging_obj = {
            'pageIdx': pageIdx,
            'quantity': quantity,
            'totalCount': len(blog.comments.all())
        }
        comments_list = []
        if current_user.is_active:
            user_id = current_user.id
            for comment in comments:
                allow_delete = comment.author == current_user.username or current_user.can(Permission.ADMINISTER)
                c = comment.to_dict()
                redis_key = 'zan_comment:{}'.format(comment.id)
                c['liked'] = redis.getbit(redis_key, user_id)
                c['zan_count'] = redis.bitcount(redis_key, 0, -1)
                c['allow_delete'] = allow_delete
                comments_list.append(c)
            # 先根据赞的数量由大到小排序， 再根据时间从小到大排序
            comments_list.sort(key=lambda k: (-k['zan_count'], k['time']))
            comments_obj['data'] = comments_list
            comments_obj['paging'] = paging_obj
            return comments_obj
        else:
            for comment in comments:
                c = comment.to_dict()
                redis_key = 'zan_comment:{}'.format(comment.id)
                c['liked'] = 0
                c['zan_count'] = redis.bitcount(redis_key, 0, -1)
                c['allow_delete'] = False
                comments_list.append(c)
            # 先根据赞的数量由大到小排序， 再根据时间从小到大排序
            comments_list.sort(key=lambda k: (-k['zan_count'], k['time']))
            comments_obj['data'] = comments_list
            comments_obj['paging'] = paging_obj
            return comments_obj

    @marshal_with(comment_fields)
    def post(self, blog_id=None):
        if not blog_id:
            abort(404)
        blog = Blog.query.get(blog_id)
        if not blog:
            abort(404)
        args = comment_post_parser.parse_args()
        reply_to = args['replyTo']
        content = args['content']
        author = args['author']
        href = args['href']

        pattern = re.compile('@(.*?)\s')
        if reply_to:
            # 被回复的 comment
            c = Comment.query.filter_by(id=int(reply_to)).first()
            if not c:
                abort(404)
            receiver = c.author
            comment = Comment(author, receiver, content)
            comment.time = time.time() * 1000
            comment.blog_id = blog_id
            comment.save()
            total_comments = len(blog.comments.all())
            u = User.query.filter_by(username=receiver).first()
            if u:
                message = Message(author, content)
                message.href = '/post/{}?pageIdx={}#comment{}'.format(blog_id,
                                                                      str((total_comments + 15 - 1) / 15),
                                                                      str(comment.id))
                message.time = time.time() * 1000
                message.users = u
                message.checked = '0'
                message.message_type = '有人回复你'
                message.save()
                emit_new_message_to_current_user(u, Message)
            # 根据正则表达式来匹配 content 中的用户名，再做出提醒
            if (pattern.search(content)):
                username_array = pattern.findall(content)
                for a in username_array:
                    u = User.query.filter_by(username=a).first()
                    if u:
                        message = Message(author, content)
                        message.href = '/post/{}?pageIdx={}#comment{}'.format(blog_id,
                                                                              str((total_comments + 15 - 1) / 15),
                                                                              str(comment.id))
                        message.time = time.time() * 1000
                        message.users = u
                        message.checked = '0'
                        message.message_type = '有人@你'
                        message.save()
                        emit_new_message_to_current_user(u, Message)
            return comment
        comment = Comment(author, '', content)
        comment.time = time.time() * 1000
        comment.blog_id = blog_id
        comment.save()
        total_comments = len(blog.comments.all())
        if (pattern.search(content)):
            username_array = pattern.findall(content)
            for a in username_array:
                u = User.query.filter_by(username=a).first()
                if u:
                    message = Message(author, content)
                    message.href = '/post/{}?pageIdx={}#comment{}'.format(blog_id,
                                                                          str((total_comments + 15 - 1) / 15),
                                                                          str(comment.id))
                    message.time = time.time() * 1000
                    message.users = u
                    message.checked = '0'
                    message.message_type = '有人@你'
                    message.save()
                    emit_new_message_to_current_user(u, Message)
        return comment

    @marshal_with(comment_fields)
    def delete(self, blog_id=None):
        if not blog_id:
            abort(404)
        args = comment_delete_parser.parse_args()
        comment_id = args['commentId']
        if not comment_id:
            abort(404)
        comment = Comment.query.get(comment_id)
        if comment and current_user.is_active and (comment.author == current_user.username
                                                   or current_user.can(Permission.ADMINISTER)):
            comment.delete()
            return comment
        else:
            abort(404)


class RegisterApi(Resource):
    def post(self):
        args = register_post.parse_args()
        args_username = args['username']
        user = User.query.filter_by(username=args_username).first()
        args_password = args['password']
        args_email = args['email']
        new_user = User(args_username, args_password)
        new_user.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        new_user.email = args_email

        d = {
            "username": new_user.username
        }
        try:
            new_user.save()
            if args_email:
                result = send_email('xilixjd blog', [args_email], '欢迎注册')
                return d, 202, {'Location': url_for('emails.get_status', id=result.id)}
            else:
                return d, 202
        except:
            new_user.roll_back()
            return None, 404


class LoginApi(Resource):
    @marshal_with(user_fields)
    def post(self):
        args = login_post.parse_args()
        args_username = args['username']
        args_password = args['password']
        if not args_username:
            abort(404)
        user = User.query.filter_by(username=args_username).first()
        if not user:
            abort(404)
        login_user(user, True)
        unchecked_messages = Message.user_unchecked_messages(user.id)
        d = {
            "username": user.username,
            "messages": user.messages.all(),
            "uncheckedMessagesLen": len(unchecked_messages)
        }
        return d


class LogoutApi(Resource):
    def get(self):
        if current_user.is_active:
            logout_user()
            return "logout"
        else:
            return "you are not logged in !", 404


class UserApi(Resource):
    @marshal_with(user_fields)
    def get(self):
        if current_user.is_active:
            user_id = current_user.id
            unchecked_messages = Message.user_unchecked_messages(user_id)
            d = {
                "username": current_user.username,
                "messages": current_user.messages.order_by(Message.time.desc()).all(),
                "uncheckedMessagesLen": len(unchecked_messages)
            }
            return d
        else:
            abort(404)


class CheckMessageApi(Resource):
    @marshal_with(message_fields)
    def post(self):
        if current_user.is_active:
            userid = current_user.id
            # 在用户点击 checkMessage 10s 后对每个 message 作 checked 处理
            result = check_messages_async.apply_async(args=[userid], countdown=10)
            return current_user.messages.order_by(Message.time.desc()).all()
        else:
            return None


class MessageApi(Resource):
    @marshal_with(message_fields)
    def get(self, message_id=None):
        if current_user.is_active:
            if message_id:
                message = Message.query.filter_by(id=message_id).first()
                return message
            else:
                messages = current_user.messages.order_by(Message.time.desc()).all()
                return messages
        else:
            return None

    @marshal_with(message_fields)
    def post(self):
        args = message_post.parse_args()
        args_sender = args['sender']
        args_content = args['content']
        args_receiver = args['receiver']
        u = User.query.filter_by(username=args_receiver).first()
        if u:
            message = Message(args_sender, args_content)
            message.checked = 0
            message.time = time.time() * 1000
            message.users = u
            message.save()
            return message
        else:
            return None, 404


class MentionApi(Resource):
    def post(self):
        args = mention_post.parse_args()
        name = args['name']
        if name:
            mentions = User.get_username_by_reg(name)
            if not len(mentions):
                # return User.get_username_limit5()
                return []
            return mentions
        else:
            mentions = User.get_username_limit5()
            return mentions


class ZanApi(Resource):
    # 点赞
    def post(self, comment_id):
        if not comment_id:
            abort(404)
        comment = Comment.query.get(comment_id)
        if not comment:
            abort(404)
        if not current_user.is_active:
            abort(404)
        args = zan_post.parse_args()
        href = args['href']
        user_id = current_user.id
        redis_key = 'zan_comment:{}'.format(comment_id)
        model_obj = {
            'user_id': user_id,
            'comment_id': comment_id
        }
        # 先判断是否已赞, 0 为未点赞， 1 为已点赞
        zaned = redis.getbit(redis_key, user_id)
        if zaned == 0:
            # 根据 comment_id 和 user_id 判断哪个用户对哪条评论点赞
            redis.setbit(redis_key, user_id, 1)
            zan_count = redis.bitcount(redis_key, 0, -1)
            write_zan_model_operation.apply_async(args=[model_obj, zaned, zan_count, href])
            return zan_count
        else:
            # 根据 comment_id 和 user_id 判断哪个用户对哪条评论点赞
            redis.setbit(redis_key, user_id, 0)
            zan_count = redis.bitcount(redis_key, 0, -1)
            write_zan_model_operation.apply_async(args=[model_obj, zaned, zan_count, href])
            return zan_count


class GetImgApi(Resource):
    def get(self):
        args = img_get.parse_args()
        page = args['pageIdx']
        img_url = 'http://www.ivsky.com/index.php?tn=indexload&page={}'.format(page)
        r = requests.get(img_url)
        img_json = r.json()
        data = []
        # http://img.ivsky.com/img/tupian/pre/201612/12/fankai_de_shuben.jpg
        for img in img_json:
            request_img = img['litpic'].replace('bizhi/pic', 'bizhi/pre')
            request_img = request_img.replace('tupian/pic', 'tupian/pre')
            temp = {
                'image': 'http://read.html5.qq.com/image?src=forum&q=5&r=0&imgflag=7&imageUrl=' + 'http://img.ivsky.com' + request_img,
                'title': img['title'],
                'content': img['description']
            }
            # s = requests.session()
            # print s.get(temp['image']).status_code
            data.append(temp)
        return data[:16]


class SearchApi(Resource):
    def post(self):
        args = search_post.parse_args()
        content = args['content']
        blog_lists = Blog.query.whoosh_search(content).all()
        user_lists = User.query.whoosh_search(content).all()
        comment_lists = Comment.query.whoosh_search(content).all()
        lists = blog_lists + user_lists + comment_lists
        parser = list(jieba.cut(content, cut_all=False))
        response_lists = []
        for l in lists:
            l_type = l.__class__.__name__
            l_dict = {}
            if l_type == "Blog":
                l_dict = {
                    'url': '/post/{}?{}'.format(l.id, query_search_to_string(parser)),
                    'type': l_type,
                    'content': l.title,
                    'id': l.id,
                }
            elif l_type == "Comment":
                blog_id = l.blog_id
                comment_index = l.index_of_comment_in_blog()
                url = '/post/{}?pageIdx={}&{}#comment{}'.format(blog_id,
                    str((comment_index + 15 - 1) / 15), query_search_to_string(parser),
                    str(l.id))
                l_dict = {
                    'url': url,
                    'type': l_type,
                    'content': l.content,
                    'id': l.id,
                }
            elif l_type == "User":
                l_dict = {
                    'url': '/user/{}?{}'.format(l.id, content),
                    'type': l_type,
                    'content': l.username,
                    'id': l.id,
                }
            response_lists.append(l_dict)
        return response_lists
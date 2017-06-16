# -*- coding: utf-8 -*-
from flask_restful import reqparse

# bloglist
# get
bloglist_get_parser = reqparse.RequestParser()
bloglist_get_parser.add_argument('pageIdx', type=int, location=['args', 'headers'])
bloglist_get_parser.add_argument('author', type=str, location=['args', 'headers'])
bloglist_get_parser.add_argument('quantity', type=int, location=['args', 'headers'])
bloglist_get_parser.add_argument('tag', type=str, location=['args', 'headers'])

# post
bloglist_post_parser = reqparse.RequestParser()
bloglist_post_parser.add_argument('author', type=str, required=True)
bloglist_post_parser.add_argument('title', type=str, required=True)
bloglist_post_parser.add_argument('content', type=str, required=True)

# put
bloglist_put_parser = reqparse.RequestParser()
bloglist_put_parser.add_argument('title', type=str)
bloglist_put_parser.add_argument('content', type=str)

# delete

# blogtitle
# get
blog_title_get_parser = reqparse.RequestParser()
blog_title_get_parser.add_argument('pageIdx', type=int)
blog_title_get_parser.add_argument('quantity', type=int)

# comment
# get
comment_get_parser = reqparse.RequestParser()
comment_get_parser.add_argument('pageIdx', type=str)
comment_get_parser.add_argument('quantity', type=str)

# post
comment_post_parser = reqparse.RequestParser()
comment_post_parser.add_argument('author', type=str, required=True)
comment_post_parser.add_argument('content', type=str, required=True)
comment_post_parser.add_argument('replyTo', type=str)
comment_post_parser.add_argument('href', type=str)

# delete
comment_delete_parser = reqparse.RequestParser()
comment_delete_parser.add_argument('commentId', type=int, required=True)

# login
# post
login_post = reqparse.RequestParser()
login_post.add_argument('username', type=str, required=True)
login_post.add_argument('password', type=str)

# register
# post
register_post = reqparse.RequestParser()
register_post.add_argument('username', type=str, required=True)
register_post.add_argument('password', type=str, required=True)
register_post.add_argument('email', type=str)

# message
# post
message_post = reqparse.RequestParser()
message_post.add_argument('sender', type=str, required=True)
message_post.add_argument('content', type=str, required=True)
message_post.add_argument('receiver', type=str, required=True)

# mentions
mention_post = reqparse.RequestParser()
mention_post.add_argument('name', type=str)

# 点赞
zan_post = reqparse.RequestParser()
zan_post.add_argument('href', type=str)

# 获取图片列表
img_get = reqparse.RequestParser()
img_get.add_argument('pageIdx', type=str)

# 搜索
search_post = reqparse.RequestParser()
search_post.add_argument('content', type=str)
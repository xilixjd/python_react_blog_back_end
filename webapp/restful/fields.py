# -*- coding: utf-8 -*-

from flask_restful import fields


page_fields = {
    'pageIdx': fields.Integer(),
    'quantity': fields.Integer(),
    'totalCount': fields.Integer()
}


def generate_data_wrap_fields(page=page_fields, nest_fields=None):
    if page:
        data_obj = {
            'paging': fields.Nested(page),
            'data': fields.Nested(nest_fields),
            'status_code': fields.String()
        }
    else:
        data_obj = {
            'data': fields.Nested(nest_fields),
            'status_code': fields.String()
        }
    return data_obj


nested_tag_fields = {
    'id': fields.Integer(),
    'title': fields.String()
}

nested_comment_fields = {
    'id': fields.Integer(),
    'time': fields.Integer(),
    'content': fields.String(),
    'author': fields.String()
}

blog_fields = {
    'id': fields.Integer(),
    'author': fields.String(),
    'title': fields.String(),
    'content': fields.String(),
    'time': fields.Integer(),
    'tags': fields.List(fields.Nested(nested_tag_fields)),
    # 'comments': fields.List(fields.Nested(nested_comment_fields))
}

blog_title_fields = {
    'id': fields.Integer(),
    'author': fields.String(),
    'title': fields.String(),
    'time': fields.Integer(),
    'tag': fields.String(),
}

tag_blog_fields = {
    'id': fields.Integer(),
    'author': fields.String(),
    'title': fields.String(),
    'time': fields.Integer(),
    # 'tags': fields.List(fields.Nested(nested_tag_fields)),
    'tags': fields.String()
}

comment_fields = {
    'id': fields.Integer(),
    'author': fields.String(),
    'content': fields.String(),
    'time': fields.Integer(),
    'receiver': fields.String(),
    'zan_count': fields.Integer(),
    'liked': fields.Integer(),
}

comment_page_fields = generate_data_wrap_fields(page_fields, comment_fields)
# {
#     'paging': fields.Nested(page_fields),
#     'data': fields.Nested(comment_fields)
# }

message_fields = {
    'id': fields.Integer(),
    'time': fields.Integer(),
    'checked': fields.String(),
    'sender': fields.String(),
    'content': fields.String(),
    'href': fields.String(),
    'message_type': fields.String()
}

user_fields = {
    'username': fields.String(),
    'messages': fields.List(fields.Nested(message_fields)),
    "uncheckedMessagesLen": fields.Integer(),
}

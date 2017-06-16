# -*- coding: utf-8 -*-

from webapp import create_app

from webapp.extensions import db

from webapp.models import User
from webapp.models import Blog
from webapp.models import Tag
from webapp.models import Comment
from webapp.models import Message
from webapp.models import Reply
from webapp.models import Zan
from webapp.models import Role

from flask_script import Manager
from flask_script import Server
from flask_script import prompt_bool
from flask_script.commands import ShowUrls

from flask_migrate import Migrate
from flask_migrate import MigrateCommand


app = create_app("webapp.config.DevConfig")

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)
manager.add_command('show-urls', ShowUrls())


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Blog=Blog,
        Comment=Comment,
        Tag=Tag,
        Zan=Zan,
        Role=Role,
    )


@manager.command
def dropdb():
    if prompt_bool('Are u sure ?'):
        db.drop_all()

if __name__ == '__main__':
    manager.run()
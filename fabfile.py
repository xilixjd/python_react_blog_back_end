# -*- coding: utf-8 -*-

from fabric.api import local, cd, run, env, lcd

env.hosts = ['ubuntu@118.89.143.159']


def local_git_operate():
    local('git add -A')
    local('git commit --allow-empty -m "fabric deploy"')
    local('git push')


def remote_git_operate():
    run('git fetch --all')
    run('git reset --hard origin/master')
    run('git pull')


def local_operate():
    with lcd('/Users/xilixjd/Desktop/python_react_blog1/python_react_blog_front_end'):
        local('cross-env NODE_ENV=production webpack')
        local_git_operate()
    with lcd('/Users/xilixjd/Desktop/python_react_blog1/python_react_blog_back_end'):
        local_git_operate()


def remote_operate():
    with cd('/home/ubuntu/python_react_blog/python_react_blog_front_end'):
        remote_git_operate()
    with cd('/home/ubuntu/python_react_blog/python_react_blog_back_end'):
        remote_git_operate()
        run('supervisorctl -c supervisor.conf reload')


def main():
    local_operate()
    remote_operate()


def hello():
    print("Hello world!")
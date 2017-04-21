# 个人博客后端 Flask Blog
[xjd的博客](http://www.xilixjd.cc)
## 技术栈
Python Flask

## 功能
查看博客文章

用户登录注册，发表评论，点赞

新消息提醒，@用户

## 快速开始
1.安装 redis，python2.7，mysql

2.安装依赖
```
pip2 install -r requirements.txt
```

3.在 app_blueprint.py 中将注释掉的初始化博客文章恢复，并运行视图函数，初始化数据库

4.启动 python_react_blog_back_end
```angular2html
python __init__.py
```

5.启动 mysql redis celery
```angular2html
redis-server
celery worker -A webapp.celery_worker.celery --loglevel=info
```

## 拓展库及应用
### redis
点赞，博客文章缓存
### flask_socketio
新消息通知
### celery
后台异步处理：缓存未命中时的数据库处理，发邮件
### flask_restful
restful API

## 线上配置
1.nginx

参考 nginx.conf

2.supervisor

参考 supervisor.conf

3.fabric

参考 fabfile.py

## Todo
### docker
### 上传图片
### flask_security 权限管理
### 为返回数据提供状态码（成功或失败）
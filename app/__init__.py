#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/28 20:47
# @Author  : Matrix
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from app.database import db
from app.config import configs
from app.webapi import webapi
__author__ = 'blackmatrix'

_no_value = object()


def create_app(app_config='default'):

    app = Flask(__name__)

    # 读取配置文件
    app.config.from_object(configs[app_config])
    # 蓝图注册
    register_blueprints(app)
    # 扩展注册
    register_extensions(app)

    @app.route('/', methods=['GET'])
    def index():
        return '<h1>请直接调用接口</h1>'

    return app


def register_blueprints(app):
    app.register_blueprint(webapi, url_prefix='/api')


def register_extensions(app):
    db.init_app(app)


if __name__ == '__main__':
    pass

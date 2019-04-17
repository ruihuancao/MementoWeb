#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/7 12:43
# @Author  : ruihuancao@gmail.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

index = Blueprint(
    'index',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views
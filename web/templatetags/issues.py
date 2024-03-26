#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.template import Library
from django.urls import reverse
from web import models

# 这里必须要写register，必须要写register
register = Library()


@register.simple_tag
def string_just(num):
    """自定义模版，适配长度"""
    if num < 100:
        num = str(num).rjust(3, "0")#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
    return "#{}".format(num)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import django

#模拟一下manage.py程序,离线脚本
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#程序的绝对路径
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ss25.settings")
django.setup()  # os.environ['DJANGO_SETTINGS_MODULE']
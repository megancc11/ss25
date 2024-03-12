import os
import sys
import django
from utils import encrypt

#模拟一下manage.py程序,离线脚本
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#程序的绝对路径
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ss25.settings")
django.setup()  # os.environ['DJANGO_SETTINGS_MODULE']


from web import models
# 往数据库添加数据：链接数据库、操作、关闭链接
models.UserInfo.objects.create(username='梅根', email='megan.chen@igg.com', mobile_phone='13959195082', password=encrypt.md5('123456789'))
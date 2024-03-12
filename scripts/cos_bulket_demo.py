#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""创建桶的示例代码"""
import base#先模拟一下manage.py程序,离线脚本
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from django.conf import settings
import time

# secret_id = settings.TENCENT_COS_ID  # 替换为用户的 secretId，默认只能创建两个秘钥
# secret_key = settings.TENCENT_COS_KEY # 替换为用户的 secretKey,在后台新建秘钥的时候保存，不要给别人
#
# region = 'ap-chengdu'  # 替换为用户的 Region
#
# token = None
# scheme = 'https'
# config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
#
# client = CosS3Client(config)
#
#
# response = client.create_bucket(
#     Bucket='test'+settings.BUCKET_SUFFIX,#把桶的后缀要改成和你手动创建桶的后缀一样
#     ACL="public-read"  #三种选项  private  /  public-read / public-read-write
# )

bucket = "{}-{}-{}".format('aaa','bbbb', str(int(time.time())))+settings.BUCKET_SUFFIX
print(bucket)
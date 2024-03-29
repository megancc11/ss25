#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""删除桶的示例代码"""
import base#先模拟一下manage.py程序,离线脚本
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from django.conf import settings

secret_id = settings.TENCENT_COS_ID  # 替换为用户的 secretId，默认只能创建两个秘钥
secret_key = settings.TENCENT_COS_KEY # 替换为用户的 secretKey,在后台新建秘钥的时候保存，不要给别人

region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

# client.delete_object(
#     Bucket='aa',
#     Key='p1.png'
# )

#批量删除
objects = {
    "Quiet": "true",
    "Object": [
        {
            "Key": "a.txt"
        },
        {
            "Key": "快捷键.txt"
        }
    ]
}

client.delete_objects(
    Bucket='13959195082-1710229382-1324595248',#把桶的后缀要改成和你手动创建桶的后缀一样
    Delete=objects
)

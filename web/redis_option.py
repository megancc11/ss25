from django.shortcuts import render, HttpResponse
import redis
from  django_redis import get_redis_connection

def redis(request):
    # 直接连接redis
    #安装模块pip3 install redis
    conn = redis.Redis(host='10.0.9.13',port=6379,password='123456', encoding='utf-8')

    # 设置键值:code=“8888”且超时时间为60秒(值写入到redis时会自动转字符串)
    conn.set('code',8888,ex=60)

    # 根据键获取值:如果存在获取值(获取到的是字节类型);不存在则返回None
    value = conn.get('code')
    print(value)
    return HttpResponse(value)


def redis_connectionpool(request):
    import redis
    # 创建redis连接池(默认连接池最大连接数 2**31=2147483648),max_connections是为了处理并发
    pool = redis.ConnectionPool(host='10.0.9.13', port=6379, password='123456', encoding='utf-8', max_connections=1000)
    #去连接池中获取一个连接
    conn= redis.Redis(connection_pool=pool)
    #设置键值:name=“megan”且超时时间为10秒(值写入到redis时会自动转字符串)
    conn.set('name',"megan",ex=10)

    #根据键获取值:如果存在获取值(获取到的是字节类型);不存在则返回None
    value=conn.get('name')

    print(value)
    return HttpResponse(value)

def django_redis(request):
    # 去连接池中获取一个连接
    conn=get_redis_connection("master")
    conn.set('nickname', "megan",ex = 10)
    value=conn.get('nickname')
    print(value)
    return HttpResponse(value)
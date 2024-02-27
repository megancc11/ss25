from django.shortcuts import render,HttpResponse
from utils.tencent.sms import send_sms_single
import random
# Create your views here.
def send_sms(request):
    """发送短信"""
    code=random.randrange(1000,9999)
    res=send_sms_single('135552','548760',[code,])
    print(res)
    if res['result']==0:
        return HttpResponse('发送成功')
    else:
        return HttpResponse('发送失败')

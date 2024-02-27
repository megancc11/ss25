from django.shortcuts import render,HttpResponse
from utils.tencent.sms import send_sms_single
import random
from django.conf import settings

def send_sms(request):
    """发送短信
    ?tpl=login ->1111
    ?tpl=register ->2222
    """
    tpl=request.GET.get('tpl')
    template_id=settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')

    code=random.randrange(1000,9999)
    res=send_sms_single('135552',template_id,[code,])
    print(res)
    if res['result']==0:
        return HttpResponse('发送成功')
    else:
        return HttpResponse('发送失败')

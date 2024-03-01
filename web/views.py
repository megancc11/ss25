from django.shortcuts import render, HttpResponse
from utils.tencent.sms import send_sms_single
import random
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from web import models

def send_sms(request):
    """发送短信
    ?tpl=login ->1111
    ?tpl=register ->2222
    http://127.0.0.1:8000/sms/send/?tpl=login
    签名未通过，无法用腾讯短信发送功能
    """
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)

    if not template_id:
        return HttpResponse('模板不存在')

    code = random.randrange(1000, 9999)
    res = send_sms_single('1111111', template_id, [code, ])
    print(res)
    if res['result'] == 0:
        return HttpResponse('发送成功')
    else:
        return HttpResponse('发送失败')


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|516|7|8|9])\d{9}$', '手机号格式错误'), ])
    password = forms.CharField(widget=forms.PasswordInput(),label="密码")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="重复密码")
    code = forms.CharField(label='验证码',widget=forms.TextInput(),)

    class Meta:
        model = models.UserInfo
        fields = ['username','password','confirm_password','mobile_phone','email','code']  # 修改页面展示顺序
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)  # 执行父类的__init__方法
        # 循环找到所有的字段，添加了class="form-control"样式
        for name, field in self.fields.items():
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": '请输入%s'%(field.label,)
                }

def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})


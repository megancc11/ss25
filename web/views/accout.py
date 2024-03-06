from django.shortcuts import render, HttpResponse,redirect
from utils.tencent.sms import send_sms_single
from utils.imagecode.code import check_code
import random
from django.conf import settings
from web.forms.account import RegisterModelForm,SendEmailForm,LoginForm,LoginEmailForm
from django.http import JsonResponse
from web import models
from django.db.models import Q
from io import BytesIO
"""
用户账户相关功能：注册、登录、短信、注销
"""

def register(request):
    """ 注册 """
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'web/register.html', {'form': form})
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过，写入数据库（密码要是密文）
        # instance = form.save，在数据库中新增一条数据，并将新增的这条数据赋值给instance

        # 用户表中新建一条数据（注册）
        instance = form.save()

        # 创建交易记录
        # 方式一
        # policy_object = models.PricePolicy.objects.filter(category=1, title="个人免费版").first()
        # models.Transaction.objects.create(
        #     status=2,
        #     order=str(uuid.uuid4()),
        #     user=instance,
        #     price_policy=policy_object,
        #     count=0,
        #     price=0,
        #     start_datetime=datetime.datetime.now()
        # )

        # 方式二

        return JsonResponse({'status': True, 'data': '/web/login/'})

    return JsonResponse({'status': False, 'error': form.errors})

def login(request):
    """ 用户名和密码登录 """
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'web/login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        #  (手机=username and pwd=pwd) or (邮箱=username and pwd=pwd)，构造复杂的查询条件则使用Q方法
        user_object = models.UserInfo.objects.filter(Q(email=username) | Q(mobile_phone=username)).filter(password=password).first()
        if user_object:
            # 登录成功
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 14)

            return redirect('index')

        form.add_error('username', '用户名或密码错误')

    return render(request, 'web/login.html', {'form': form})

def image_code(request):
    """ 生成图片验证码 """
    image_object, code = check_code()
    request.session['image_code'] = code
    request.session.set_expiry(60)  # 主动修改session的过期时间为60s,默认时区是UTC时区

    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())

def login_email(request):
    """邮箱验证码登录"""
    if request.method == 'GET':
        form = LoginEmailForm()
        return render(request, 'web/login_email.html', {'form': form})
    form = LoginEmailForm(request.POST)

    if form.is_valid():
        # 用户输入正确，登录成功
        email = form.cleaned_data['email']
        # 把用户名写入到session中
        user_object = models.UserInfo.objects.filter(email=email).first()
        request.session['user_id'] = user_object.id
        request.session.set_expiry(60 * 60 * 24 * 14)

        return JsonResponse({"status": True, 'data': "/web/index/"})

    return JsonResponse({"status": False, 'error': form.errors})

def logout(request):
    request.session.flush()#清空session数据
    return redirect('index')
#发送邮件获取验证码
def send_email(request):
    """ 发送邮件 """
    form = SendEmailForm(request,data=request.GET)
    # 只是校验Email：不能为空、格式是否正确
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})

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


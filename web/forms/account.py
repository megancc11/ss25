from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from web.forms.bootstrap import BootStrapForm
from web import models
import random
from utils.email import send_email
from django_redis import get_redis_connection
from utils import encrypt

class RegisterModelForm(BootStrapForm, forms.ModelForm):
    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=64,
        error_messages={
            'min_length': "密码长度不能小于8个字符",
            'max_length': "密码长度不能大于64个字符"
        },
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        label='重复密码',
        min_length=8,
        max_length=64,
        error_messages={
            'min_length': "重复密码长度不能小于8个字符",
            'max_length': "重复密码长度不能大于64个字符"
        },
        widget=forms.PasswordInput())

    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])

    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        fields = ['username', 'password', 'confirm_password', 'mobile_phone','email', 'code']#有校验的先后顺序

    def clean_username(self):
        username = self.cleaned_data['username']
        exists = models.UserInfo.objects.filter(username=username).exists()#创建索引可以提升查询速度
        if exists:
            raise ValidationError('用户名已存在')#抛出异常后不继续执行后续代码
            # self.add_error('username','用户名已存在')抛出异常后继续执行后续代码
        return username

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密 & 返回
        return encrypt.md5(pwd)

    def clean_confirm_password(self):

        pwd = self.cleaned_data.get('password')#验证一下是否已经存在
        confirm_pwd = encrypt.md5(self.cleaned_data['confirm_password'])#原密码已经加密了，所以需要加密后比对

        if pwd != confirm_pwd:
            raise ValidationError('两次密码不一致')

        return confirm_pwd

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('手机号已注册')
        return mobile_phone

    def clean_email(self):
        email = self.cleaned_data['email']
        exists = models.UserInfo.objects.filter(email=email).exists()
        if exists:
            raise ValidationError('邮箱已存在')
        return email

    def clean_code(self):
        code = self.cleaned_data['code']

        email = self.cleaned_data.get('email')#验证一下是否已经存在
        if not email:
            return code

        conn = get_redis_connection()
        redis_code = conn.get(email)
        if not redis_code:
            raise ValidationError('验证码失效或未发送，请重新发送')

        redis_str_code = redis_code.decode('utf-8')#B类型转换为字符串

        if code.strip() != redis_str_code:
            raise ValidationError('验证码错误，请重新输入')

        return code

class SendEmailForm(forms.Form):
    email = forms.CharField(
        label='邮件',
        widget=forms.EmailInput(),
        required=True # 不允许为空
    )
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_email(self):
        """邮箱校验的钩子 """
        email = self.cleaned_data['email']

        # 判断短信模板是否有问题
        tpl = self.request.GET.get('tpl')

        exists = models.UserInfo.objects.filter(email=email).exists()

        if tpl == 'login':
            if not exists:
                #self.add_error('email','邮件不存在')抛出错误信息继续执行后续代码
                raise ValidationError('邮件不存在')#抛出错误信息不执行后续代码
        else:
            # 注册校验数据库中是否已有邮件
            if exists:
                raise ValidationError('邮件已存在,请更换邮箱！')#抛出错误信息不执行后续代码

        code = random.randrange(1000, 9999)

        # 发送邮件
        send_status = send_email(email,tpl,code)
        if send_status==0:
            raise ValidationError('邮件发送失败')#抛出错误信息不执行后续代码

        # 验证码 写入redis（django-redis）

        conn = get_redis_connection()
        conn.set(email, code, ex=60)

        return email

class LoginEmailForm(BootStrapForm, forms.Form):
    email = forms.CharField(
        label='邮箱',
        widget = forms.EmailInput(),
        required=True  # 不允许为空
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        exists = models.UserInfo.objects.filter(email=email).exists()
        # user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()#返回一个用户对象
        if not exists:
            raise ValidationError('邮箱地址不存在')
        return email
        # return user_object

    def clean_code(self):

        email = self.cleaned_data.get('email')
        code = self.cleaned_data['code']

        # 邮件地址不存在，则验证码无需再校验
        if not email:
            return code

        conn = get_redis_connection()
        redis_code = conn.get(email)  # 根据手机号去获取验证码
        if not redis_code:
            raise ValidationError('验证码失效或未发送，请重新发送')

        redis_str_code = redis_code.decode('utf-8')

        if code.strip() != redis_str_code:
            raise ValidationError('验证码错误，请重新输入')

        return code

class LoginForm(BootStrapForm, forms.Form):
    username = forms.CharField(label='邮箱或手机号')

    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=64,
        error_messages={
            'min_length': "密码长度不能小于8个字符",
            'max_length': "密码长度不能大于64个字符"
        },
        widget=forms.PasswordInput(render_value=True)#render_value=True保留上一次收入的密码
    )

    code = forms.CharField(label='图片验证码')

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密 & 返回
        return encrypt.md5(pwd)

    def clean_code(self):
        """ 钩子 图片验证码是否正确？ """
        # 读取用户输入的验证码
        code = self.cleaned_data['code']

        # 去session获取自己的验证码
        session_code = self.request.session.get('image_code')

        if not session_code:
            raise ValidationError('验证码已过期，请重新获取')

        if code.strip().upper() != session_code.strip().upper():
            raise ValidationError('验证码输入错误')

        return code
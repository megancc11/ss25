from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """用户登录与注册"""
    #ID默认会生成且是主键,修改表类型也是同样的方法
    username=models.CharField(verbose_name="姓名",max_length=32)
    email=models.EmailField(verbose_name="邮箱",max_length=32)
    mobile_phone = models.CharField(verbose_name="手机号", max_length=11)
    password = models.CharField(verbose_name="密码", max_length=32)

    def __str__(self):
        return  self.username
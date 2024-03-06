import smtplib
from email.mime.text import MIMEText
from django.conf import settings

def send_email(email,send_type,code):
    """邮件发送"""
    emailname = email.split('@')[0]
    # 把验证码的发送到注册时的邮箱！
    if send_type == 'register':
        subject = '账号注册'
        mail_msg = '<p>您好，用户%s,请输入验证码%s,进行账号注册</p>' % (emailname,code)
    elif send_type =='forget':
        subject = '登录密码找回'
        mail_msg = '<p>您好，用户%s,请输入验证码%s,进行账号密码找回</p>' % (emailname,code)
    elif send_type =='login':
        subject = '登录验证码'
        mail_msg = '<p>您好，用户%s,请输入验证码%s,进行账号登录</p>' % (emailname,code)
    mail_host = settings.MAIL_HOST# 默认，设置服务器
    mail_user = settings.MAIL_USER # 用户名
    mail_pass = settings.MAIL_PASSWORD#服务器授权码
    sender = mail_user
    message = MIMEText(mail_msg,'html','utf-8')                
    message['Subject'] = subject
    message['From'] = 'DataBI <'+sender+'>'
    if send_type == 'register':
        message['To'] = email
        receivers = email
    else:
        message['To'] = email
        receivers = email
    reset = 1 #尝试发送次数
    while((reset >=1) & (reset <2)):
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host)
            smtpObj.login(mail_user, mail_pass)
            print('邮件登录成功')
            dd = smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
            reset = 0
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
            reset += 1
    if reset == 0:
        send_status = 1
    else:
        send_status = 0
    return send_status

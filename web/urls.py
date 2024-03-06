from django.urls import path
from web.views import accout,home

#前端写URL时需要加上web/
urlpatterns = [
    path('index/', home.index, name='index'),
    path('sms/send/', accout.send_sms),
    path('register/', accout.register,name='register'),
    path('login/', accout.login, name='login'),
    path('logout/', accout.logout, name='logout'),
    path('image/code/', accout.image_code, name='image_code'),
    path('login/email/', accout.login_email, name='loginemail'),
    path('send/email/', accout.send_email,name='send_email'),

]

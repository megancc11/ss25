from django.urls import path
from web.views import accout  as accout

urlpatterns = [

    path('sms/send/', accout.send_sms),
    path('register/', accout.register,name='register'),

]

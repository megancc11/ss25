from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from web.views import redis_option

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),

    path('redis/', redis_option.redis),
    path('redis_connectionpool/', redis_option.redis_connectionpool),
    path('django_redis/', redis_option.django_redis),
]

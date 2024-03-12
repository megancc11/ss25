"""
Django settings for ss25 project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')#l)bikt3m8god94mg8#kh0lh2#&yo0p)3+0uzj%0ls!1$7=q@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web.apps.WebConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'web.middleware.auth.AuthMiddleware'

]

ROOT_URLCONF = 'ss25.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'DIRS': [BASE_DIR, '/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ss25.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# ##########sms############

#腾讯云短信皮用的app_id
TENCENT_SMS_APP_ID =6666666666

#腾讯云短信应用的 app_key
TENCENT_SMS_APP_KEY="6666666666666666666666"

# 腾讯云短信签名内容
TENCENT_SMS_SIGN ="**********"

# 短信模板
TENCENT_SMS_TEMPLATE={
    'register':2081647,
    'login':2081645
}

#腾讯邮件发送设置
MAIL_HOST = "***"  # 默认，设置服务器
MAIL_USER = "***"  # 用户名
MAIL_PASSWORD = "***"  # 服务器授权码

#腾讯cos ID和KEY配置
TENCENT_COS_ID = "COS的secret_id"
TENCENT_COS_KEY = "COS的secret_key"
BUCKET_SUFFIX="COS桶的后缀-数字"


# ########### 登录白名单：无需登录就可以访问的页面 ###########
WHITE_REGEX_URL_LIST = [
    "/web/register/",
    "/web/send/email/",
    "/web/login/",
    "/web/login/email/",
    "/web/image/code/",
    "/web/index/",
    "/web/price/",
]

try:
    from .local_settings import *
except ImportError:
    pass
"""
Django settings for TeacherManager project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hzv6)*7a151tyd@fxbetzf2pbz&)ef9_)(2f5%k)7)0v%3xmcg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.checker',
    'apps.user'
)
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'apps.user.backends.UsernumBackend',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'TeacherManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'TeacherManager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# mysql数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Teachers',
        'HOST': '39.107.112.244',
        'PORT': 3306,
        'USER': 'python',
        'PASSWORD': '123456',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 指定django认证系统的模型类
AUTH_USER_MODEL='user.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# 设置静态文件存放的目录
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 邮件发送配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = 'hua2680465171@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'python666'
#收件人看到的发件人
EMAIL_FROM = 'python<hua2680465171@163.com>'



# 设置redis作为django的缓存设置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 把这里缓存你的redis服务器ip和port
        "LOCATION": "redis://127.0.0.1:6379/12",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 设置redis存储django的session信息
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
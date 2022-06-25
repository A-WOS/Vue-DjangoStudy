import os

from .base import *


SECRET_KEY = os.environ['SECRET_KEY']
# Debug = True : 개발모드 , False : 운영모드
DEBUG = False

# AWS Example

# ALLOWED_HOSTS 를 공백으로 놔두면 ['localhost', '127.0.0.1'] 인식한다.
ALLOWED_HOSTS = ['.elasticbeanstalk.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'django-mysql.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
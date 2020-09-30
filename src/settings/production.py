# -*- coding:utf-8 -*-
import os

DEBUG = False

ALLOWED_HOSTS = [
    'work_tasks.ru',
    '0.0.0.0',
]
SITE_HOST = 'work_tasks'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

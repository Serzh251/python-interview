from .prod import *

DEBUG = False

SITE_ID = 3
SECRET_KEY = 'django-insecure-j%3ipx@rbmzckvn3osh-1j@8==h7w4yei0+75cx0uv4kyay+a8'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'serzh',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432'
    }
}
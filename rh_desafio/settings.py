from pathlib import Path
from functools import partial
from decouple import config, Csv

import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'collectfast',
    'django.contrib.staticfiles',

    'core',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rh_desafio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rh_desafio.wsgi.application'

default_db_url = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

parse_database = partial(dj_database_url.parse, conn_max_age=600)

DATABASES = {
    'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
}

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# Configuração de ambiente de desenvolvimento

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

COLLECTFAST_ENABLED = True

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

# STORAGE CONFIGURATION IN S3 AWS
if AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age-86400', }
    AWS_PRELOAD_METADA = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_CUSTOM_DOMAIN = None
    AWS_DEFAULT_ACL = 'private'

    COLLECTFAST_ENABLED = True

    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"

    # Statics Assets
    # ----------------------------------------------------

    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = 'static'
    STATIC_ROOT = f'/{STATIC_S3_PATH}/'
    STATIC_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    # Upload Media Folder
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.StaticStorage'
    DEFAULT_S3_PATH = 'media'
    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}/'
    MEDIA_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{DEFAULT_S3_PATH}/'

    INSTALLED_APPS.append('s3_folder_storage')
    INSTALLED_APPS.append('storages')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

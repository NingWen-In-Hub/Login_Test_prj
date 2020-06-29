from .settings_common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'login_test_db',
        'USER': 'postgres',
        'PASSWORD': '0000',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
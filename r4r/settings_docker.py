from os import environ
from r4r.settings_shared import *  # noqa: F401,F403

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB'),
        'USER': environ.get('POSTGRES_USER'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD'),
        'HOST': 'r4r-db',
        'PORT': environ.get('POSTGRES_PORT'),
    }
}

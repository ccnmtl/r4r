# Django settings for r4r project.
import sys
from os import path, getenv
from ctlsettings.shared import common

project = 'r4r'
base = path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'r4r.main',
]

USE_TZ = True

if DEBUG:  # noqa
    INSTALLED_APPS += [  # noqa
        'debug_toolbar',
    ]
    MIDDLEWARE += [  # noqa
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

MIDDLEWARE += [  # noqa
    'django.middleware.csrf.CsrfViewMiddleware',
]

INSTALLED_APPS += [  # noqa
    'django_bootstrap5',
    'django_extensions',
    'markdownify.apps.MarkdownifyConfig',
    'r4r',
    'r4r.main',
    'rest_framework'
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

if not ('test' in sys.argv or 'jenkins' in sys.argv):
    AWS_ACCESS_KEY = getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = getenv('AWS_SECRET_KEY')
    AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')

    S3_MEDIA_BUCKET_NAME = 'ctl-r4r-static-stage'

    EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
    EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = True

    SENTRY_DSN = getenv('SENTRY-DSN')
    SENTRY_KEY = getenv('SENTRY-KEY')

    DATABASES = {
        'default': {
            'ENGINE': getenv('POSTGRES_ENGINE'),
            'HOST': getenv('POSTGRES_HOST'),
            'NAME': getenv('POSTGRES_NAME'),
            'PASSWORD': getenv('POSTGRES_PASSWORD'),
            'PORT': getenv('POSTGRES_PORT'),
            'USER': getenv('POSTGRES_USER'),
        }
    }


# Team count is constant throughout a given course
TEAM_COUNT = 12

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

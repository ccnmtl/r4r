# Django settings for r4r project.
from os import path
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
    'rest_framework',
    'drf_spectacular'
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Ready for Residency',
    'DESCRIPTION': 'A Columbia run Provost-funded project initiated by \
        Dr. Trudi Cloyd and managed by Columbia\'s Center for \
            Teaching and Learning',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

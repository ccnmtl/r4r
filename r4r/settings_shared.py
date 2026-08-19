# Django settings for r4r project.
import os.path
from ctlsettings.shared import common

project = 'r4r'
base = os.path.dirname(__file__)

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

    'r4r.main',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

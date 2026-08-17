# flake8: noqa
from r4r.settings_shared import *

try:
    from r4r.local_settings import *
except ImportError:
    pass

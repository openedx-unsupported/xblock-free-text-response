"""
Settings for freetextresponse xblock
"""

# Using the XBlock generic settings for a shorter settings file
from workbench.settings import *  # pylint: disable=all

# Fix "file not found" with the workbench.settings LOGGING config
from django.conf.global_settings import LOGGING  # pylint: disable=all


from os import path

REPO_ROOT = path.dirname(path.dirname(path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'intentionally-omitted',
    },
}
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'workbench',
    'freetextresponse',
)

SECRET_KEY = 'SECRET_KEY'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

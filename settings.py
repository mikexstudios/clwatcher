# Django settings for clwatcher project.
import os
import django
import sys

# For setting relative paths. See: http://tinyurl.com/adsa3k
# Path of Django framework files (no trailing /):
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
# Path of this "site" (no trailing /):
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#simplejson library needs this path:
#TODO: Set a check to see if path already exists. Since we are constantly
#      appending, this is bad if the python run is persistent.
#sys.path.append(os.path.join(SITE_ROOT, 'watcher')) 

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'clwatcher'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(pu*qhpr&7zzqm68m@20cc7b4bpcv)@=no122m3jb!_d74!hos'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', 
)

ROOT_URLCONF = 'clwatcher.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'watcher/templates'),
)

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    'clwatcher.watcher', 
    'debug_toolbar',
)

# Debug toolbar setting:
INTERNAL_IPS = ('127.0.0.1',)

#-------------
# Watcher Settings:
#update_interval = 30 #minutes

#Google Feeds API Key:
GOOGLE_FEEDS_API_KEY = 'ABQIAAAAZO-juu0ocGGR0i-QMcicihT2yXp_ZAY8_ufC3CFXhHIE1NvwkxQi7lKn-749OcSky89EeFc4dwmvIg'

#The number of existing posts that we need to encounter before we assume that
#the rest of the posts are also duplicate posts. (And hence, we don't need to
#check to see if they are new.)
DUPLICATE_POSTS_THRESHOLD= 2



#Import any local settings (ie. production environment) that will override
#these development environment settings.
try:
    from local_settings import *
except ImportError:
    pass 

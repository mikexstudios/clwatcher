import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'clwatcher.settings'

sys.path.append('/home/clwatcher/clwatcher_env')
sys.path.append('/home/clwatcher/clwatcher')
sys.path.append('/home/clwatcher')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

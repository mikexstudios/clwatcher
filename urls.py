from django.conf.urls.defaults import *
from django.conf import settings

import watcher.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^clwatcher/', include('clwatcher.foo.urls')),

    #TODO: Move this into watcher
    (r'^$', watcher.views.home), #default url
    (r'^add/$', watcher.views.add), 
    (r'^delete/(\d+)?$', watcher.views.delete), 

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    #Temporary fix for serving static files in dev environment.
    #See: http://docs.djangoproject.com/en/dev/howto/static-files/
    #In production setting, the webserver automatically overrides this, 
    #so there is no need to take this out when in production:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),

)

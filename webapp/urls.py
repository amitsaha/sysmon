from django.conf.urls.defaults import patterns, include, url
from webapp.views import sysmon, battery, networks, gettime

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',sysmon),
                       url(r'^battery/$',battery),
                       url(r'^networks/$',networks),
                       url(r'^time/$',gettime)
                       )

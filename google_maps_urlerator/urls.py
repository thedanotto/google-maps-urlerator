from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'urlerator.views.home', name='home'),
    url(r'^google-maps/$', 'urlerator.views.home', name='google-maps'),
)

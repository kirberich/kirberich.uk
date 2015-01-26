from django.conf.urls import patterns, include, url

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^_ah/', include('djangae.urls')),
    url(r'.*', include('core.urls')),
)

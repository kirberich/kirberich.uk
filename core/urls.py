from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'core.views.main', name='main'),
)

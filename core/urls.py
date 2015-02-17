from django.conf.urls import patterns, url

from views import main, article


urlpatterns = patterns('',
    url(r'^(?P<article_slug>\w+)', article, name="article"),
    url(r'^$', main, name='main'),
)

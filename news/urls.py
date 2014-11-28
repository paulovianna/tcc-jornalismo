from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name='home'),
    url(r'^noticia/(?P<id>\d+)', 'news.views.noticia', name='noticia'),
    url(r'^noticias/(?P<categoria>\w+)', 'news.views.noticias_categoria', name='noticias_categoria'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static-files/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)

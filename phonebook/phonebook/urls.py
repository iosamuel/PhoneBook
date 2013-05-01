from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'principal.views.index'),
	url(r'^detalle/(?P<id>\d+)$', 'principal.views.detalle'),

    url(r'^admin/', include(admin.site.urls)),
)

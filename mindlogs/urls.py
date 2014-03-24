from django.conf.urls import patterns, include, url
from views import IndexView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounts/', include('activity.urls', namespace='activity')),
    url(r'^activity/', include('activity.urls', namespace='activity')),
)

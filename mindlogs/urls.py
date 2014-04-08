from django.conf.urls import patterns, include, url
from views import IndexView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # APPs
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^activities/', include('activities.urls', namespace='activities')),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
)

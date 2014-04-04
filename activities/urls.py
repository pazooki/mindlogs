from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.ActivityList.as_view(), name='activity_list'),
    url(r'(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view(), name='activity_detail'),
)
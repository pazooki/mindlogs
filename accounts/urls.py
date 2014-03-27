from django.conf.urls import include
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^accounts/$', views.UserList.as_view()),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
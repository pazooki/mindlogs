from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views


urlpatterns = patterns('',

    url(r'^$', 'api_root'),

    url(r'^authors/', views.AuthorList.as_view()),
    url(r'^authors/^$', views.AuthorList.as_view()),
    url(r'^authors/(?P<pk>\w+)/$', views.AuthorDetail.as_view()),

    url(r'^posts/', views.PostList.as_view()),
    url(r'^posts/^$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)
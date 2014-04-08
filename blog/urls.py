from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views


urlpatterns = patterns('',


    url(r'authors/', views.AuthorList.as_view(), name='author_list'),
    url(r'authors/^$', views.AuthorList.as_view(), name='author_list'),
    url(r'authors/(?P<pk>[0-9]+)/$', views.AuthorList.as_view(), name='author_detail'),

    url(r'posts/', views.PostList.as_view(), name='post_list'),
    url(r'posts/^$', views.PostList.as_view(), name='post_list'),
    url(r'posts/(?P<pk>[0-9]+)/$', views.PostList.as_view(), name='post_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
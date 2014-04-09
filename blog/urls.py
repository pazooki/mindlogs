from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views


urlpatterns = patterns('',

    url(r'^$', 'api_root'),

    url(r'authors/', views.AuthorList.as_view(), name='author-list'),
    url(r'authors/^$', views.AuthorList.as_view(), name='author-list'),
    url(r'authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view(), name='author-detail'),

    url(r'posts/', views.PostList.as_view(), name='post-list'),
    url(r'posts/^$', views.PostList.as_view(), name='post-list'),
    url(r'posts/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='post-detail'),

    url(r'comments/', views.CommentList.as_view(), name='comment-list'),
    url(r'comments/^$', views.CommentList.as_view(), name='comment-list'),
    url(r'comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name='comment-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
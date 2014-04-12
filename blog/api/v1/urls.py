from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from blog.api.v1 import views


router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)


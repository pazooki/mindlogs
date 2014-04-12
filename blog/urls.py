from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from blog.api.v1 import views as v1_views


router = DefaultRouter()
router.register(r'v1/authors', v1_views.AuthorViewSet)
router.register(r'v1/posts', v1_views.PostViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router)),
)


print '#'*200
print urlpatterns
print '#'*200

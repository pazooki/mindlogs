from django.conf.urls import patterns
from blog.api.v1.urls import urlpatterns as v1_urls

print '#'*200
print v1_urls
print '#'*200

urlpatterns = patterns(
    ''
)

urlpatterns += v1_urls



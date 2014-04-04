from django.conf.urls import include
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    # Social Auth:
    url(r'^login/$', views.login),
    url(r'^signup-email/', views.signup_email),
    url(r'^email-sent/', views.validation_sent),
    url(r'^logout/$', views.logout),
    url(r'^done/$', views.done, name='done'),
    url(r'^email/$', views.require_email, name='require_email'),
)

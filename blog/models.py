from django.db import models

from django.contrib.auth.models import User


class User(User):
    pass


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

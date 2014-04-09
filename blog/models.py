from django.db import models
from django.contrib.auth.models import User


Author = User


class Post(models.Model):
    author = models.ForeignKey(Author, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('created',)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ('created',)
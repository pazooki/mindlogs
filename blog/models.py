from django.db import models
from django.contrib.auth.models import User

Author = User


class Post(models.Model):
    author = models.ForeignKey(Author, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('created_at',)

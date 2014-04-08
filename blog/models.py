from django.db import models

from django.contrib.auth.models import User


class User(User):
    pass


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     """
    #     Could do whatever before save
    #     """
    #     super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)

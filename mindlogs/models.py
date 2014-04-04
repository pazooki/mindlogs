from activities.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from django.db import models

# Create your models here.

class IndexModel(models.Model):
    info = 'Mindlogs Info'

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def __unicode__(self):
        return self.info
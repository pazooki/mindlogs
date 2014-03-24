from django.db import models

# Create your models here.

class IndexModel(models.Model):
    info = 'Mindlogs Info'

    def __unicode__(self):
        return self.info
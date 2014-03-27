from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class ActivityModel(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    activity = models.CharField(max_length=300)


class ActivityForm(ModelForm):
    class Meta:
        model = ActivityModel
        exclude = ['user']
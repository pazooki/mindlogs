from django.db import models
from account.models import AccountModel
from django.forms import ModelForm


class ActivityModel(models.Model):
    account = models.ForeignKey(AccountModel)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    activity = models.CharField(max_length=300)


class ActivityForm(ModelForm):
    class Meta:
        model = ActivityModel
        exclude = ['account']
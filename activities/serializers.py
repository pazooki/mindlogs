from activities.models import ActivityModel
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        fields = ('id', 'account', 'created', 'activity')
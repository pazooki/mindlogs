from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'user', 'created', 'activity')
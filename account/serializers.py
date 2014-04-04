from account.models import AccountModel
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = AccountModel
        fields = ('id',)
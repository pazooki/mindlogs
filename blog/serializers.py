from django.contrib.auth.models import User
from blog.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.Field(source='author.username')
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
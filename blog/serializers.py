from blog.models import Post, Author
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.Field(source='author.username')
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body')


class AuthorSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Author
        fields = ('id', 'username', 'posts')
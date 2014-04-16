from rest_framework import serializers

from blog.models import Post, Author


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'title', 'body')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail')

    class Meta:
        model = Author
        fields = ('url', 'id', 'username', 'posts')

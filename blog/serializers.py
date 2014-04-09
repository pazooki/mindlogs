from blog.models import Post, Author
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'title', 'body')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        lookup_field='username',
        view_name='post-list',
        format='html'
    )

    class Meta:
        model = Author
        fields = ('url', 'id', 'posts')

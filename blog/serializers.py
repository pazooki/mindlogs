from blog.models import Post, Comment, Author
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.username')
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-list', format='html')
    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'title', 'body')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.username')
    class Meta:
        model = Comment
        fields = ('url', 'id', 'author', 'body')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-list', format='html')

    class Meta:
        model = Author
        fields = ('url', 'id', 'posts')

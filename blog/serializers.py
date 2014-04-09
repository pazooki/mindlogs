from blog.models import Post, Comment, Author
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.Field(source='author.username')
    class Meta:
        model = Post
        fields = ('url', 'author', 'title', 'body')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.Field(source='author.username')
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', format='html')
    class Meta:
        model = Comment
        fields = ('url', 'author', 'body')

# class AuthorSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True)
#
#     class Meta:
#         model = Author
#         fields = ('id', 'username', 'posts')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-list', format='html')

    class Meta:
        model = Author
        fields = ('url', 'username', 'posts')
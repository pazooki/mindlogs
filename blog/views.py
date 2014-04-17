from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response

from blog.models import Post, Author
from blog.permissions import IsAdminOrReadOnly
from blog.api.v1.serializers import PostSerializer, AuthorSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



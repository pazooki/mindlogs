from blog.models import Post, User
from blog.serializers import PostSerializer, UserSerializer
from rest_framework import generics, permissions


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

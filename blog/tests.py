from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Author
from blog.api.v1.serializers import PostSerializer

class PostTests(APITestCase):
    fixtures = ['blog_author.json', 'blog_post.json']

    def setUp(self):
        mindlogger = 'mindlogger'
        self.client.login(username=Author.objects.get(username=mindlogger), password=mindlogger)

    def test_create_post(self):
        test_fields = ['author', 'title', 'body']
        url = reverse('post-list')
        data = PostSerializer(Post.objects.get(pk=1)).data
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=(response, data))
        self.assertEqual(
            [response.data.get(field) for field in test_fields],
            [data.get(field) for field in test_fields],
            msg=(response.data, data)
        )


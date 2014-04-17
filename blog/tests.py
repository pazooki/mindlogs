from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post
from common.converters import jsonify

class PostTests(APITestCase):
    fixtures = ['blog_author.json', 'blog_post.json']

    def test_create_post(self):
        url = reverse('post-list')
        data = jsonify(Post.objects.get(pk=1))
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


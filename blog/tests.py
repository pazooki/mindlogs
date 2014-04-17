from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post
from django.core import management

class PostTests(APITestCase):
    fixtures = ['blog_author.json', 'blog_post.json']

    @classmethod
    def setUpClass(cls):
        cls.Post = Post
        super(PostTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
    #     cls.Post.clean()
        super(PostTests, cls).tearDownClass()

    def test_submit(self):
        url = reverse('post-list')
        print self.Post.objects.filter(pk=1)
        data = self.Post.objects.filter(pk=1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


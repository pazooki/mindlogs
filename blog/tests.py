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
        post_id = '1'
        data = PostSerializer(Post.objects.get(pk=post_id)).data
        url = reverse('post-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=(url, response.status_code, data))
        self.assertEqual(
            [response.data.get(field) for field in test_fields],
            [data.get(field) for field in test_fields],
            msg=(response.data, data)
        )

    def test_get_post(self):
        test_fields = ['author', 'title', 'body']
        post_id = '1'
        data = PostSerializer(Post.objects.get(pk=post_id)).data
        url = reverse('post-detail', kwargs={'pk': post_id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=(url, response.status_code, data))
        self.assertEqual(
            [response.data.get(field) for field in test_fields],
            [data.get(field) for field in test_fields],
            msg=(response.data, data)
        )

    def test_delete_post(self):
        # TODO: fix this ugly url
        url = reverse('post-list') + '1/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=(url, response.status_code))
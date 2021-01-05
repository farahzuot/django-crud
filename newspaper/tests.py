from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.
class NewsTest(TestCase):
    def setUp(self):
        self.user= get_user_model().objects.create_user(
            username = 'user1',
            email = 'useruser@gmail.com',
            password = '123123user'
        )
        self.post = Post.objects.create(
            title = 'test',
            author = self.user,
            body = 'test test'
        )
    
    def test_news_status(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_details_status(self):
        res = self.client.get(reverse('details', args='1'))
        self.assertEqual(res.status_code,200)

    def test_details_content(self):
        res = self.client.get(reverse('details', args='1'))
        self.assertContains(res , 'test')

    def test_update_content(self):
        res = self.client.post(reverse('update', args='1'), {
            'title' : 'google',
        })
        self.assertContains(res, 'google')
        self.assertNotContains(res, 'test')
    
    def test_add_content(self):
        res = self.client.post(reverse('delete', args='1'))
        res2 = self.client.get(reverse('home'))
        self.assertNotContains(res2,'test')

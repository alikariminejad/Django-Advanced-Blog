from django.test import TestCase
from datetime import datetime

from ..models import  Post
from accounts.models import User,Profile

class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='12@12345$')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name='test_name',
            last_name='test_last_name',
            description='test_description',)
    def test_create_post_with_data(self):
        post = Post.objects.create(
        author = self.profile,
        title='test',
        content='test',
        status=True,
        published_date=datetime.now(),
        category=None)
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title, 'test')

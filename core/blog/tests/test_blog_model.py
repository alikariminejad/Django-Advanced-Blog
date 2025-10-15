from django.test import TestCase
from datetime import datetime

from ..models import  Post,Category
from django.contrib.auth import get_user_model
from ...accounts.models import User,Profile

class TestPostModel(TestCase):
    user = User.objects.create_user(email='test', password='12@12345$')
    profile = Profile.objects.create(
        user=user,
        first_name='test_name',
        last_name='test_last_name',
        description='test_description',)
    def test_create_post_with_data(self):
        post = Post.objects.create(
        author = profile,
        title='test',
        content='test',
        description='test',
        status=True,
        published_date=datetime.now(),
        category=None)
        self.assertEqual(post.title, 'test')

from django.test import TestCase
from datetime import datetime

from ..forms import  PostForm
from ..models import  Category

class TestPostForm(TestCase):
    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name="test")
        form = PostForm(data={
            'title': 'test',
            'content': 'test',
            'description': 'test',
            'status': True,
            'published_date': datetime.now(),
            'category': category_obj})
        self.assertTrue(form.is_valid())

    def test_post_form_with_no(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
import datetime
from django.urls import reverse, resolve
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self):
        client = APIClient()
        url = reverse("blog:api-v1:post-list")
        response = client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_401_status(self):
        url = reverse("blog:api-v1:post-list")
        data = {
            'title':'test',
            'content':'description',
            'status':True,
            'published_date':datetime.now()
        }
        response = self.client.post(url,data)
        assert response.status_code == 401
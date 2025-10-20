from django.http import HttpResponse, JsonResponse
import time
from django.core.cache import cache
from .tasks import sendEmail
import requests


def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get("")
        cache.set("test_delay_api", response.json(),60)
    return JsonResponse(cache.get("test_delay_api"))
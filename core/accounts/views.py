from django.http import HttpResponse, JsonResponse
import time
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .tasks import sendEmail
import requests

@cache_page(60)
def test(request):
    response = requests.get("")
    return JsonResponse(response.json())
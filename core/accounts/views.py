from django.http import HttpResponse, JsonResponse
import time
from .tasks import sendEmail
import requests


def test(request):
    response = requests.get("")
    return JsonResponse(response.json())
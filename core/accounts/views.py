from django.http import HttpResponse
import time
from .tasks import sendEmail

def send_email(request):
    sendEmail.delay(3)
    return HttpResponse("<h1>Done Sending</h1>")
from django.http import HttpResponse
from django.shortcuts import render

from mainapp.tasks import test_task
from send_mail_app.tasks import send_mail_func


def test(request):
    test_task.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    result = send_mail_func.delay()
    print(result)  # Optional: see task ID
    return HttpResponse("Send")

from django.http import HttpResponse
from django.shortcuts import render

from mainapp.tasks import test_task
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, ClockedSchedule
import json


def test(request):
    test_task.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    result = send_mail_func.delay()
    print(result)  # Optional: see task ID
    return HttpResponse("Send")


import datetime


def shcedule_mail(request):
    time_obj = datetime.time(hour=22, minute=8)
    schedule, created = ClockedSchedule.objects.get_or_create(clocked_time=time_obj)
    task = PeriodicTask.objects.create(
        clocked=schedule,
        name="schedule_mail_task11",
        task="send_mail_app.tasks.send_mail_func",
        args=json.dumps([1, 2]),
    )

    return HttpResponse("Send")

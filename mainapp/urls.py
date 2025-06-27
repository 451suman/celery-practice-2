from mainapp.views import send_mail_to_all, test
from django.urls import include, path

urlpatterns = [
    path("", test, name="task_list"),
    path("send/mail/", send_mail_to_all, name="send_mail_to_all"),
]
""
# 'celery -A core.celery worker --pool=solo -l info'
# celery -A core.celery beat -l info

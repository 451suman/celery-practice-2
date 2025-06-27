import os
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from time import sleep

User = get_user_model()


@shared_task(bind=True)
def send_mail_func(self):
    print("triggered send_mail_func")
    from_email = os.environ.get("EMAIL_HOST_USER")
    users = User.objects.all()
    for user in users:
        mail_subject = "Test mail"
        message = "This is a test mail message"
        to_email = user.email
        try:
            send_mail(
                subject=mail_subject,
                message=message,
                from_email=from_email,
                recipient_list=[to_email],
                fail_silently=False,  # Raise exceptions for debugging
            )
            print(f"Sent mail to {to_email}")
        except Exception as e:
            print(f"Failed to send mail to {to_email}: {e}")

    return "Done"

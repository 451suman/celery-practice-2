from celery import shared_task
from time import sleep  # Corrected import


@shared_task(bind=True)
def test_task(self):
    sleep(20)  # Simulates some delay
    return "done 1 1 1"  # Moved return outside the loop

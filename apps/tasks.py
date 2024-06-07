from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def send_email(email, code):
    send_mail('hh.uz', str(code), EMAIL_HOST_USER, [email])

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField
from rest_framework.fields import DateTimeField


class User(AbstractUser):
    phone = CharField(max_length=20, null=True, blank=True)

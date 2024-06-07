from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, EmailField, OneToOneField, CASCADE
from rest_framework.authtoken.models import Token, TokenProxy
from root.settings import AUTH_USER_MODEL, INSTALLED_APPS
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone = CharField(max_length=20, null=True, blank=True)
    email = EmailField(max_length=60, unique=True)


class CustomToken(Token):
    user = None
    email = OneToOneField(
        AUTH_USER_MODEL, related_name='custom_token',
        on_delete=CASCADE, verbose_name=_("Email")
    )

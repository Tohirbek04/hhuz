from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserCreateSerializer


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = AllowAny,


class SendEmailAPIView(APIView):

    def get(self, request, email):
        send_mail('Tema', 'xabar', EMAIL_HOST_USER, [email])
        return {'message': f'Email sent {email}'}

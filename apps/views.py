import random

from django.core.cache import cache
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.filters import VacancyFilterSet
from apps.models import Vacancy
from apps.permissions import IsOwner
from apps.serializers import VacancyRetrieveSerializers, VacancyListSerializer, VacancyCreateSerializers, \
    SendEmailSerializers, SendEmailCodeSerializers
from root.settings import EMAIL_HOST_USER
from users.models import CustomToken


class VacancyListCreateAPIView(ListCreateAPIView):
    queryset = Vacancy.objects.all()
    permission_classes = AllowAny,
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilterSet

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VacancyListSerializer
        return VacancyCreateSerializers


class VacancyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyRetrieveSerializers
    permission_classes = IsOwner,


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(cache.get('user1'), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SendEmailSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = random.randint(10 ** 5, 10 ** 6)
        send_mail('hh.uz', str(code), EMAIL_HOST_USER, [serializer.data.get('email')])
        # send_email.delay(code, serializer.data.get('email'))
        cache.set(f'{code}', serializer.data, 60)
        return Response("Enter the code sent to your email !", status=status.HTTP_200_OK)


class CustomTokenAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SendEmailCodeSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = cache.get(f'{serializer.data}')
        if email:
            token, created = CustomToken.objects.get_or_create(email=email)
            return Response({
                'token': token.key,
                'email': email
            })
        else:
            return Response("code invalid !")

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.filters import VacancyFilterSet
from apps.models import Vacancy
from apps.permissions import IsOwner
from apps.serializers import VacancyRetrieveSerializers, VacancyListSerializer, VacancyCreateSerializers


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

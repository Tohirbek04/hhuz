from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.models import Vacancy


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = 'title', 'price', 'district'


class VacancyCreateSerializers(ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = 'user',


class VacancyRetrieveSerializers(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = 'title', 'price', 'district', 'description', 'compony', 'experience'


class SendEmailSerializers(serializers.Serializer):
    email = serializers.EmailField(max_length=50)


class SendEmailCodeSerializers(serializers.Serializer):
    code = serializers.IntegerField()

from rest_framework.serializers import ModelSerializer

from apps.models import Vacancy


class VacancyListSerializer(ModelSerializer):

    class Meta:
        model = Vacancy
        fields = 'title', 'price','district'


class VacancyCreateSerializers(ModelSerializer):

    class Meta:
        model = Vacancy
        exclude = 'user',


class VacancyRetrieveSerializers(ModelSerializer):

    class Meta:
        model = Vacancy
        fields = 'title', 'price', 'district', 'description', 'compony', 'experience'

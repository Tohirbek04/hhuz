import django_filters

from apps.models import Vacancy


class VacancyFilterSet(django_filters.FilterSet):
    work_time = django_filters.ChoiceFilter(choices=Vacancy.WorkTime.choices)

    class Meta:
        model = Vacancy
        fields = {
            'title': ['icontains'],
            'experience': ['exact']
        }

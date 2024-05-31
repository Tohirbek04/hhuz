from django.contrib import admin

from apps.models import Vacancy


@admin.register(Vacancy)
class VacancyModelAdmin(admin.ModelAdmin):
    pass


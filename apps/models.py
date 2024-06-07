from django.db.models import Model, CharField, FloatField, ForeignKey, CASCADE, IntegerField, TextChoices
from django_ckeditor_5.fields import CKEditor5Field


class District(Model):
    name = CharField(max_length=50)


class Vacancy(Model):
    title = CharField(max_length=255)
    price = FloatField(null=True, blank=True)
    compony = CharField(max_length=30)
    description = CKEditor5Field(config_name='extends')
    user = ForeignKey('users.User', on_delete=CASCADE)
    experience = IntegerField()
    district = ForeignKey('apps.District', on_delete=CASCADE)

    class WorkTime(TextChoices):
        FULL = 'full_time', 'Full Time'
        PART = 'part_time', 'Part Time'
        PROJECT = 'project_work', 'Project Time'

    work_time = CharField(max_length=30, choices=WorkTime.choices)



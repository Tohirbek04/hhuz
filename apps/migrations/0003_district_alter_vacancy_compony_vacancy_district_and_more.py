# Generated by Django 5.0.6 on 2024-05-31 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='compony',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.district'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Compony',
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-13 03:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='registered_course',
            field=models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

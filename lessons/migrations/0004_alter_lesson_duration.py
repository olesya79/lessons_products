# Generated by Django 4.1.3 on 2023-09-29 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_alter_lesson_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.DateTimeField(verbose_name=datetime.timedelta(0)),
        ),
    ]
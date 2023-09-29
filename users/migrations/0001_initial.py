# Generated by Django 4.1.3 on 2023-09-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['first_name'],
            },
        ),
    ]

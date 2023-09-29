from core.abstract_models import Abstract
from django.db import models


class User(Abstract):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name

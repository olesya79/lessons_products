from core.abstract_models import Abstract
from core.enums.lesson_enums import StatusOflesson
from django.db import models
from products.models import Product
from users.models import User
import datetime
from datetime import timedelta


class Lesson(Abstract):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration = models.DateTimeField(datetime.timedelta(seconds=0))
    products = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class LessonView(Abstract):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.DateTimeField()
    status = models.CharField(
        max_length=15,
        choices=StatusOfleson.choices
    )

    class Meta:
        ordering = ['status']
        verbose_name = 'Статус просмотра'
        verbose_name_plural = 'Статусы просмотров'

    def __str__(self):
        return self.lesson

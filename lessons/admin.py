from django.contrib import admin
from lessons.models import Lesson, LessonView
from django.db.models import QuerySet


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'video_link', 'duration', 'products']
    ordering = ['name']
    search_fields = ['name__istartwith']


@admin.register(LessonView)
class LessonViewAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'view_time', 'status']
    ordering = ['user']
    search_fields = ['user']

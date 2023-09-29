from rest_framework import serializers
from lessons.models import Lesson, LessonView

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ['lesson', 'view_time', 'status']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'video_link', 'duration', 'lesson_views', 'time_create']
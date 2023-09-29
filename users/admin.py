from django.contrib import admin
from users.models import User
from django.db.models import QuerySet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name']
    ordering = ['second_name']
    search_fields = ['second_name__istartwith']



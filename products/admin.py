from products.models import Product, Owner
from django.contrib import admin
from django.db.models import QuerySet


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    ordering = ['name']
    search_fields = ['name__istartwith']

    @admin.action()
    def lessons(self, request, pk=None):
        product = self.get_object()
        lessons = Lesson.objects.filter(product=product)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

    @admin.action()
    def statistics(self, request, pk=None):
        product = self.get_object()
        students = product.students.all()
        lesson_views = LessonView.objects.filter(lesson__product=product)
        total_lessons_viewed = lesson_views.count()
        total_view_time = lesson_views.aggregate(total_time=Sum('view_time'))['total_time'] or 0

        data = {
            'total_lessons_viewed': total_lessons_viewed,
            'total_view_time': total_view_time,
            'total_students': students.count(),
            'access_percentage': students.count() / User.objects.count() * 100,
        }
        return Response(data)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'age', 'contact', 'phone']
    ordering = ['second_name']
    search_fields = ['second_name']

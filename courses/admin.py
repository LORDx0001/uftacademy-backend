from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title_en", "duration", "created_at")
    search_fields = ("title_en", "title_uz", "title_ru")
    list_filter = ("created_at",)

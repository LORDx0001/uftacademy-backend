from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title_uz", "title_ru", "title_en", "duration", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title_uz", "title_ru", "title_en")

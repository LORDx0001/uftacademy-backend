from django.contrib import admin
from .models import Title


@admin.register(Title)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title_uz", "title_ru", "title_en")
    search_fields = ("title_uz", "title_ru", "title_en")

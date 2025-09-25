from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "title_uz", "title_ru", "title_en", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title_uz", "title_ru", "title_en")

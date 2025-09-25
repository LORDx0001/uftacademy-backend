from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "title_en", "created_at")
    search_fields = ("title_en", "title_uz", "title_ru")
    list_filter = ("created_at",)

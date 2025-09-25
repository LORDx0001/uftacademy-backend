from django.contrib import admin
from .models import Footer


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("id", "title_en", "created_at")
    search_fields = ("title_en", "title_uz", "title_ru")

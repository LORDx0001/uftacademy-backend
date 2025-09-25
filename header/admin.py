from django.contrib import admin
from .models import Header

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("id", "title_uz", "created_at")
    search_fields = ("title_uz", "title_ru", "title_en")

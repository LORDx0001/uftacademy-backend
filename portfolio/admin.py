from django.contrib import admin
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "title_en", "created_at")
    search_fields = ("title_en", "title_uz", "title_ru")
    list_filter = ("created_at",)

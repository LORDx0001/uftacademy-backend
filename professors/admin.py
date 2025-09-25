from django.contrib import admin
from .models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "position_en")
    search_fields = ("full_name", "position_en", "position_uz", "position_ru")

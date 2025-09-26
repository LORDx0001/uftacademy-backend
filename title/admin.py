from django.contrib import admin
from .models import Title

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('key', 'title_uz', 'title_ru', 'title_en')
    search_fields = ('key', 'title_uz', 'title_ru', 'title_en')
    list_filter = ('key',)

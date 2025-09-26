from django.contrib import admin
from .models import Header

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en', 'created_at')
    search_fields = ('title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en')
    readonly_fields = ('created_at',)

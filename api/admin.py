from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Course,
    Teacher,
    PortfolioItem,
    InfoBlock,
    ContactMessage,
    SocialMedia,
    SectionTitle,
    HeaderSection
)

# 🔹 КУРСЫ
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'duration', 'image_preview')
    search_fields = ('title_uz', 'title_ru', 'title_en')
    list_filter = ('duration',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height:100px;" />', obj.image)
    image_preview.short_description = "Превью"

@admin.register(HeaderSection)
class HeaderSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ru', 'logo_preview')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" style="height:50px;" />'
        return "-"
    logo_preview.allow_tags = True
    logo_preview.short_description = "Превью логотипа"

# 🔹 ПРЕПОДАВАТЕЛИ
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'avatar_preview')
    search_fields = ('name_uz', 'name_ru', 'name_en')
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        return format_html('<img src="{}" style="max-height:100px;" />', obj.avatar)
    avatar_preview.short_description = "Аватар"


# 🔹 ПОРТФОЛИО
@admin.register(PortfolioItem)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'category', 'image_preview')
    search_fields = ('title_uz', 'title_ru', 'title_en')
    list_filter = ('category',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height:100px;" />', obj.image)
    image_preview.short_description = "Изображение"


# 🔹 ИНФО-БЛОКИ
@admin.register(InfoBlock)
class InfoBlockAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'icon')
    search_fields = ('title_uz', 'title_ru', 'title_en')


# 🔹 СООБЩЕНИЯ
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'telegram', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone', 'telegram')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)



@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon_preview', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'url')

    def icon_preview(self, obj):
        return format_html('<img src="{}" style="height:30px;" />', obj.icon_url)
    icon_preview.short_description = "Иконка"
    
@admin.register(SectionTitle)
class SectionTitleAdmin(admin.ModelAdmin):
    list_display = ('key', 'title_ru', 'title_uz', 'title_en')
    search_fields = ('key', 'title_ru', 'title_uz', 'title_en')

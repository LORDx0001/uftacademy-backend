from django.db import models

class Header(models.Model):
    logo = models.ImageField(upload_to="header/", verbose_name="Логотип")

    title_uz = models.CharField(max_length=255, verbose_name="Заголовок (UZ)")
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Заголовок (EN)")

    description_uz = models.TextField(verbose_name="Описание (UZ)")
    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_en = models.TextField(verbose_name="Описание (EN)")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title_uz

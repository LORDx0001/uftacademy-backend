from django.db import models

class Titles(models.Model):
    
    key = models.CharField(max_length=200, verbose_name="keys")
    title_uz = models.CharField(max_length=255, verbose_name="Заголовок (UZ)")
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Заголовок (EN)")
    
    def __str__(self):
        return self.title_uz

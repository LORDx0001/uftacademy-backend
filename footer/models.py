from django.db import models


class Footer(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    logo = models.ImageField(upload_to="footer/")

    link_facebook = models.URLField(blank=True, null=True)
    link_instagram = models.URLField(blank=True, null=True)
    link_telegram = models.URLField(blank=True, null=True)
    link_youtube = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en

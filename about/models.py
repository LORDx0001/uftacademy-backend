from django.db import models


class About(models.Model):
    # Title
    title_uz = models.CharField(max_length=255, verbose_name="Title (Uzbek)")
    title_ru = models.CharField(max_length=255, verbose_name="Title (Russian)")
    title_en = models.CharField(max_length=255, verbose_name="Title (English)")

    # Description
    description_uz = models.TextField(verbose_name="Description (Uzbek)")
    description_ru = models.TextField(verbose_name="Description (Russian)")
    description_en = models.TextField(verbose_name="Description (English)")

    # Image
    image = models.ImageField(upload_to="about/", verbose_name="Image")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title_uz

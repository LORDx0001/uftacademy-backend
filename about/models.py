from django.db import models


class About(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title_uz

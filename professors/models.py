from django.db import models


class Professor(models.Model):
    full_name = models.CharField(max_length=255)
    position_uz = models.CharField(max_length=255)
    position_ru = models.CharField(max_length=255)
    position_en = models.CharField(max_length=255)

    bio_uz = models.TextField()
    bio_ru = models.TextField()
    bio_en = models.TextField()

    image = models.ImageField(upload_to="professors/")

    def __str__(self):
        return self.full_name

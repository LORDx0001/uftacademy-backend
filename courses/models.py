from django.db import models


class Course(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    duration = models.CharField(max_length=100)  # masalan: "3 oy"

    image = models.ImageField(upload_to="courses/")

    def __str__(self):
        return self.title_uz

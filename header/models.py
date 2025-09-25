from django.db import models

class Header(models.Model):
    logo = models.ImageField(upload_to="header/")
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    # navbar tugmalari
    nav_about_uz = models.CharField(max_length=100)
    nav_about_ru = models.CharField(max_length=100)
    nav_about_en = models.CharField(max_length=100)

    nav_courses_uz = models.CharField(max_length=100)
    nav_courses_ru = models.CharField(max_length=100)
    nav_courses_en = models.CharField(max_length=100)

    nav_professors_uz = models.CharField(max_length=100)
    nav_professors_ru = models.CharField(max_length=100)
    nav_professors_en = models.CharField(max_length=100)

    nav_portfolio_uz = models.CharField(max_length=100)
    nav_portfolio_ru = models.CharField(max_length=100)
    nav_portfolio_en = models.CharField(max_length=100)

    nav_contact_uz = models.CharField(max_length=100)
    nav_contact_ru = models.CharField(max_length=100)
    nav_contact_en = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz

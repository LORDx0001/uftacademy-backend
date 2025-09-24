from django.db import models

class Course(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    duration = models.CharField(max_length=50)
    image = models.URLField()


class Teacher(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    bio_uz = models.TextField()
    bio_ru = models.TextField()
    bio_en = models.TextField()

    avatar = models.URLField()
    skills = models.JSONField()


class PortfolioItem(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    image = models.URLField()
    category = models.CharField(max_length=50)


class InfoBlock(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    icon = models.CharField(max_length=50)

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)         
    url = models.URLField()                        
    icon_url = models.URLField()                   
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.name
    
class SectionTitle(models.Model):
    key = models.CharField(max_length=50, unique=True) 
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.key} → {self.title_ru}"

from django.db import models

# Create your models here.
class Album(models.Model):
    content = models.TextField(max_length=20)
    image = models.ImageField(blank=True)
from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=30)
    image_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
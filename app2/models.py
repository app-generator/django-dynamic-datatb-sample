from django.db import models

# Create your models here.

class City(models.Model):

    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100, default='')
    visited = models.CharField(max_length=100, default='false')
    
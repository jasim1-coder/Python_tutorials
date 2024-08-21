from django.db import models

# Create your models here.

class movie_info(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    summary = models.TextField()

class director(models.Model):
    name = models.CharField(max_length=250)
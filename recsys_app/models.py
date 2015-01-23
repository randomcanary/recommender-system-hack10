from django.db import models

# Create your models here.

class Case(models.Model):
    client = models.CharField(max_length=200)
    typeoflaw = models.CharField(max_length=200)
    lawyer = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    

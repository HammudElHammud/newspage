from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Cont(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    website= models.CharField(max_length=100)






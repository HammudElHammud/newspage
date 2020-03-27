from __future__ import unicode_literals
from django.db import models

# Create your models here.
class subCategory(models.Model):
    name = models.CharField(max_length=15)
    categoryName = models.CharField(max_length=15)
    categoryId = models.IntegerField()


    def __str__(self):
        return self.name

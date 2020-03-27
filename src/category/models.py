from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    count  = models.IntegerField(default=0)

    def __str__(self):
        return self.name

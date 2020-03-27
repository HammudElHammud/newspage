
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=50)
    short_txt  = models.CharField(max_length=40)
    date  = models.DateField()
    newBody  = RichTextField(max_length=200)
    picName = models.CharField(max_length=5000)
    picUrl = models.CharField(max_length=5000)
    writer = models.CharField(max_length=20)
    newCategory = models.IntegerField()
    newShow = models.IntegerField()
    catId= models.CharField(max_length=50,default=1)
    OcatId= models.CharField(max_length=50)
    tag = models.TextField(default='')



    name_set = models.CharField(max_length=20,default='-')
    def __str__(self):
        return self.name_set

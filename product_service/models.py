from django.db import models

# Create your models here.


class Product(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=255)
    SLUG = models.SlugField(max_length=255)
    ICON = models.ImageField(upload_to='uploads/products/%Y/%m/%d/')
    SHORT_DESCRIPTION = models.TextField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)


class SERVICE(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=255)
    SLUG = models.SlugField(max_length=255)
    ICON = models.ImageField(upload_to='uploads/services/%Y/%m/%d/')
    IMAGE = models.ImageField(upload_to='uploads/services/%Y/%m/%d/')
    SHORT_DESCRIPTION = models.TextField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)

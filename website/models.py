from django.db import models
from multiselectfield import MultiSelectField
import os

# Create your models here.


def get_upload_path(instance, filename):
    return os.path.join('uploads', instance.Banner, filename)


class BannerImage(models.Model):
    BANNER_TYPE = [
        ('About_Us_Banner', 'About_Us_Banner'),
        ('Carrer_Details_Banner', 'Carrer_Details_Banner'),
        ('Carrer_list_Baner', 'Carrer_list_Baner'),
        ('Home_Banner', 'Home_Banner'),
        ('Services_Banner', 'Services_Banner'),
    ]

    ID = models.AutoField(primary_key=True)
    Banner = models.CharField(max_length=60, choices=BANNER_TYPE)
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Image = models.ImageField(upload_to=get_upload_path)

    def __str__(self) -> str:
        return self.Banner


class ContactForm(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=100)
    Subject = models.CharField(max_length=255)
    Message = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Name


class ContactInfo(models.Model):
    Email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    Latitude_Logitude = models.CharField(
        max_length=50, help_text="Right click on the google maps to get latitude and longitude")
    Facebook_link = models.URLField(default="www.facebook.com")
    Instagram_link = models.URLField(default="www.instagram.com")
    X_link = models.URLField(default="www.twitter.com")
    Youtube_link = models.URLField(default="www.youtube.com")
    Linkedin_link = models.URLField(default="www.linkedin.com")
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Email


class PageContent(models.Model):
    Page_type = [
        ('About_Us', 'About_Us'),
        ('Home', 'Home'),
        ('Carrers', 'Carrers'),
        ('Services', 'Services'),
    ]
    Page_Type = models.CharField(max_length=60, choices=Page_type)
    Page_Title = models.CharField(max_length=255)
    Page_Content = models.TextField()
    image = models.ImageField(upload_to='uploads/pages/%Y/%m/%d/')
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Page_Type

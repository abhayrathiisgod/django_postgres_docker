from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import os
# Create your models here.


class Job(models.Model):
    job_TYPE = [
        ('FULL_TIME', 'FULL_TIME'),
        ('REMOTE', 'REMOTE'),
        ('HYBRID', 'HYBRID'),
        ('PARTIME', 'PARTIME'),
    ]
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Job_Type = models.CharField(max_length=255, choices=job_TYPE)
    About_Role = CKEditor5Field(default="")
    Job_Requirement = CKEditor5Field(default="")
    Open_date = models.DateField()
    Close_date = models.DateField()
    is_published = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title


def get_upload_path(instance, filename):
    return os.path.join('uploads', instance.Position.Job_name, filename)


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=100, default="123")
    Position = models.ForeignKey(Job, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    CV = models.FileField(upload_to=get_upload_path)

    def __str__(self) -> str:
        return self.Name

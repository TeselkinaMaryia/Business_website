from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    information = models.TextField()
    photo = models.FileField(upload_to='img/')


class Directors(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    joined_company = models.IntegerField()
    information = models.TextField()
    photo = models.FileField(upload_to='img/')

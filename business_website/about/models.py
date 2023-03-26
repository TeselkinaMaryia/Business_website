from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    information = models.TextField()
    photo = models.FileField(upload_to='employees/')


class SeniorEmployees(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    information = models.TextField()
    photo = models.FileField(upload_to='senior_employees/')


class Cantact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

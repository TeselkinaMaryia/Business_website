from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80)
    image = models.FileField(upload_to='ask/')

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    auther = models.CharField(max_length=50)
    department = models.CharField(max_length=50, blank=True, null=True)
    date_of_create = models.DateField(auto_now_add=True)
    your_question = models.TextField()

    def __str__(self):
        return self.your_question


class Comments(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    your_comment = models.TextField()

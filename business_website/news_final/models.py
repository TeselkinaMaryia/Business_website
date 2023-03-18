from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.FileField(upload_to='news/')
    date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date']


class Conference(models.Model):
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=30)
    categories = models.ManyToManyField('Category', related_name='conferences')
    topic = models.CharField(max_length=30)
    about = models.TextField()
    number_of_people = models.IntegerField()


class Registration(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()
    number_of_people = models.IntegerField()
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE)

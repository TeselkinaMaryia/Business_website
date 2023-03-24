from django.db import models


class Vacancies(models.Model):
    name = models.CharField(max_length=100)
    responsibilities = models.TextField()
    income = models.CharField(max_length=100)
    opportunity_to_work_from_home = models.CharField(max_length=50)
    timetable = models.CharField(max_length=100)
    additional_requirements = models.TextField()

    def __str__(self):
        return self.name


class Apply(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    working_position = models.ForeignKey('Vacancies', on_delete=models.CASCADE)
    short_summary = models.TextField()
    work_in_the_office = models.CharField(max_length=50, blank=True)
    online_work = models.CharField(max_length=50, blank=True)
    individual_feature = models.TextField(blank=True)


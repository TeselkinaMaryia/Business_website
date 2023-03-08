from django.shortcuts import render
from . import models


def about_main(request):
    return render(request, 'about_main.html')


def about_history(request):
    return render(request, 'about_history.html')


def about_leadership(request):
    employees = models.Employees.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'about_leadership.html', context)


def employees_more(request, pk):
    employee = models.Employees.objects.get(pk=pk)
    context = {
        'employee': employee
    }
    return render(request, 'about_leadership_employee.html', context)

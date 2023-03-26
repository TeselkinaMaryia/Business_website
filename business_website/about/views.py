from django.shortcuts import render
from . import models
from . import forms


def about_main(request):
    return render(request, 'about_main.html')


def about_history(request):
    return render(request, 'about_history.html')


def about_leadership(request):
    employees = models.Employees.objects.all()
    senior_employees = models.SeniorEmployees.objects.all()
    context = {
        'employees': employees,
        'senior_employees': senior_employees
    }
    return render(request, 'about_leadership.html', context)


def employees_more(request, pk):
    employee = models.Employees.objects.get(pk=pk)
    context = {
        'employee': employee
    }
    return render(request, 'about_leadership_employee.html', context)


def senior_employees_more(request, pk):
    senior_employee = models.SeniorEmployees.objects.get(pk=pk)
    context = {
        'senior_employee': senior_employee
    }
    return render(request, 'about_leadership_senior_employee.html', context)


def contacts(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            contact_us = models.Cantact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            contact_us.save()
    context = {
        'form': form,
    }
    return render(request, 'about_contacts.html', context)

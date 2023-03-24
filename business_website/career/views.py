from django.shortcuts import render
from . import models
from . import forms


def career_main(request):
    return render(request, 'career/career_main.html')


def vacancies(request):
    all_vacancies = models.Vacancies.objects.all().order_by('income')
    context = {
        'all_vacancies': all_vacancies
    }
    return render(request, 'career/career_vacancies.html', context)


def apply(request):
    form = forms.ApplyForm()
    if request.method == 'POST':
        form = forms.ApplyForm(request.POST)
        if form.is_valid():
            statement = models.Apply(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                working_position=form.cleaned_data['working_position'],
                short_summary=form.cleaned_data['short_summary'],
                work_in_the_office=form.cleaned_data['work_in_the_office'],
                online_work=form.cleaned_data['online_work'],
                individual_feature=form.cleaned_data['individual_feature']
            )
            statement.save()
    context = {
        'form': form,
    }
    return render(request, 'career/career_apply.html', context)


def vacancy_more(request, pk):
    vacancy = models.Vacancies.objects.get(pk=pk)
    context = {
        'vacancy': vacancy
    }
    return render(request, 'career/vacancy_more.html', context)

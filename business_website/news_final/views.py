from django.shortcuts import render
from . import models
from . import forms


def news_main(request):
    news = models.News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news_main.html', context)


def news_more(request, pk):
    one_news = models.News.objects.get(pk=pk)
    context = {
        'one_news': one_news
    }
    return render(request, 'news_more.html', context)


def news_events(request):
    conferences = models.Conference.objects.all().order_by('-date')
    context = {
        'conferences': conferences
    }
    return render(request, 'news_events.html', context)


def events_category(request, category):
    conferences = models.Conference.objects.filter(categories__name__contains=category).order_by('-date')
    context = {
        'category': category,
        'conferences': conferences
    }
    return render(request, 'events_category.html', context)


def events_more(request, pk):
    conference = models.Conference.objects.get(pk=pk)
    # form = forms.RegistrationForm()
    #
    # if request.method == 'POST':
    #     form = forms.RegistrationForm(request.POST)
    #     if form.is_valid():
    #         registration = models.Registration(
    #             name=form.cleaned_data['name'],
    #             second_name=form.cleaned_data['second_name'],
    #             email=form.cleaned_data['email'],
    #             number_of_people=form.cleaned_data['number_of_people'],
    #             conference=conference
    #         )
    #         registration.save()
    # registrations = models.Registration.objects.filter(conference=conference)
    #
    # context = {
    #     'conference': conference,
    #     'registrations': registrations,
    #     'form': form
    # }
    # return render(request, 'events_more.html', context)

    if models.Registration.objects.all():
        get_places = []
        reg_seats = models.Registration.objects.all()
        for people in reg_seats:
            get_places.append(people.number_of_people)
        free_places = conference.number_of_people - sum(get_places)
        form = forms.RegistrationForm()
        if free_places > 0:
            if request.method == 'POST':
                form = forms.RegistrationForm(request.POST)
                if form.is_valid():
                    registration = models.Registration(
                        name=form.cleaned_data['name'],
                        second_name=form.cleaned_data['second_name'],
                        email=form.cleaned_data['email'],
                        number_of_people=form.cleaned_data['number_of_people'],
                        conference=conference
                    )
                    registration.save()
        registrations = models.Registration.objects.filter(conference=conference)

        context = {
            'conference': conference,
            'registrations': registrations,
            'free_places': free_places,
            'form': form
        }
        return render(request, 'events_more.html', context)
    else:
        free_places = conference.number_of_people
        form = forms.RegistrationForm()
        if free_places > 0:
            if request.method == 'POST':
                form = forms.RegistrationForm(request.POST)
                if form.is_valid():
                    registration = models.Registration(
                        name=form.cleaned_data['name'],
                        second_name=form.cleaned_data['second_name'],
                        email=form.cleaned_data['email'],
                        number_of_people=form.cleaned_data['number_of_people'],
                        conference=conference
                    )
                    registration.save()
        registrations = models.Registration.objects.filter(conference=conference)

        context = {
            'conference': conference,
            'registrations': registrations,
            'free_places': free_places,
            'form': form
        }
        return render(request, 'events_more.html', context)

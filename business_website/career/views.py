from django.shortcuts import render


def career_main(request):
    return render(request, 'career/career_main.html')

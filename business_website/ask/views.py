from django.shortcuts import render


def ask_main(request):
    return render(request, 'ask_main.html')

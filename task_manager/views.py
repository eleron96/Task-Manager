from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def home(request):
    return render(request, 'home.html', context={
        'who': 'World',
    })

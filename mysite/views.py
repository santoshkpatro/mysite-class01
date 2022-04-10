from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return HttpResponse('<h1>Contact Us Page is lit</h1>')


def about_us(request):
    return render(request, 'about.html')
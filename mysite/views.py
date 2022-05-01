from django.shortcuts import HttpResponse, render


def index(request):
    # Processing
    data = {
        'name': 'Jeet',
        'age': 18,
        'scores': [20, 34, 56, 77]
    }
    return render(request, 'index.html', context=data)


def contact_us(request):
    return render(request, 'contact.html')


def about_us(request):
    return render(request, 'about.html')
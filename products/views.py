from django.shortcuts import render, HttpResponse

# Create your views here.
def product_list(request):
    return HttpResponse('Product List')


def product_detail(request, product_id):
    print(product_id)
    return HttpResponse('Product Detail')
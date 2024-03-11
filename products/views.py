from django.http import HttpResponse
from django.shortcuts import render
from . models import Product

# /products -> index function


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')




#    Product.objects.all()
#    Products.objecs.filter()
#    Product.objects.get()
#    Products.objecs.save()
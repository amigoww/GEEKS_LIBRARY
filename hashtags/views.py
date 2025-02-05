from django.shortcuts import render
from .models import Tag, Product


def all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'all_products.html', {'products': products})


def male_products(request):
    if request.method == 'GET':
        products = Product.objects.filter(tag__name='Male')
        return render(request, 'products.html', {'products': products})


def female_products(request):
    if request.method == 'GET':
        products = Product.objects.filter(tag__name='Female')
        return render(request, 'products.html', {'products': products})



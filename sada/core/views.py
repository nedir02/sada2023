from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from core.models import Product, Category


def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {
        'product': product,
        'category': category
    }
    return render(request, 'index.html', {'product': product})


def about_us(request):
    return render(request, 'about_us.html')


def history(request):
    return render(request, 'history.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def product(request):
    return render(request, 'products.html')

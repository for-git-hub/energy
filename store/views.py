from django.shortcuts import render
from .models import Product
from category import models
from category.models import Category


def store(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)

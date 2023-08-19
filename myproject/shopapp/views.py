from datetime import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import Group
from shopapp.models import Product, Order


def shop_index(request: HttpRequest) -> HttpResponse:
    products = [
        ('Laptop', 2000),
        ('Smartphone', 3000),
        ('Notebook', 5000),
    ]
    context = {
        'time_now': datetime.now(),
        'products': products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)

def groups_list(request):
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'shopapp/groups-list.html', context=context)

def products_list(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shopapp/products-list.html', context=context)

def order_list(request):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(request, 'shopapp/order-list.html', context=context)
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ListProducts(ListView):
    model = Product
    template_name = 'products/list_products.html'
    context_object_name = 'products'


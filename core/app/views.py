from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class EventListView(ListView):
    model = Product
    template_name = 'app/about-us.html'
    context_object_name = 'object_list'


def view_cart(request):
    return render(request, 'app/cart.html')


def view_checkout(request):
    return render(request, 'app/checkout.html')


def view_contact(request):
    return render(request, 'app/contact.html')


def view_shop(request):
    return render(request, 'app/shop.html')
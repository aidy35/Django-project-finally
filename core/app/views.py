from django.shortcuts import render


def view_index(request):
    return render(request, 'app/about-us.html')


def view_cart(request):
    return render(request, 'app/cart.html')


def view_checkout(request):
    return render(request, 'app/checkout.html')


def view_contact(request):
    return render(request, 'app/contact.html')


def view_shop(request):
    return render(request, 'app/shop.html')



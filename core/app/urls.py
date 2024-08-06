from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', view_index, name='home'),
    path('cart/', view_cart, name='cart'),
    path('list_objects/', view_shop, name='list')

]
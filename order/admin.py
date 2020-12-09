from django.contrib import admin
from .models import ShopCartItem, ShopCart

admin.site.register(ShopCart)
admin.site.register(ShopCartItem)

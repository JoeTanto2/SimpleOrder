from django.contrib import admin
from .models import Order, Toppings, Item

admin.site.register(Order)
admin.site.register(Toppings)
admin.site.register(Item)
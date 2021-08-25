from django.urls import path
from .views import all_orders, add_item, item_not_in_stock, add_topping, close_day
urlpatterns = [
    path ('orders/', all_orders),
    path ('add-item/', add_item),
    path ('add-topping/', add_topping),
    path ('out-of-stock/', item_not_in_stock),
    path ('closing/', close_day),
]

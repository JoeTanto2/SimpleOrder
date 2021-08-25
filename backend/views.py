from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Order, Toppings, ItemManager, ToppingsManager,Item
from .serializer import OrderSerializer
from djongo import models
from django.db.models import F, Func
@api_view(['GET'])
def all_orders (request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response({'data': serializer.data})

@api_view(['POST'])
def add_item (request):
    info = request.data['data']
    print(info)
    item_object = ItemManager.add_item(ItemManager(), info['item'], info['price'])
    return Response(item_object)

@api_view(['POST', 'GET'])
def item_not_in_stock (request):
    if request.method == 'GET':
        list = []
        items = Item.objects.all()
        for item in items:
            if item.in_stock != False:
                to_send = {}
                to_send['id'] = item.id
                to_send['item'] = item.item
                list.append(to_send)
        return Response(list)
    info = request.data['data']
    item = ItemManager.out_of_stock(ItemManager(), info['id'])
    return Response(item)

@api_view(['POST'])
def add_topping (request):
    info = request.data
    topping_object = ToppingsManager.add_topping(ToppingsManager(), info['topping'], info['price'])
    return Response(topping_object)


@api_view(['GET'])
def close_day (request):
    grand_total = 0
    todays_orders = Order.objects.filter(closed=1)
    total_toppings = todays_orders.aggregate(toppings=models.Sum('toppings__price'))
    total_items = todays_orders.aggregate(items=models.Sum('items__price'))
    grand_total = total_toppings['toppings'] + total_items['items']
    amount_of_orders = todays_orders.count()
    todays_orders.update(closed=0)
    return Response({'GrandTotal': grand_total, 'orders': amount_of_orders})

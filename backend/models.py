from djongo import models
# from djangotoolbox.fields import

from django.contrib.auth.models import User

class ToppingsManager (models.Manager):
    def add_topping (self, topping: str, price: float):
        topping = Toppings.objects.create(topping=topping, price=price)
        if topping:
            return f'Topping {topping.topping} at a price of {topping.price} has been succesfully added'

    def out_of_stock (self, topping: str):
        topping = Toppings.objects.filter(topping=topping)
        if topping.exists():
            topping.update(in_stock=False)
            return f'topping {topping[0].topping} with id of {self.id} is now out of stock'
        return f'Topping {topping} does not exist'

    def in_stock (self, topping:str):
        topping = Toppings.objects.filter(topping=topping)
        if topping.exists():
            topping.update(in_stock=True)
            return f'topping {topping[0].topping} with id of {self.id} is now in stock'
        return f'Topping {topping} does not exist'

class Toppings (models.Model):
    topping = models.CharField(max_length=30)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)

    def __str__ (self):
        return self.topping

class ItemManager (models.Manager):
    def add_item(self, item: str, price: float):
        item = Item.objects.create(item=item, price=price)
        if item:
            return f'Item {item.item} at a price {item.price} has been successfully added.'
        return 'something went wrong, please try again'

    def out_of_stock (self, id: int):
        item = Item.objects.filter(id=id)
        if not item:
            return f'something went worng'
        item.update(in_stock=False)
        return f'{item[0].item} with id of {id} is now out of stock'

class Item (models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return f'{self.item}, id {self.id}'


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
    toppings = models.ManyToManyField(to=Toppings)
    items = models.ManyToManyField(to=Item)
    is_delivery = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    address = models.TextField(null=True)
    status = models.CharField(max_length=100, default=None)
    closed = models.IntegerField(default=1)
    def __str__ (self):
        return str(self.id)









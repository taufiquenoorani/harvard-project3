from django.db import models
from django.contrib.auth.models import User
from stock.models import Pizza, Topping, PizzaType, Sub, Pasta, Salad, DinnerPlatter

class OrderStatus(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

#cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    price = models.FloatField(default = 0.0)

class Cartpizza(models.Model):
    Carts = models.ForeignKey(Cart, on_delete = models.CASCADE)
    pizzas = models.ForeignKey(Pizza, on_delete = models.CASCADE)

class CartTopping(models.Model):
    Carts = models.ForeignKey(Cart, on_delete = models.CASCADE)
    Toppings = models.ForeignKey(Topping, on_delete = models.CASCADE)

class CartSub(models.Model):
    Carts = models.ForeignKey(Cart, on_delete = models.CASCADE)
    Subs = models.ForeignKey(Sub, on_delete = models.CASCADE)

class CartPasta(models.Model):
    Carts = models.ForeignKey(Cart, on_delete = models.CASCADE)
    Pastas = models.ForeignKey(Pasta, on_delete = models.CASCADE)

class CartSalad(models.Model):
    Carts = models.ForeignKey(Cart, on_delete = models.CASCADE)
    Salads = models.ForeignKey(Salad, on_delete = models.CASCADE)

class CartDinnerPlatter(models.Model):
    Carts = models.ForeignKey(Cart, on_delete = models.CASCADE)
    DinnerPlatters = models.ForeignKey(DinnerPlatter, on_delete = models.CASCADE)


#confirmed orders
class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    price = models.FloatField(default = 0.0)
    OrderStatus = models.ForeignKey(OrderStatus, on_delete = models.CASCADE)

class Orderpizza(models.Model):
    Orders = models.ForeignKey(Order, on_delete = models.CASCADE)
    pizzas = models.ForeignKey(Pizza, on_delete = models.CASCADE)

class OrderTopping(models.Model):
    Orders = models.ForeignKey(Order, on_delete = models.CASCADE)
    Toppings = models.ForeignKey(Topping, on_delete = models.CASCADE)

class OrderSub(models.Model):
    Orders = models.ForeignKey(Order, on_delete = models.CASCADE)
    Subs = models.ForeignKey(Sub, on_delete = models.CASCADE)

class OrderPasta(models.Model):
    Orders = models.ForeignKey(Order, on_delete = models.CASCADE)
    Pastas = models.ForeignKey(Pasta, on_delete = models.CASCADE)

class OrderSalad(models.Model):
    Orders = models.ForeignKey(Order, on_delete = models.CASCADE)
    Salads = models.ForeignKey(Salad, on_delete = models.CASCADE)

class OrderDinnerPlatter(models.Model):
    Orders = models.ForeignKey(Order, on_delete = models.CASCADE)
    DinnerPlatters = models.ForeignKey(DinnerPlatter, on_delete = models.CASCADE)
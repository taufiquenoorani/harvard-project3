from django.shortcuts import render, redirect, HttpResponse
from .models import *

def ordering(request):
    #if user is authenticated
    if request.user.is_authenticated:
        items = request.POST.get('item')
        types = request.POST.get('type')
        #cart object initiate
        cart_obj, new = Cart.objects.update_or_create(
            user = request.user,
        )
        total = cart_obj.price
        if types == "Pizza":
            pizza_obj = Cartpizza.objects.create(
                Carts = cart_obj,
                pizzas_id = items
            )
            total = total + pizza_obj.pizzas.price
        elif types == "Toppings":
            topping_obj = CartTopping.objects.create(
                Carts = cart_obj,
                Toppings_id = items
                
            )
            total = total + topping_obj.Toppings.price
        elif types == "Subs":
            sub_obj = CartSub.objects.create(
                Carts = cart_obj,
                Subs_id = items
            )
            total = total + sub_obj.Subs.price
        elif types == "Pasta":
            pasta_obj = CartPasta.objects.create(
                Carts = cart_obj,
                Pastas_id = items
            )
            total = total + pasta_obj.Pastas.price
        elif types == "Salads":
            salad_obj = CartSalad.objects.create(
                Carts = cart_obj,
                Salads_id = items
            )
            total = total + salad_obj.Salads.price
        elif types == "Dinner":
            dinner_obj = CartDinnerPlatter.objects.create(
                Carts = cart_obj,
                DinnerPlatters_id = items
            )
            total = total + dinner_obj.DinnerPlatters.price
        cart_obj.price = total
        cart_obj.save()
        return HttpResponse()
        
    #if not logged in redirect to login page
    else:
        return redirect('/accounts/login/')

def cartitem(request):
    #if user is authenticated
    if request.user.is_authenticated:
        #get users cart details
        try:
            cart_obj = Cart.objects.get(
                user = request.user,
            )
        except:
            return redirect('index')
        pizza_obj = Cartpizza.objects.filter(
            Carts = cart_obj
        )
        
        topping_obj = CartTopping.objects.filter(
            Carts = cart_obj
            
        )
        sub_obj = CartSub.objects.filter(
            Carts = cart_obj
        )
        pasta_obj = CartPasta.objects.filter(
            Carts = cart_obj
        )
        salad_obj = CartSalad.objects.filter(
            Carts = cart_obj
        )
        dinner_obj = CartDinnerPlatter.objects.filter(
            Carts = cart_obj
        )
        if request.method == 'GET':
            datas = {
                "cart": cart_obj,
                "price_cent": float(cart_obj.price) * 100,
                "pizza" : pizza_obj,
                "topping": topping_obj,
                "sub": sub_obj,
                "pasta" : pasta_obj,
                "salad" : salad_obj,
                "dinner": dinner_obj,
            }
            return render(request, 'cart/view.html', datas)
        elif request.method == 'POST':
            #confirm = request.POST.get('confirm')
            #if int(confirm) is 1:
            order_obj = Order.objects.create(
                user = request.user,
                OrderStatus_id = 1
            )
            for a in pizza_obj:
                #create pizza in order
                pizza_obj = Orderpizza.objects.create(
                    Orders = order_obj,
                    pizzas = a.pizzas
                )
            for a in topping_obj:
                topping_obj = OrderTopping.objects.create(
                    Orders = order_obj,
                    Toppings = a.Toppings
                )
            for a in sub_obj:
                sub_obj = OrderSub.objects.create(
                    Orders = order_obj,
                    Subs = a.Subs
                )
            for a in pasta_obj:
                pasta_obj = OrderPasta.objects.create(
                    Orders = order_obj,
                    Pastas = a.Pastas
                )
            for a in salad_obj:
                salad_obj = OrderSalad.objects.create(
                    Orders = order_obj,
                    Salads = a.Salads
                )
            for a in dinner_obj:
                dinner_obj = OrderDinnerPlatter.objects.create(
                    Orders = order_obj,
                    DinnerPlatters = a.DinnerPlatters
                )
            cart_obj.delete()
            return redirect('index')


    #if not logged in redirect to login page
    else:
        return redirect('/accounts/login/')


def orderlist(request):
    #if user is authenticated
    if request.user.is_authenticated:
        if request.user.is_superuser is True:
            if request.method == 'GET':
                order_obj = Order.objects.all()
                datas = {
                    "order": order_obj
                }
                return render(request, 'order/orderlist.html', datas)
            elif request.method == 'POST':
                orderid = request.POST.get('OrderId')
                confirm = request.POST.get('confirm')
                print(orderid)
                #get order object
                order_obj = Order.objects.get(id = orderid)
                if int(confirm) is 1:
                    order_obj.OrderStatus_id = 2
                    order_obj.save()
                elif int(confirm) is 0:
                    order_obj.OrderStatus_id = 3
                    order_obj.save()
                order_obj = Order.objects.all()
                datas = {
                    "order": order_obj
                }
                return render(request, 'order/orderlist.html', datas)
        else:
            return redirect('index')
    #if not logged in redirect to login page
    else:
        return redirect('/accounts/login/')

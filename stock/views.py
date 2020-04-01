from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Pizza, Topping, PizzaType, Sub, Pasta, Salad, DinnerPlatter

def LogoutView(request):
    logout(request)
    return redirect('/')

def AllFoodList(request):
    #if user is authenticated
    if request.user.is_authenticated:
        #get all pizza type
        pizza_type = PizzaType.objects.all()
        #get all pizza list
        pizza_list = Pizza.objects.all()
        #get all toppings
        topping_list = Topping.objects.all()
        #get all subs
        sub_list = Sub.objects.all()
        #get all pasta
        pasta_list = Pasta.objects.all()
        #get all salads
        salad_list = Salad.objects.all()
        #get all Dinner Platters
        diner_plattter_list = DinnerPlatter.objects.all()

        datas = {
            "pizza_type" : pizza_type,
            "pizza" : pizza_list,
            "topping" : topping_list,
            "sub": sub_list,
            "pasta": pasta_list,
            "salad": salad_list,
            "dinner": diner_plattter_list,
        }
        return render(request, 'stock/index.html', datas)
    #if not logged in redirect to login page
    else:
        return redirect('/accounts/login/')
        #create signup page#######################
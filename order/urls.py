from django.urls import path
from .views import ordering, cartitem, orderlist

urlpatterns = [
    path('ordering', ordering, name = "ordering"),
    path('cartitem', cartitem, name = 'cart'),
    path('orderlist', orderlist, name = 'orderlist'),
]
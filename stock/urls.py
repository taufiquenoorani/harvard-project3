from django.urls import path
from .views import *

urlpatterns = [
    path('', AllFoodList, name = "index"),
    path('logout', LogoutView, name = "logout"),
]
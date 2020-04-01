from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    #user app's urls
    path('',include('stock.urls')),
    path('users/',include('users.urls')),
    path('order/',include('order.urls')),
]

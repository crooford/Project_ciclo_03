from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login', views.login, name='login'),
    path('admon.html', views.admon, name='admon'),
    path('admon-waiter', views.waiter, name='waiter'),
]

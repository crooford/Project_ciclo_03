from django.urls import path
from . import views

urlpatterns = [
    path('', views.admon, name='admon'),
    path('admon-waiter.html', views.waiter, name='waiter'),
    path('admon-menu.html', views.menu, name='menu'),
    path('admon-waiter-data.html', views.waiterData, name='waiterData'),
]

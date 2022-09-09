from django.urls import path
from . import views

urlpatterns = [
    path('admon.html', views.admon, name='admon'),
    path('admon-waiter.html', views.waiter, name='waiter'),
    path('admon-menu.html', views.menu, name='menu'),
    path('admon-waiter-data.html', views.waiterData, name='waiterData'),
]

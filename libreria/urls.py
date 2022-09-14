from django.urls import path
from . import views

urlpatterns = [
    path('admon.html', views.admon, name='admon'),
    path('admon-waiter.html', views.waiter, name='waiter'),
    path('admon-menu.html', views.menu, name='menu'),
    path('admon-waiter-data.html', views.waiterData, name='waiterData'),    
    path('mesero-mesas.html', views.meseroMesas, name='meseroMesas'),
    path('mesero-orden.html', views.meseroOrden, name='meseroOrden'),
    path('registro.html', views.registro, name='registro'),
]

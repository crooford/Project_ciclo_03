
from django.urls import path
from . import views

urlpatterns = [
   path('', views.ppal, name='ppal'),
   path('ppal.html', views.ppal, name='ppal'),
   path('registro.html', views.registro, name='registro'),  
   path('usuarios.html', views.usuarios, name='usuarios'), 
   path('mesero-mesas.html', views.mesero_mesas, name='mesero-mesas'), 
   path('mesero-orden.html', views.mesero_orden, name='mesero-orden'), 
   
]

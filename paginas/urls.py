
from django.urls import path
from . import views
from .views import listUsuario

urlpatterns = [
   path('', views.ppal, name='ppal'),
   path('ppal.html', views.ppal, name='ppal'),
   path('registro.html', views.registro, name='registro'),  
   path('usuarios.html', views.usuarios, name='usuarios'),
   path('menu.html', views.menu, name='menu'),
   path('crear-plato.html', views.crear_plato, name='crear-plato'),
   path('editar-plato/<int:id>/', views.editar_plato, name='editar'), 
   path('eliminar-plato/<int:id>/', views.eliminar_plato, name='eliminar'),
   path('usuarios.html', listUsuario.as_view(), name='usuarios'),
   path('mesero-mesas.html', views.mesero_mesas, name='mesero_mesas'),
   path('mesero-orden.html', views.mesero_orden, name='mesero_orden'),
]


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
   path('mesero-orden/<int:id>/', views.mesero_orden, name='editar-plato'),
   path('cocinero-comandas-list.html', views.cocinero_list, name='cocinero_list'),
   path('cocinero-comandas-mesa.html', views.cocinero_mesa, name='cocinero_mesa'),
   path('cocinero-comandas-todas.html', views.cocinero_todas, name='cocinero_todas'),
   path('vaciar/<int:id>/', views.vaciar_orden, name='vaciar'),
]

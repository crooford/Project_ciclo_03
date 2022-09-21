
from django.urls import path
from . import views
from paginas.views import listUsuario

urlpatterns = [
   path('', views.ppal, name='ppal'),
   path('ppal.html', views.ppal, name='ppal'),
   path('registro.html', views.registro, name='registro'),  
   path('usuarios.html', views.usuarios, name='usuarios'),
   path('menu.html', views.menu, name='menu'),
   path('crear-plato.html', views.crear_plato, name='crear-plato'),
   path('editar-contacto/<int:id>/', views.editar_plato, name='editar-plato'), 
   path('eliminar-contacto/<int:id>/', views.eliminar_plato, name='eliminar-plato'),
<<<<<<< HEAD
   path('usuarios.html', listUsuario.as_view(), name='usuarios'),
=======
   
>>>>>>> c0fd2b7e4be0aa1199940777968057d9748e57c9
]

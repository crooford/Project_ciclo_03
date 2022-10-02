
from django.urls import path
from . import views


urlpatterns = [
   path('', views.ppal, name='ppal'),
   path('ppal', views.ppal, name='ppal'),
   path('menu', views.menu, name='menu'),
   path('crear-plato', views.crear_plato, name='crear-plato'),
   path('editar-plato/<int:id>/', views.editar_plato, name='editar'), 
   path('eliminar-plato/<int:id>/', views.eliminar_plato, name='eliminar'),
   path('mesas', views.mesero_mesas, name='mesero_mesas'),
   path('mesas-editar-plato/<int:id>/', views.mesero_orden, name='editar-plato'),
   path('cocina', views.cocinero_todas, name='cocinero_todas'),
   path('vaciar-orden/<int:id>/', views.vaciar_orden, name='vaciar'),
   path('eliminar-itemorden/<int:id>/', views.eliminar_itemorden, name='eliminar-itemorden'),
]

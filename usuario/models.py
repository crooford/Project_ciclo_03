from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Cargo = models.CharField (
        max_length=10,
        choices=[('Cocinero', 'Cocinero'), ('Mesero', 'Mesero')]                                           
    )
    
    Rol = models.CharField (
        max_length=12,
        choices=[('Cocina1', 'Cocina1'), ('Cocina2', 'Cocina2'), ('Cocina3', 'Cocina3'), ('Bebidas1', 'Bebidas1'), ('Bebidas2', 'Bebidas2')]                                             
    )
    
    def __str__(self):
        return self.user.username

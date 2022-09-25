from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Menu(models.Model):  
    id = models.AutoField(primary_key=True)
    nombre_plato= models.CharField(max_length=155, blank=False, null=False)
    precio= models.FloatField(null=False, blank=False)
    descripcion= models.TextField(max_length=255, blank=True, null=True)
    tipo_plato= models.CharField (
        max_length=50,
        choices=[('Entrada', 'Entrada'), ('Plato Principal', 'Plato Principal'), ('Postre', 'Postre'), ('Bebida', 'Bebida'), ('Otro', 'Otro')]                                             
    )

    def __str__(self):
        mostrar= self.nombre_plato
        return mostrar
    

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

class Mesas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_mesa = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nombre_mesa

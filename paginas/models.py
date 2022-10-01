from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#------------------------------------- menu ---------------------------------------------------------------
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
    
#-------------------------------------cargo usuarios---------------------------------------------------------------
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    Cargo = models.CharField (
        max_length=13,
        choices=[('Administrador', 'Administrador'), ('Cocinero', 'Cocinero'), ('Mesero', 'Mesero')]                                           
    )
    
    Rol = models.CharField (
        max_length=13,
        choices=[('Administrador', 'Administrador'), ('Cocina', 'Cocina'), ('Bebidas', 'Bebidas'), ('Mesero', 'Mesero')]                                             
    )
    
    def __str__(self):
        return self.user.username

#-------------------------------------mesas---------------------------------------------------------------
class Mesas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_mesa = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nombre_mesa

#-------------------------------------id de ordenes---------------------------------------------------------------
class IdOrden(models.Model):
    id = models.AutoField(primary_key=True)
    mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Orden: {self.id} para la {self.mesa}, fecha {self.date.strftime("%b %d %I: %M %p")}.'
    

#-------------------------------------mesa ordenes---------------------------------------------------------------
class Ordenmesas(models.Model):
    id = models.AutoField(primary_key=True)
    
    mesa= models.ForeignKey(Mesas, on_delete=models.CASCADE)
    item= models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad= models.IntegerField(default=1)
    observacion= models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f'Plato: {self.item}, cantidad: {self.cantidad} para la {self.mesa}.'



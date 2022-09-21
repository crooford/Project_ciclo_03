from django.db import models

# Create your models here.
class Menu(models.Model):  
    id = models.AutoField(primary_key=True)
    nombre_plato= models.CharField(max_length=155, blank=False, null=False)
    precio= models.FloatField(null=False, blank=False)
    descripcion= models.CharField(max_length=255, blank=True, null=True)
    tipo_plato= models.CharField (
        max_length=50,
        choices=[('Entrada', 'Entrada'), ('Plato Principal', 'Plato Principal'), ('Postre', 'Postre'), ('Bebida', 'Bebida'), ('Otro', 'Otro')]                                             
    )

    def __str__(self):
        mostrar= self.nombre_plato
        return mostrar
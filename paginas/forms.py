from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Menu, Mesas, Usuario, IdOrden , Ordenmesas

#------------------------------------- formulario para usuarios ---------------------------------------------------------------
class CustomUserCreationForm(UserCreationForm):
     
    class Meta:
       model = User
       fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
       
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user 
   
#------------------------------------- formulario para cargo usuarios ---------------------------------------------------------------
class Usuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('Cargo', 'Rol')

#------------------------------------- formulario para platos del menu ---------------------------------------------------------------
class Menuform(forms.ModelForm):
    class Meta:
        model=Menu
        fields = ('__all__')

#------------------------------------- formulario para mesas --sin usar por el momento ---------------------------------------------------------------
class Mesaform(forms.ModelForm):
    class Meta:
        model=Mesas
        fields=('__all__')

#------------------------------------- formulario para id ordenes --sin usar por el momento ---------------------------------------------------------------
class Idordenform(forms.ModelForm):
    class Meta:
        model=IdOrden
        fields=('__all__')

#------------------------------------- formulario para tomar pedido en las mesas ---------------------------------------------------------------
class Ordenmesasform(forms.ModelForm):
    class Meta:
        model=Ordenmesas
        fields=('__all__')

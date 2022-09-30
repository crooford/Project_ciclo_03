from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Menu, Mesas, Usuario, Ordenplato, Ordenmesa , Ordenmesas


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
   

class Usuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('Cargo', 'Rol')

class Menuform(forms.ModelForm):
    class Meta:
        model=Menu
        fields = ('__all__')

class Mesaform(forms.ModelForm):
    class Meta:
        model=Mesas
        fields=('__all__')

class Ordenmesaform(forms.ModelForm):
    class Meta:
        model=Ordenmesa
        fields=('__all__')

class Ordenplatoform(forms.ModelForm):
    class Meta:
        model=Ordenplato
        fields=('__all__')

class Ordenmesasform(forms.ModelForm):
    class Meta:
        model=Ordenmesas
        fields=('__all__')

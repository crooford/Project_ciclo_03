from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, Usuario
from django.contrib.auth import login, logout, authenticate
from .forms import Menuform
from .models import *
from django.contrib.auth.models import User
from usuario.models import Usuario
from django.views.generic import ListView

# Create your views here.
def usuarios(request):
    usuarios = User.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'usuarios.html', context)
def ppal(request):
    return render(request, 'ppal.html')
def registro(request):
   
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        usuario_form = Usuario(request.POST)
        
        if formulario.is_valid() and usuario_form.is_valid():
            user =formulario.save()
            usuario = usuario_form.save(commit=False)
            usuario.user = user
            
            usuario.save()
            
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
           
            return render(request, 'ppal.html')
    else:
        formulario = CustomUserCreationForm()
        usuario_form = Usuario()     
    context = {'formulario' : formulario, 'usuario_form': usuario_form}    
    return render(request, 'registration/registro.html', context)

def menu(request):
    platos = Menu.objects.all()
    context = {'platos': platos}
    return render(request,'menu.html', context)

def crear_plato(request):
    if request.method == 'GET':
        formulariom = Menuform()
    else:
         formulariom = Menuform(request.POST)
         if formulariom.is_valid():
             formulariom.save()
             return redirect('menu')    
    return render(request, 'crear-plato.html',{'formulariom': formulariom})

def editar_plato(request,id):
    plato= Menu.objects.get(id=id)
    if request.method == 'GET':
        formulariom = Menuform(instance=plato)
        contexto={
            'formulariom': formulariom
        }
    else:
        formulariom = Menuform(request.POST,instance=plato)
        contexto={
            'formulariom': formulariom
        }
        if formulariom.is_valid():
            formulariom.save()
            return redirect('menu')
    return render(request,'editar-plato.html',contexto) 

def eliminar_plato(request,id):
    plato = Menu.objects.get(id=id)
    plato.delete()
    return redirect('menu')

class listUsuario(ListView):
    model = User
    template_name = 'usuarios.html'

def mesero_orden(request):
    return render(request, 'mesero-orden.html')

def mesero_mesas(request):
    mesas = Mesas.objects.all()
    return render(request, 'mesero-mesas.html', {'mesas': mesas})


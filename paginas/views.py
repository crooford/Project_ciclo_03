from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, Usuario
from django.contrib.auth import login, logout, authenticate
from .forms import Menuform
from .models import Menu

# Create your views here.
def usuarios(request):
    return render(request, 'usuarios.html')
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

def crear_plato(request):
    if request.method == 'GET':
        formulario = Menuform()
    else:
         formulario = Menuform(request.POST)
         if formulario.is_valid():
             formulario.save()
             return redirect('menu.html')    
    return render(request, 'crear-plato.html',{'formulario': formulario})

def editar_plato(request,id):
    plato= Menu.objects.get(id=id)
    if request.method == 'POST':
        formulario = Menuform(instance=plato)
        contexto={
            'formulario': formulario
        }
    else:
        formulario = Menuform(request.POST,instance=plato)
        contexto={
            'formulario': formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('menu.html')
    return render(request,'editar_plato.html',contexto) 

def eliminar_plato(request,id):
    plato = Menu.objects.get(id=id)
    plato.delete()
    return redirect('menu.html')


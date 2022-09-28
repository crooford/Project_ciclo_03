from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, Usuario
from django.contrib.auth import login, logout, authenticate
from .forms import Menuform, Mesaform , Ordenmesaform, Ordenplatoform
from .models import Menu, Usuario, Mesas , Ordenplato, Ordenmesa
from django.contrib.auth.models import User
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
        formuser = CustomUserCreationForm(request.POST)
        usuario_form = Usuario(request.POST)
        
        if formuser.is_valid() and usuario_form.is_valid():
            user =formuser.save()
            usuario = usuario_form.save(commit=False)
            usuario.user = user
            
            usuario.save()
            
            user = authenticate(username=formuser.cleaned_data["username"], password=formuser.cleaned_data["password1"])
            login(request, user)
           
            return render(request, 'ppal.html')
    else:
        formuser = CustomUserCreationForm()
        usuario_form = Usuario()     
    context = {'formuse' : formuser, 'usuario_form': usuario_form}    
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
    platos = Menu.objects.all()
    
    entradas= Menu.objects.filter(tipo_plato='Entrada')
    plato_principal= Menu.objects.filter(tipo_plato='Plato Principal')
    postres= Menu.objects.filter(tipo_plato='Postre')
    bebidas= Menu.objects.filter(tipo_plato='Bebida') 
    otros= Menu.objects.filter(tipo_plato='Otro') 
    context = {'platos': platos,
    'entradas': entradas,
    'plato_principal': plato_principal,
    'postres': postres,
    'bebidas': bebidas,
    'otros': otros,
   

    }
    return render(request, 'mesero-orden.html',context)

def mesero_mesas(request):
    mesas = Mesas.objects.all()
    mesaform= Mesaform()
    return render(request, 'mesero-mesas.html', {'mesas': mesas, 'mesaform': mesaform})

def cocinero_list(request):
    return render(request, 'cocinero-comandas-list.html')

def cocinero_todas(request):
    orden= Ordenmesa.objects.all()
    ordenplato= Ordenplato.objects.all()
    menu=Menu.objects.all()
    
    mesa_1= Ordenplato.objects.filter(mesa=1)
    context= {
        'orden': orden ,
        'ordenplato': ordenplato,
        'menu': menu,
        'mesa_1': mesa_1,
        
    }
    return render(request, 'cocinero-comandas-todas.html', context)

def cocinero_mesa(request):
    return render(request, 'cocinero-comandas-mesa.html')


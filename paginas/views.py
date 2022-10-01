from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, Usuario
from django.contrib.auth import login, logout, authenticate
from .forms import Menuform, Ordenmesasform
from .models import Menu, Usuario, IdOrden , Ordenmesas
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.

#-------------------------------------pagina principal---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def ppal(request):

    return render(request, 'ppal.html')

#-------------------------------------registro de usuarios---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
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

#-------------------------------------pagina menu---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def menu(request):
    platos = Menu.objects.all()
    context = {'platos': platos}

    return render(request,'menu.html', context)

#-------------------------------------pagina crear plato---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def crear_plato(request):

    if request.method == 'GET':
        formulariom = Menuform()
    else:
         formulariom = Menuform(request.POST)
         if formulariom.is_valid():
            formulariom.save()
            return redirect('menu') 

    return render(request, 'crear-plato.html',{'formulariom': formulariom})

#-------------------------------------pagina editar plato---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
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

#-------------------------------------eliminar plato---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def eliminar_plato(request,id):
    plato = Menu.objects.get(id=id)
    plato.delete()

    return redirect('menu')

#-------------------------------------editar orden de plato---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def mesero_orden(request, id):
    ordenmesa= Ordenmesas.objects.all()
    idorden= IdOrden.objects.all()
    plato= Ordenmesas.objects.get(id=id)
    if request.method == 'GET':
        formulariom = Ordenmesasform(instance=plato)
        context={
            'formulariom': formulariom
        }
    else:
        formulariom =Ordenmesasform(request.POST,instance=plato)
        context={
            'formulariom': formulariom
        }

        if formulariom.is_valid():
            formulariom.save()

            return redirect('mesero_mesas') 

    context = {
        'formulariom': formulariom,
        'ordenmesa': ordenmesa ,
        'idorden': idorden,
    }

    return render(request, 'mesero-orden.html',context)

#-------------------------------------mesa ordenes---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def mesero_mesas(request):
    ordenmesa= Ordenmesas.objects.all()
    idorden= IdOrden.objects.all()
    
    if request.method == 'GET':
        formulariom = Ordenmesasform()
    else:
        formulariom = Ordenmesasform(request.POST)
        if formulariom.is_valid():
            formulariom.save()

            return redirect('mesero_mesas')
        
    context= {
    'ordenmesa': ordenmesa ,
    'idorden': idorden,
    'formulariom': formulariom,           
    }

    return render(request, 'mesero-mesas.html', context)

#-------------------------------------cocina ordenes---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def cocinero_todas(request):
    ordenmesa= Ordenmesas.objects.all()
    idorden= IdOrden.objects.all()
    
    context= {
        'ordenmesa': ordenmesa ,
        'idorden': idorden,    
    }

    return render(request, 'cocinero-comandas-todas.html', context)

#-------------------------------------vaciar orden de una mesa---------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def vaciar_orden(request,id):
    plato = Ordenmesas.objects.filter(mesa=id)
    plato.delete()

    return redirect('cocinero_todas')
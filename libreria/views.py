from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>WELCOME<h1>")

def login(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contraseña_usuario=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contraseña_usuario)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'admon.html')
            else:
                messages.error(request, "usuario incorrecto")
            
    form=AuthenticationForm()
    return render(request, 'login.html', {"form":form})

def admon(request):
    return render(request, 'admon.html')

def waiter(request):
    return render(request, 'admon-waiter.html')

def menu(request):
    return render(request, 'admon-menu.html')

def waiterData(request):
    return render(request, 'admon-waiter-data.html')



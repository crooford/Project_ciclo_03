from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def admon(request):
    return render(request, 'admon.html')

def waiter(request):
    return render(request, 'admon-waiter.html')

def menu(request):
    return render(request, 'admon-menu.html')

def waiterData(request):
    return render(request, 'admon-waiter-data.html')

def meseroMesas(request):
    return render(request, 'mesero-mesas.html')

def meseroOrden(request):
    return render(request, 'mesero-orden.html')



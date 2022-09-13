from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.


def admon(request):
    return render(request, 'admon.html')

def waiter(request):
    return render(request, 'admon-waiter.html')

def menu(request):
    return render(request, 'admon-menu.html')

def waiterData(request):
    return render(request, 'admon-waiter-data.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    return render(request, 'registration/registro.html', data)



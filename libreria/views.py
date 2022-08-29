from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>WELCOME<h1>")

def login(request):
    return render(request, 'LOGIN.html')

def admon(request):
    return render(request, 'ADMON.html')

def waiter(request):
    return render(request, 'ADMON-WAITER.html')

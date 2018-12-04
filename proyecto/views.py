from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.

#Creamos un metodo Index/ Request este almacena toda la info desde el servidor hacia nosotros

def index(request):
    return render(request,'index.html',{})

def registro(request):
    return render(request, 'register.html',{})

def crear(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    contrasenia  = request.POST.get('contrasenia','')
    usuario = Usuario(nombre=nombre,correo=correo,contrasenia=contrasenia)
    usuario.save()
    return HttpResponse("nombre :" +nombre+ " correo:  "+correo+ "  contrasenia: "+contrasenia)
    
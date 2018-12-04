from django.shortcuts import render

# Create your views here.

#Creamos un metodo Index/ Request este almacena toda la info desde el servidor hacia nosotros

def index(request):
    return render(request,'index.html',{'nombre': "Alonso"})

def login(request):
    return render(request,'login.html',{})


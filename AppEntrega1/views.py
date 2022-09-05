from django.shortcuts import render
from AppEntrega1.forms import *
from AppEntrega1.models import *
from django.http import HttpResponse


def Inicio (request):
    return render(request, "inicio.html")

def Modelo1 (request):
    return render(request, "Modelo1.html")

def Modelo2 (request):
    return render(request, "Modelo2.html")

def Modelo3 (request):
    return render(request, "Modelo3.html")


#ESTE ES EL FORMULARIO PARA INGRESAR DATOS A MODELO1
def FormularioModelo1(request):
    if request.method=="POST":
       form=Modelo1Form(request.POST)
       if form.is_valid():
        informacion=form.cleaned_data
        nombre=informacion["nombre"]
        comision=informacion["comision"]
        modelo=ClaseModelo1(nombre=nombre, comision=comision)
        modelo.save()
        return render(request, "Modelo1.html",{"mensaje": "Formulario Creado Correctamente"})

    else:
        formulario=Modelo1Form()
        return render (request, "FormularioModelo1.html",{"formulario":formulario})


#ESTE ES EL FORMULARIO PARA INGRESAR DATOS A MODELO2
def FormularioModelo2(request):
    if request.method=="POST":
       form=Modelo2Form(request.POST)
       if form.is_valid():
        informacion=form.cleaned_data
        nombre=informacion["nombre"]
        apellido=informacion["apellido"]
        email=informacion["email"]
        modelo2=ClaseModelo2(nombre=nombre, apellido=apellido, email=email)
        modelo2.save()
        return render(request, "Modelo2.html",{"mensaje": "Formulario Creado Correctamente"})

    else:
        formulario=Modelo2Form()
        return render (request, "FormularioModelo2.html",{"formulario":formulario})

#ESTE ES EL FORMULARIO PARA INGRESAR DATOS A MODELO3
def FormularioModelo3(request):
    if request.method=="POST":
       form=Modelo3Form(request.POST)
       if form.is_valid():
        informacion=form.cleaned_data
        nombre=informacion["nombre"]
        apellido=informacion["apellido"]
        email=informacion["email"]
        profesion=informacion["profesion"]
        modelo=ClaseModelo3(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
        modelo.save()
        return render(request, "Modelo3.html",{"mensaje": "Formulario Creado Correctamente"}) #NO ME ESTA TRAYENDO ESTO

    else:
        formulario=Modelo3Form()
        return render (request, "FormularioModelo3.html",{"formulario":formulario})

#ESTOS VAN A SER LOS FORMULARIOS PARA REALIZAR LAS BUSQUEDAS QUE NOS PIDEN

def BusquedaModelo2 (request):
    return render(request, "BusquedaModelo2.html")

def BuscarModelo2(request):
    if request.GET["apellido"]:
      apellido=request.GET["apellido"]
      variable=ClaseModelo2.objects.filter(apellido__icontains=apellido)
      return render (request, "BuscarModelo2.html", {"apellido":variable})
    else:
      return render (request, "BusquedaModelo2.html", {"mensaje":"Debes ingresar datos validos"})
#ME ESTA FALTANDO CREAR LA FUNCION EN LA QUE EL HTML BUSCAR VA A REALIZAR EL FOR PARA ENCONTRAR LOS DATOS
    


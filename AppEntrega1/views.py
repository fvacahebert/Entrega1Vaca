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


#VER SI DEJO ESTE FORMULARIO O LO BORRO
#def FormularioModelo1(request):
    #if request.method=="POST":
       #form=Modelo1Form(request.POST)
       #if form.is_valid():
        #informacion=form.cleaned_data
        #nombre=informacion["nombre"]
        #comision=informacion["comision"]
        #modelo=ClaseModelo1(nombre=nombre, comision=comision)
        #modelo.save()
       # return render(request, "Modelo1.html",{"mensaje": "Formulario Creado Correctamente"})

   # else:
        #formulario=Modelo1Form()
        #return render (request, "FormularioModelo1.html",{"formulario":formulario})


#ESTE ES EL FORMULARIO PARA INGRESAR LOS REGISTROS EN LA PAGINA
def FormularioModelo2(request):
    if request.method=="POST":
       form=Modelo2Form(request.POST)
       if form.is_valid():
        informacion=form.cleaned_data
        nombre=informacion["nombre"]
        apellido=informacion["apellido"]
        email=informacion["email"]
        usuario=informacion["usuario"]
        contrasenia=informacion["contrasenia"]
        modelo2=ClaseModelo2(nombre=nombre, apellido=apellido, email=email, usuario=usuario, contrasenia=contrasenia)
        modelo2.save()
        return render(request, "inicio.html",{"mensaje": "Formulario Creado Correctamente"})

    else:
        formulario=Modelo2Form()
        return render (request, "FormularioModelo2.html",{"formulario":formulario})

#ESTE FORMULARIO VA A SER PARA EL CONTACT US
def FormularioModelo3(request):
    if request.method=="POST":
       form=Modelo3Form(request.POST)
       if form.is_valid():
        informacion=form.cleaned_data
        nombre=informacion["nombre"]
        apellido=informacion["apellido"]
        email=informacion["email"]
        texto=informacion["texto"]
        modelo=ClaseModelo3(nombre=nombre, apellido=apellido, email=email, texto=texto)
        modelo.save()
        return render(request, "inicio.html",{"mensaje": "Gracias por contactarte con nosotros. Nuestro equipo se comunicara con vos"}) 

    else:
        formulario=Modelo3Form()
        return render (request, "FormularioModelo3.html",{"formulario":formulario})

#ESTOS SON LOS FORMULARIOS PARA BUSQUEDA DE REGISTROS

def BusquedaModelo2 (request):
    return render(request, "BusquedaModelo2.html")

def BuscarModelo2(request):
    if request.GET["apellido"]:
      apellido=request.GET["apellido"]
      variable=ClaseModelo2.objects.filter(apellido__icontains=apellido)
      return render (request, "BuscarModelo2.html", {"apellido":variable})
    else:
      return render (request, "BusquedaModelo2.html", {"mensaje":"Debes ingresar datos validos"})

    


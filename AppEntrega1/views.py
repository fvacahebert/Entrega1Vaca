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
        modelo=ClaseModelo2(nombre=nombre, apellido=apellido, email=email)
        modelo.save()
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
        return render(request, "Modelo3.html",{"mensaje": "Formulario Creado Correctamente"})

    else:
        formulario=Modelo3Form()
        return render (request, "FormularioModelo3.html",{"formulario":formulario})

#ESTOS VAN A SER LOS FORMULARIOS PARA REALIZAR LAS BUSQUEDAS QUE NOS PIDEN

"""def BusquedaComision (request): #Esta es la vista para buscar datos en un formulario
    return render(request, "AppCoder/BusquedaComision.html")"""

"""def Buscar(request):
    #Esta linea de if es para cuando un usuario busca algo sin ingresar parametro (Blanco)
    if request.GET["comision"]:
      comision=request.GET["comision"] #Aca recibe la comision ingresada por formulario
      cursos=Curso.objects.filter(comision__icontains=comision) #Traiga de la base todos los cursos que tengan comision
      #cursos=Curso.objects.all() esto traeria todos los objetos que estan en la base. (el icontains es para que haga una busqueda por parametro y no de palabra exacta)
      #cursos=Curso.objects.get(comision=comision) Este me trae uno
      return render (request, "AppCoder/Buscar.html", {"cursos":cursos}) # Este es el diccionario que va ir al template de buscar para hacer la funcion for de busqueda
    else:
      return render (request, "AppCoder/BusquedaComision.html", {"mensaje":"Debes ingresar datos validos"})"""

    


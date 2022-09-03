from django.contrib import admin
from django.urls import path
from AppEntrega1.views import *

urlpatterns = [

    path("",Inicio,name="home"),
    path("Modelo1/",Modelo1,name="Modelo1"),
    path("Modelo2/",Modelo2,name="Modelo2"),
    path("Modelo3/",Modelo3,name="Modelo3"),
    path("FormularioModelo1/",FormularioModelo1,name="formulario1"),
    path("FormularioModelo2/",FormularioModelo2,name="formulario2"),
    path("FormularioModelo3/",FormularioModelo3,name="formulario3"),

]
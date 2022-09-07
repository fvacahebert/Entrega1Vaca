from django import forms

#TENGO QUE VER SI BORRO ESTA CLASE
#class Modelo1Form(forms.Form):
    #nombre= forms.CharField(max_length=50)
    #comision= forms.IntegerField()


#Clase para registro
class Modelo2Form(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    usuario=forms.CharField(max_length=50)
    contrasenia=forms.CharField(max_length=50)

#Clase para contacto
class Modelo3Form(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    texto=forms.CharField(max_length=400)
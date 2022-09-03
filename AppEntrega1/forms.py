from django import forms

class Modelo1Form(forms.Form):
    nombre= forms.CharField(max_length=50)
    comision= forms.IntegerField()

class Modelo2Form(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()

class Modelo3Form(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)
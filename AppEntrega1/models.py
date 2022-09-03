from django.db import models

# Create your models here.

class ClaseModelo1(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)

class ClaseModelo2(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.email)

class ClaseModelo3(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.email)+" "+self.profesion

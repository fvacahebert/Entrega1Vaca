from django.db import models


#VER SI BORRO ESTA CLASE
#class ClaseModelo1(models.Model):
    #nombre=models.CharField(max_length=50)
    #comision=models.IntegerField()

    #def __str__(self):
        #return self.nombre+" "+str(self.comision)


#ESTA ES LA CLASE PARA LOS REGISTROS DE LA PAGINA
class ClaseModelo2(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    usuario=models.CharField(max_length=50)
    contrasenia=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.email)+" "+str(self.usuario)+" "+str(self.contrasenia)


#Clase para contacto
class ClaseModelo3(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    texto=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.email)+" "+self.texto

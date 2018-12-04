from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    def __str__(self):
        return "nombre: "+self.nombre+" correo: "+self.correo

from django.db import models

class DatoPersonal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_servicio

class Agenda(models.Model):
    fecha = models.DateField()
    horario = models.TimeField()

    
    def __str__(self):
        return f"{self.fecha} a las {self.horario}"
from django.db import models
from django.contrib.auth.models import User

class DatoPersonal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    nombre = models.CharField(max_length=100, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.nombre}"

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_servicio

class Agenda(models.Model):
    fecha = models.DateField()
    horario = models.TimeField()
    
    def __str__(self):
        return f"{self.fecha} a las {self.horario}"
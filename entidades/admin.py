from django.contrib import admin
from .models import DatoPersonal, Servicio, Agenda

# 1. Clase para el modelo DatoPersonal
@admin.register(DatoPersonal)
class DatoPersonalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'telefono') 
    search_fields = ('nombre', 'telefono') 

# 2. Clase para el modelo Servicio
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio',)
    search_fields = ('nombre_servicio',)

# 3. Clase para el modelo Agenda
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'horario') 
    list_filter = ('fecha',) 
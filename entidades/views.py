from django.shortcuts import render, redirect, reverse 
from .models import DatoPersonal, Servicio, Agenda
from django.contrib import messages 

def agenda_view(request):
    template_name = 'entidades/index.html'
    
    if request.method == 'POST': 
        
        
        # 1. Datos Personales
        if 'nombre' in request.POST and 'edad' in request.POST and 'telefono' in request.POST:
            try:
                edad_valor = int(request.POST.get('edad')) if request.POST.get('edad').isdigit() else None
                
                
                DatoPersonal.objects.create(
                    nombre=request.POST.get('nombre'),
                    edad=edad_valor, 
                    telefono=request.POST.get('telefono')
                )
                messages.success(request, "Datos personales guardados con éxito.")
            except Exception as e:
                 messages.error(request, f"Error al guardar datos personales: {e}")
                 print(f"Error de depuración: {e}")
                 
        # 2. Servicio a Realizar
        elif 'nombre_servicio' in request.POST:
            try:
                Servicio.objects.create(
                    nombre_servicio=request.POST.get('nombre_servicio')
                )
                messages.success(request, "Servicio registrado con éxito.")
            except Exception as e:
                messages.error(request, f"Error al registrar servicio: {e}")
            
        # 3. Lógica para Agenda
        # Solo se ejecuta si AMBOS campos (fecha Y horario) están presentes.
        elif 'fecha' in request.POST and 'horario' in request.POST:
            try:
                Agenda.objects.create(
                    fecha=request.POST.get('fecha'),
                    horario=request.POST.get('horario')
                )
                messages.success(request, "Cita (Día y Horario) guardada con éxito.")
            except Exception as e:
                messages.error(request, f"Error al guardar la cita: {e}. Revisa si tu modelo Agenda permite campos vacíos.")
        
        return redirect('home')

    return render(request, template_name)
from django.shortcuts import render, redirect
from .models import DatoPersonal, Servicio, Agenda
from django.contrib import messages 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required

# VISTA PRINCIPAL (AGENDA Y FORMULARIOS)
def agenda_view(request):
    template_name = 'entidades/index.html'
    
    # 1. Buscamos el perfil del usuario logueado actualmente para mostrar la foto
    paciente_actual = None
    if request.user.is_authenticated:
        try:
            paciente_actual = DatoPersonal.objects.get(user=request.user)
        except DatoPersonal.DoesNotExist:
            paciente_actual = None
    
    # Si el usuario intenta enviar datos (POST)
    if request.method == 'POST': 
        if not request.user.is_authenticated:
            messages.error(request, "Debes iniciar sesión para realizar esta acción.")
            return redirect('login')

        # --- 1. Lógica para Datos Personales y Foto (PUNTO 4 ACTUALIZADO) ---
        if 'foto' in request.FILES or 'nombre' in request.POST:
            try:
                # Buscamos o creamos el perfil único para este usuario para evitar duplicados
                perfil, created = DatoPersonal.objects.get_or_create(user=request.user)

                # Si el usuario llenó los campos de texto del formulario
                if 'nombre' in request.POST:
                    perfil.nombre = request.POST.get('nombre')
                    
                    # Manejo seguro de la edad: si está vacío o no es número, se guarda como None
                    edad_input = request.POST.get('edad')
                    if edad_input and edad_input.isdigit():
                        perfil.edad = int(edad_input)
                    else:
                        perfil.edad = None

                    perfil.telefono = request.POST.get('telefono')

                # Si se detecta una foto (por el auto-submit del círculo o el form)
                if 'foto' in request.FILES:
                    perfil.foto = request.FILES.get('foto')

                perfil.save() # Guardado definitivo
                messages.success(request, "Perfil actualizado correctamente.")
                
            except Exception as e:
                 messages.error(request, f"Error al guardar datos: {e}")
                 
        # --- 2. Servicio a Realizar ---
        elif 'nombre_servicio' in request.POST:
            try:
                Servicio.objects.create(
                    nombre_servicio=request.POST.get('nombre_servicio')
                )
                messages.success(request, "Servicio registrado con éxito.")
            except Exception as e:
                messages.error(request, f"Error al registrar servicio: {e}")
            
        # --- 3. Lógica para Agenda ---
        elif 'fecha' in request.POST and 'horario' in request.POST:
            try:
                Agenda.objects.create(
                    fecha=request.POST.get('fecha'),
                    horario=request.POST.get('horario')
                )
                messages.success(request, "Cita guardada con éxito.")
            except Exception as e:
                messages.error(request, f"Error al guardar la cita: {e}")
        
        return redirect('home')

    # Contexto para cargar la info de la clínica y el paciente logueado
    context = {
        'info_clinica': {
            'nombre': 'Odontología Gómez y Asociados',
            'descripcion': 'Líderes en salud bucal con más de 10 años de experiencia.',
        },
        'paciente_actual': paciente_actual 
    }
    return render(request, template_name, context)


# __________________ SECCIÓN DE AUTENTICACIÓN __________________

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data


def registro_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registro.html', {'form': form})
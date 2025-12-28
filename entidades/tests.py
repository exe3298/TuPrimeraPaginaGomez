from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import DatoPersonal, Agenda, Servicio

class OdontologiaTests(TestCase): 

    def setUp(self):
        """Configuración inicial para las pruebas"""
        self.client = Client()
        # Creamos un usuario de prueba para los tests
        self.user = User.objects.create_user(username='paciente_test', password='password123')

    # TEST 1: Login de Usuario (Coincide con ID 1 del Excel)
    def test_login_usuario(self):
        response = self.client.post(reverse('login'), {
            'username': 'paciente_test',
            'password': 'password123'
        })
        # Verifica redirección exitosa (302) tras el login
        self.assertEqual(response.status_code, 302) 

    # TEST 2: Carga de Perfil (Coincide con ID 2 del Excel)
    def test_creacion_objeto_perfil(self):
        # El sistema debe crear/obtener el perfil vinculado al usuario
        perfil, created = DatoPersonal.objects.get_or_create(user=self.user)
        self.assertTrue(DatoPersonal.objects.filter(user=self.user).exists())

    # TEST 3: Campos Opcionales / Nulos (Coincide con ID 3 del Excel)
    def test_campos_perfil_nulos(self):
        self.client.login(username='paciente_test', password='password123')
        perfil, created = DatoPersonal.objects.get_or_create(user=self.user)
        
        # Simulamos guardar datos dejando nombre y edad vacíos
        perfil.nombre = None
        perfil.edad = None
        perfil.save()
        
        # Verificamos que la base de datos acepta los valores nulos (lo que arreglamos en models.py)
        self.assertIsNone(perfil.nombre)
        self.assertIsNone(perfil.edad)

    # TEST 4: Agendar Turno (Coincide con ID 4 del Excel)
    def test_agendar_turno_agenda(self):
        # Verificamos que el modelo Agenda guarda correctamente la información
        cita = Agenda.objects.create(
            fecha="2025-05-20",
            horario="10:30"
        )
        self.assertTrue(Agenda.objects.filter(fecha="2025-05-20", horario="10:30").exists())

    # TEST 5: Registro de Servicio (Coincide con ID 5 del Excel)
    def test_registro_nuevo_servicio(self):
        # Verificamos que el sistema puede dar de alta nuevos tratamientos o servicios
        servicio = Servicio.objects.create(
            nombre_servicio="Limpieza Dental Completa"
        )
        self.assertEqual(servicio.nombre_servicio, "Limpieza Dental Completa")
        self.assertTrue(Servicio.objects.filter(nombre_servicio="Limpieza Dental Completa").exists())
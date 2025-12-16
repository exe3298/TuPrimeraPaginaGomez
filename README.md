# ODONTOLOGÍA GÓMEZ Y ASOCIADOS - Sistema de Agendamiento

Una aplicación web desarrollada con Django para permitir a los clientes registrar sus datos, seleccionar un servicio odontológico y agendar una cita (día y horario).

## Funcionalidades Principales

El sistema está diseñado para capturar la información de la cita en tres etapas dentro de la página principal:

- **Registro de Datos Personales**: Captura el nombre, edad y teléfono del paciente. (Modelo `DatoPersonal`)
- **Registro de Servicio**: Permite seleccionar el tipo de servicio odontológico requerido (Ej: Limpieza, Extracción, Consulta). (Modelo `Servicio`)
- **Agendamiento de Cita**: Fija el día y el horario de la cita. (Modelo `Agenda`)
- **Panel Admin**: Administrar todos los datos de pacientes, servicios y citas desde el administrador de Django.

## Cómo usar
 
### Página Principal
- Accede a `http://localhost:8000/`
- Verás la página de bienvenida con la información a completar por parte del paciente

### Introducción de datos personales
1. Ve a `http://localhost:8000/datos_personales/`
2. Completa los campos vacíos (nombre, edad, telefono)

### Introducción de servicio a realizar
1. Ve a `http://localhost:8000/servicio/`
2. Completa los campos vacíos (servicio a realizar)

### Introducción de fecha y horario
1. Ve a `http://localhost:8000/horario/`
2. Completa los campos vacíos (fecha y horario)

### Panel Admin
1. Ve a `http://localhost:8000/admin/`
2. Ingresa con las credenciales de superusuario
3. Aquí puedes ver, crear, editar y eliminar todos los datos

## Estructura de carpetas
```
TuPrimeraPaginaGomez/
├── entidades/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── entidades/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── TuPrimeraPaginaGomez/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── sd.md
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cv.db
├── db.sqlite3
├── manage.py
└── README.md
```

## Modelos

### DatoPersonal
- nombre (CharField)
- edad (IntegerField)
- telefono (CharField)

### Servicio
- nombre_servicio (CharField)

### Agenda
- fecha (DateField)
- horario (TimeField)

## Autor

Exequiel Gómez

## Licencia

MIT

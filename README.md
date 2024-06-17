# Servicio de Consulta, Extracción y Transformación de Datos

Este servicio está diseñado para manejar operaciones de consulta, extracción y transformación de datos desde una base de datos, proporcionando una interfaz API clara y bien documentada. Utiliza Flask para el backend y SQLAlchemy para la interacción con la base de datos, asegurando una administración de datos eficiente y segura.

## Características

- **Modularidad**: Estructura organizada y modular que facilita el mantenimiento y la extensión del servicio.
- **Escalabilidad**: Arquitectura diseñada para manejar un gran número de solicitudes simultáneas.
- **Seguridad**: Configuración y manejo seguro de los datos y conexiones a la base de datos.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/Servicecasecreator


Accede a la documentación de la API en tu navegador visitando la URL http://localhost:4000/docs.

## Estructura del Servicio
   ```bash
   api-get-data/
├── requirements.txt          # Dependencias del proyecto
└── src/
    ├── run.py                # Punto de entrada de la aplicación
    └── app/
        ├── config.py         # Configuración de la aplicación
        ├── models.py         # Modelos de datos
        ├── __init__.py       # Inicialización del paquete app
        ├── routes/
        │   └── caseCreator.py # Rutas para el servicio de creación de casos
        └── static/
            └── Swagger.json  # Documentación Swagger de la API


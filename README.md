# Sistema de Nómina de Pagos

Este proyecto es un sistema de nómina de pagos desarrollado con Django. Permite gestionar la información de empleados, departamentos, contratos y la generación de roles de pago mensuales.

## Estructura del Proyecto

El proyecto está organizado en varias aplicaciones, cada una encargada de una parte específica del sistema:

- **employees**: Maneja la información relacionada con los empleados, incluyendo sus datos personales y cargos.
- **departments**: Gestiona los departamentos dentro de la organización.
- **contracts**: Administra los diferentes tipos de contratos que pueden tener los empleados.
- **payroll**: Se encarga de la generación de roles de pago mensuales y la gestión de nómina.

## Requisitos

- Python 3.x
- Django 4.x o superior

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Navega al directorio del proyecto:
   ```
   cd payroll_system
   ```
3. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Configuración

1. Configura la base de datos en `payroll_system/settings.py`.
2. Realiza las migraciones:
   ```
   python manage.py migrate
   ```
3. Crea un superusuario para acceder al panel de administración:
   ```
   python manage.py createsuperuser
   ```

## Uso

Para iniciar el servidor de desarrollo, ejecuta:
```
python manage.py runserver
```
Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cambios.

## Licencia

Este proyecto está bajo la Licencia MIT.
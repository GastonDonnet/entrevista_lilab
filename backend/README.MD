# DJANGO API
## Instalación / Configuración

- Crear/Activar venv
- Instalar dependencias de `requirements.txt`
- Configurar Postgres
- Seedear

## Configurar Postgres

- `CREATE DATABASE django_project;`
- `CREATE USER root WITH PASSWORD 'root';`
- `ALTER ROLE root SET client_encoding TO 'utf8';`
- `ALTER ROLE root SET default_transaction_isolation TO 'read committed';`
- `ALTER ROLE root SET timezone TO 'UTC';`
- `GRANT ALL PRIVILEGES ON DATABASE django_project TO root;`

Por defecto la API utiliza

- Usuario: `root`
- Contraseña: `root`
- Base de datos: `django_project`
- Puerto: `5432`

## Data Seed

- `python manage.py seed`

## Notas

- Tiene configurado el panel administrador básico.
- No se necesita loguearse para utilizar la API.
- Nada esta configurado a través de variables de entorno
# API Bancaria - FastAPI + MongoDB + Docker

Este proyecto consiste en una API REST para la gestión de cuentas bancarias, construida con **FastAPI**, **MongoDB** como base de datos y **Docker** para facilitar su despliegue y desarrollo.

---

## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [pytest](https://docs.pytest.org/)

---

## Arquitectura y Patrones de Desarrollo

### Arquitectura: **MVC (Model - View - Controller)**

El proyecto sigue una arquitectura **MVC simplificada**, adaptada a FastAPI:

- **Modelos (`models/`)**: Definen la estructura y validación de datos usando Pydantic.
- **Rutas (`routes/`)**: Actúan como controladores. Reciben las peticiones y delegan al servicio.
- **Servicios (`services/`)**: Contienen la lógica de negocio y manejo directo con la base de datos.
- **Esquemas (`schemas/`)**: Transforman los datos entre MongoDB y los modelos que se retornan a los clientes (view models).


### Patrones de desarrollo aplicados

- **Separación de responsabilidades**: Cada archivo tiene una única responsabilidad (modelo, ruta, lógica de negocio, transformación de datos).
- **Repository-like pattern**: Los servicios funcionan como una capa intermedia entre la base de datos y las rutas, centralizando la lógica.
- **Fixture en testing**: Uso de `pytest.fixture` para limpiar datos y mantener pruebas aisladas.
- **Inyección de dependencias ligera**: La conexión a MongoDB se abstrae en un archivo separado (`config/bd.py`) y se utiliza en los servicios.


---


## Testing

Las pruebas están escritas con `pytest` y utilizan el `TestClient` de FastAPI. Se prueban:

- Creación de cuentas
- Listado de cuentas
- Actualización de saldo

### Ejecutar pruebas sin Docker (modo local)

Asegúrate de tener un entorno virtual creado e instalar dependencias con:

```bash
pip install -r requirements.txt
``` 

Luego ejecuta las pruebas con:

```bash
pytest tests/
``` 

### Ejecutar pruebas dentro de Docker

Ingresar al contenedor y correr las pruebas manualmente:

```bash
docker-compose exec api_banco bash
``` 

```bash
pytest tests/
``` 

## Uso con Docker y Docker Compose

### Construcción y ejecución

```bash
docker-compose up --build
``` 

Esto levanta:

- La API en: http://localhost:8000

- MongoDB en: mongodb://localhost:27017

### Instalación y uso local sin Docker

Si prefieres correr la aplicación sin usar Docker, sigue estos pasos:

1. Clonar el repositorio

```bash
git clone https://github.com/Sangozu13/api-banco-fastapi.git
``` 

cd api-banco

2. Crear un entorno virtual

```bash
python -m venv env
``` 

```bash
source env/bin/activate
``` 

3. Instalar dependencias

```bash
pip install -r requirements.txt
``` 

4. Ejecutar la aplicación

```bash
uvicorn app:app --reload
``` 

Esto levantará la API en http://127.0.0.1:8000

### Requisito: Instancia de MongoDB

Para que la API funcione correctamente, asegúrate de tener una instancia de MongoDB corriendo localmente en:

mongodb://localhost:27017


## Estructura del proyecto

```plaintext
.
├── Dockerfile
├── docker-compose.yml
├── app.py
├── config/
│   └── bd.py
├── models/
│   └── bank_models.py
├── routes/
│   └── bank_routes.py
├── schemas/
│   └── bank_schemas.py
├── services/
│   └── bank_services.py
├── tests/
│   └── test_accounts.py
└── requirements.txt
```

## Endpoints principales

(Método - Endpoint - Descripción)

- `GET -  /accounts` – Lista todas las cuentas  
- `GET - /accounts/{id}` – Consulta una cuenta por ID  
- `POST - /accounts` – Crea una nueva cuenta  
- `PATCH -  /accounts/{id}` – Actualiza el saldo de una cuenta  
- `DELETE - /accounts/{id}` – Elimina una cuenta (opcional)  


## Notas
- El entorno está configurado para desarrollo en caliente gracias a --reload en Uvicorn.

- Puedes usar herramientas como Postman o Swagger UI para probar los endpoints fácilmente.

## Autor

Desarrollado por Santiago Gómez
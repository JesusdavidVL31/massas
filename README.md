# Masas Antioquia - Backend

## Descripción
"Masas Antioquia" es una aplicación que permite a los usuarios registrarse, iniciar sesión y gestionar ventas de productos como masas de maíz y agua de maíz. La API está construida con FastAPI y utiliza SQLAlchemy para la interacción con la base de datos.

## Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone <>
   ```
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
5. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload
   ```
6. La API estará disponible en `http://localhost:8000`.

## Tecnologías Utilizadas
- **FastAPI**: Framework para construir APIs.
- **SQLAlchemy**: ORM para interactuar con la base de datos MySQL.
- **MySQL**: Base de datos.
- **JWT (JSON Web Tokens)**: Para autenticación de usuarios.

## Integrantes
- **Jesús David Vásquez** (Backend Developer)



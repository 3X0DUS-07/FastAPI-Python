
# API de Proyectos con FastAPI

Este es un proyecto simple que utiliza **FastAPI** para exponer una API REST que devuelve una lista de proyectos. Incluye una interfaz HTML básica que consume la API usando **fetch**. Fue testeado exitosamente con **Postman** y **Thunder Client**.

## Estructura del proyecto

```
proyecto/
├── main.py             # Servidor FastAPI
├── index.html          # Interfaz de usuario (frontend simple)
└── requirements.txt    # Dependencias del proyecto
```

## Requisitos

- Python 3.10 o superior
- Navegador moderno (para consumir el HTML)
- Herramientas opcionales: Postman o Thunder Client (para probar la API)

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/proyecto-api-fastapi.git
cd proyecto-api-fastapi
```

2. Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate   # En Windows usa: venv\Scripts\activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución del servidor

Inicia la API con:

```bash
uvicorn main:app --reload
```

Esto levantará el servidor en:  
http://127.0.0.1:8000

Puedes ver la documentación automática de la API en:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Ver la interfaz web

Abre el archivo `index.html` directamente en tu navegador.

Este archivo hace una solicitud `fetch` al endpoint `/projects` y muestra los proyectos en una lista.

## Endpoint disponible

| Método | Endpoint       | Descripción               |
|--------|----------------|---------------------------|
| GET    | `/projects`    | Retorna lista de proyectos |

Ejemplo de respuesta:

```json
{
  "projects": [
    {"id": 1, "name": "Proyecto A", "status": "active"},
    {"id": 2, "name": "Proyecto B", "status": "inactive"}
  ]
}
```

## Pruebas

Este proyecto fue probado usando:

- Postman
- Thunder Client (extensión para VS Code)

Puedes enviar peticiones GET a `http://127.0.0.1:8000/projects` para verificar la respuesta.

## Tecnologías utilizadas

- FastAPI
- Uvicorn
- HTML5
- JavaScript Fetch API

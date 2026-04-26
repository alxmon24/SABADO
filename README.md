# Sabado - Backend Flask + Web UI

Backend en Flask para un asistente tipo Jarvis llamado **Sabado**, con memoria en SQLite e interfaz web minimalista tipo consola futurista.

## Funcionalidades

- `POST /chat`
- Request JSON: `{ "mensaje": "..." }`
- Response JSON: `{ "respuesta": "..." }`
- Memoria persistente en SQLite:
  - Guarda conversación (mensaje de usuario y respuesta)
  - Recupera contexto de las últimas 5 interacciones para enviar a OpenAI
- Interfaz web en `/` (HTML + CSS + JavaScript)

## Estructura

- `app/__init__.py`: fábrica de aplicación y registro de servicios/rutas
- `app/config.py`: configuración por variables de entorno
- `app/routes/chat.py`: endpoint `/chat` y página `/`
- `app/services/openai_service.py`: integración OpenAI
- `app/services/memory_service.py`: SQLite (guardar y recuperar contexto)
- `app/templates/index.html`: UI del chat
- `app/static/styles.css`: estilo oscuro futurista
- `app/static/app.js`: lógica de frontend con `fetch`
- `run.py`: ejecución local

## Requisitos

- Python 3.10+
- API key de OpenAI

## Cómo correr

1) Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Configurar variables de entorno:

```bash
cp .env.example .env
export $(cat .env | xargs)
```

3) Ejecutar servidor:

```bash
python run.py
```

4) Abrir interfaz web:

- http://localhost:5000

5) Probar API con curl (opcional):

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"mensaje":"Hola Sabado"}'
```

## Notas

- La base SQLite se crea automáticamente en `data/sabado.db`.
- Puedes cambiar ruta de DB con `SQLITE_DB_PATH`.

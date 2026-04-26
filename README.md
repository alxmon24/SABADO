# Sabado - Backend Flask

Backend mínimo en Flask para un asistente tipo Jarvis llamado **Sabado**.

## Endpoint

- `POST /chat`
- Request JSON:

```json
{ "mensaje": "Hola Sabado" }
```

- Response JSON:

```json
{ "respuesta": "..." }
```

## Requisitos

- Python 3.10+
- Clave de OpenAI (`OPENAI_API_KEY`)

## Cómo correr

1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configurar variables de entorno:

```bash
cp .env.example .env
# Edita .env con tu OPENAI_API_KEY
export $(cat .env | xargs)
```

3. Ejecutar el servidor:

```bash
python run.py
```

4. Probar endpoint:

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"mensaje":"Hola, ¿quién eres?"}'
```

## Estructura

- `app/__init__.py`: fábrica de aplicación
- `app/config.py`: configuración
- `app/routes/chat.py`: endpoint `/chat`
- `app/services/openai_service.py`: integración con OpenAI
- `run.py`: punto de entrada

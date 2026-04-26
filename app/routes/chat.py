from flask import Blueprint, current_app, jsonify, render_template, request

chat_bp = Blueprint("chat", __name__)


@chat_bp.get("/")
def home() -> str:
    return render_template("index.html")


@chat_bp.post("/chat")
def chat() -> tuple:
    payload = request.get_json(silent=True) or {}
    mensaje = payload.get("mensaje")

    if not isinstance(mensaje, str) or not mensaje.strip():
        return jsonify({"error": "El campo 'mensaje' es obligatorio."}), 400

    clean_message = mensaje.strip()
    memory_service = current_app.config["MEMORY_SERVICE"]
    contexto = memory_service.recuperar_contexto(limite=5)

    openai_service = current_app.config["OPENAI_SERVICE"]
    respuesta = openai_service.responder(clean_message, contexto=contexto)

    memory_service.guardar_mensajes(clean_message, respuesta)

    return jsonify({"respuesta": respuesta}), 200

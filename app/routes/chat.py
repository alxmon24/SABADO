from flask import Blueprint, current_app, jsonify, request

chat_bp = Blueprint("chat", __name__)


@chat_bp.post("/chat")
def chat() -> tuple:
    payload = request.get_json(silent=True) or {}
    mensaje = payload.get("mensaje")

    if not isinstance(mensaje, str) or not mensaje.strip():
        return jsonify({"error": "El campo 'mensaje' es obligatorio."}), 400

    service = current_app.config["OPENAI_SERVICE"]
    respuesta = service.responder(mensaje.strip())

    return jsonify({"respuesta": respuesta}), 200

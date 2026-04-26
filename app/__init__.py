from flask import Flask

from app.config import Config
from app.routes.chat import chat_bp
from app.services.openai_service import OpenAIService


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    api_key = app.config.get("OPENAI_API_KEY")
    model = app.config.get("OPENAI_MODEL")

    if not api_key:
        raise RuntimeError("Falta OPENAI_API_KEY en variables de entorno.")

    app.config["OPENAI_SERVICE"] = OpenAIService(api_key=api_key, model=model)
    app.register_blueprint(chat_bp)

    return app

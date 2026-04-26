import sqlite3
from pathlib import Path


class MemoryService:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        with self._get_connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS conversaciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mensaje_usuario TEXT NOT NULL,
                    respuesta_asistente TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def guardar_mensajes(self, mensaje_usuario: str, respuesta_asistente: str) -> None:
        with self._get_connection() as conn:
            conn.execute(
                """
                INSERT INTO conversaciones (mensaje_usuario, respuesta_asistente)
                VALUES (?, ?)
                """,
                (mensaje_usuario, respuesta_asistente),
            )

    def recuperar_contexto(self, limite: int = 5) -> list[dict[str, str]]:
        with self._get_connection() as conn:
            rows = conn.execute(
                """
                SELECT mensaje_usuario, respuesta_asistente
                FROM conversaciones
                ORDER BY id DESC
                LIMIT ?
                """,
                (limite,),
            ).fetchall()

        contexto: list[dict[str, str]] = []
        for mensaje_usuario, respuesta_asistente in reversed(rows):
            contexto.append({"role": "user", "content": mensaje_usuario})
            contexto.append({"role": "assistant", "content": respuesta_asistente})

        return contexto

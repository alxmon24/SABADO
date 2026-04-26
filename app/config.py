import os


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "data/sabado.db")

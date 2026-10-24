"""Konfiguration über Umgebungsvariablen mit getrennten Profilen.

APP_ENV=dev   (Standard)  PostgreSQL, wie in docker-compose.yml
APP_ENV=test               SQLite im Arbeitsspeicher, keine Produktions-DB nötig
DATABASE_URL überschreibt in beiden Fällen die Datenbank-Adresse.
"""
import os
from dataclasses import dataclass

DEV_DATABASE_URL = "postgresql+psycopg://wgcook:wgcook@localhost:5432/wgcook"
TEST_DATABASE_URL = "sqlite+pysqlite:///:memory:"


@dataclass(frozen=True)
class Settings:
    app_env: str
    database_url: str


def get_settings() -> Settings:
    app_env = os.getenv("APP_ENV", "dev")
    standard = TEST_DATABASE_URL if app_env == "test" else DEV_DATABASE_URL
    return Settings(app_env=app_env, database_url=os.getenv("DATABASE_URL", standard))

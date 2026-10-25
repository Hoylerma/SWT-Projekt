"""Konfiguration: Profil dev = PostgreSQL, Profil test = SQLite im Speicher."""
import os

DEV_URL = "postgresql+psycopg://wgcook:wgcook@localhost:5432/wgcook"
TEST_URL = "sqlite+pysqlite:///:memory:"


def database_url() -> str:
    standard = TEST_URL if os.getenv("APP_ENV") == "test" else DEV_URL
    return os.getenv("DATABASE_URL", standard)

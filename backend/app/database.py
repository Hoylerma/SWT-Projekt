"""Datenbank-Anbindung (Engine und Session) abhängig vom Konfigurationsprofil."""
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .config import get_settings


def make_engine(url: str) -> Engine:
    if url.startswith("sqlite") and ":memory:" in url:
        # Eine In-Memory-Datenbank gilt je Verbindung, StaticPool teilt eine Verbindung.
        return create_engine(url, connect_args={"check_same_thread": False}, poolclass=StaticPool)
    return create_engine(url)


engine = make_engine(get_settings().database_url)
SessionLocal = sessionmaker(engine, expire_on_commit=False)

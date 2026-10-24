"""Einstiegspunkt der FastAPI-Anwendung. In Lab 4 gibt es nur den Health-Endpunkt."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .config import get_settings
from .database import engine
from .models import Base


@asynccontextmanager
async def lifespan(_app: FastAPI):
    Base.metadata.create_all(engine)  # legt fehlende Tabellen an
    yield


app = FastAPI(title="WG Cook", lifespan=lifespan)


@app.get("/api/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok", "umgebung": get_settings().app_env}

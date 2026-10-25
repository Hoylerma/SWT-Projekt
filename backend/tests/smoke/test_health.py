"""Smoke-Test: Die Anwendung startet im Testprofil und antwortet auf den Health-Endpunkt."""
from fastapi.testclient import TestClient

from app.main import app


def test_health_liefert_ok():
    antwort = TestClient(app).get("/api/v1/health")
    assert antwort.status_code == 200
    assert antwort.json() == {"status": "ok"}

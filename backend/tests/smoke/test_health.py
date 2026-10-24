"""Smoke-Test: Die Anwendung startet im Testprofil und antwortet auf den Health-Endpunkt."""
from fastapi.testclient import TestClient

from app.main import app


def test_health_endpunkt_antwortet_mit_ok_im_testprofil():
    with TestClient(app) as client:  # `with` startet auch das Anlegen der Tabellen
        antwort = client.get("/api/v1/health")

    assert antwort.status_code == 200
    assert antwort.json() == {"status": "ok", "umgebung": "test"}

# WG Cook

WG Cook ist eine Web-App für Wohngemeinschaften: Rezepte mit Zutaten verwalten und saisonal passende Rezepte vorschlagen. Die aktuelle Saison kommt von einem externen Kalender-Dienst.

## Labor 4

- Backend (Python, FastAPI, SQLAlchemy 2, PostgreSQL) mit Domänenmodell `Rezept` und `Zutatenzeile` und Unit-Tests (pytest)
- Frontend-Skelett (Vite, React, React Router) mit den Seiten Start, Rezepte und Not Found
- Docker Compose für Backend und Datenbank

## Labor 5 

- BDD-Akzeptanztests mit behave: Gherkin-Szenarien in `backend/tests/features/`, Step-Definitionen in `backend/tests/features/steps/`
- Handgeschriebener Kalender-Stub und In-Memory-Repository in `backend/tests/stubs/`
- `backend/run_tests.py` führt Unit-, Smoke- und BDD-Tests mit einem Befehl aus

## Tests

```bash
cd backend
pip install -r requirements-dev.txt
python run_tests.py     # komplette Suite
pytest                  # nur Unit- und Smoke-Tests
behave tests/features   # nur BDD-Tests
```


## Schnellstart

```bash
docker compose up --build        # Backend (Port 8000) und PostgreSQL
cd backend && python run_tests.py # Tests, brauchen keine Datenbank
cd frontend && npm install && npm run dev   # Frontend auf Port 5173
```

Ausführliche Anleitung: [docs/setup.md](docs/setup.md). Datenmodell: [docs/spec/data-model.md](docs/spec/data-model.md).

## Hinweis zur KI-Nutzung

Teile dieses Labors wurden mit KI-Unterstützung (Claude) erstellt und vom Team geprüft.

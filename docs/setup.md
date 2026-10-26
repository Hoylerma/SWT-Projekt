# Setup: WG Cook

## Voraussetzungen

- Python 3.12 oder neuer (für die Tests ohne Docker)
- Node.js 22 oder neuer mit npm (für das Frontend)
- Docker mit Docker Compose (für Backend und Datenbank)

## Umgebungsvariablen

| Variable | Bedeutung | Standard |
|---|---|---|
| `APP_ENV` | Profil: `dev` oder `test` | `dev` |
| `DATABASE_URL` | Adresse der Datenbank, überschreibt das Profil | Profil `dev`: PostgreSQL auf `localhost:5432` (Benutzer, Passwort und Datenbank `wgcook`), Profil `test`: SQLite im Arbeitsspeicher |

Für die Tests muss **nichts** gesetzt werden, `backend/tests/conftest.py` setzt `APP_ENV=test` und nutzt damit nie die Produktions-Datenbank.

## Backend und Datenbank starten

```bash
docker compose up --build
```

Danach läuft das Backend auf `http://localhost:8000`, die Datenbank auf Port 5432. Prüfen:

```bash
curl http://localhost:8000/api/v1/health
# {"status":"ok"}
```

## Backend-Tests ausführen (ohne Docker)

```bash
cd backend
python -m venv .venv
# Windows:   .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements-dev.txt

pytest                # alle Tests
pytest tests/unit     # nur die Unit-Tests der Entitäten (ohne Datenbank)
pytest tests/smoke    # nur die Smoke-Tests (health check)
```

Die Tests brauchen weder die PostgreSQL-Datenbank noch den Kalender-Dienst.

## Frontend starten

```bash
cd frontend
npm install
npm run dev      # Entwicklungsserver auf http://localhost:5173
npm run build    # Produktions-Build prüfen
```

Das Frontend ist in Lab 4 nur ein Skelett mit Routing: Startseite (`/`), Rezepte (`/rezepte`) und eine Seite für unbekannte Adressen. Es ruft noch keine API auf.

## Projektstruktur

```
backend/
  app/            Anwendung (config, database, models, main)
  tests/unit/     Unit-Tests der Entitäten, ohne Datenbank
  tests/smoke/    Smoke-Tests (health check)
frontend/         Web-Oberfläche (Vite, React, React Router)
docs/             Dokumentation (spec/ mit Anforderungen, Datenmodell usw.)
docker-compose.yml
```

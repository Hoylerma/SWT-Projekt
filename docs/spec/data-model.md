# Datenmodell: WG Cook

Dieses Dokument beschreibt das Datenmodell, das wir in Lab 4 umgesetzt haben. Grundlage sind die Anforderungen in `docs/spec/requirements.md` (insbesondere FR-01 und FR-02) und unser Pitch in `docs/app.md`. Der Code liegt in `backend/app/models.py`.

## 1 Entitäten

| Entität | Rolle | Tabelle | Beschreibung |
|---|---|---|---|
| **Rezept** | Primärentität | `rezepte` | Ein Rezept mit Name, Portionszahl, optionaler Beschreibung und Zubereitungsschritten und einer Saison-Zuordnung. |
| **Zutatenzeile** | Kind-Entität | `zutatenzeilen` | Eine Zutat eines Rezepts mit Menge und Einheit. |

**Bewusst keine Entität:** Der **Kalender-Dienst** ist eine externe Abhängigkeit und kein Teil unserer Daten. Er liefert das Datum, aus dem das System die Saison ableitet. Die Saison **eines Rezepts** ist dagegen ein einfaches Feld (`saison`). Wir speichern keine Anfragen an den Dienst und kein Ergebnis als eigene Entität, weil dafür kein fachlicher Bedarf besteht (die Zwischenspeicherung aus FR-12 liegt im Arbeitsspeicher des Dienstes, nicht in der Datenbank).

## 2 Beziehung und Kardinalität

Ein Rezept hat **eine bis viele** Zutatenzeilen (1 zu n). Jede Zutatenzeile gehört zu **genau einem** Rezept. Beim Löschen eines Rezepts werden seine Zutatenzeilen mitgelöscht (Cascade). Die Regel "mindestens eine Zutatenzeile je Rezept" (FR-01, FR-05) prüft die Anwendung in der Geschäftslogik (`Rezept.erstelle`, `Rezept.remove_zutat`, `Rezept.validiere`), nicht die Datenbank.

## 3 ER-Diagramm

```mermaid
erDiagram
    REZEPT ||--|{ ZUTATENZEILE : "enthaelt"
    REZEPT {
        int id PK
        string name
        int portionen
        string beschreibung
        string schritte
        string saison
    }
    ZUTATENZEILE {
        int id PK
        int rezept_id FK
        string name
        string name_key
        decimal menge
        string einheit
    }
```

## 4 Felder und Validierung

### Rezept

| Feld | Typ | Pflicht | Regel (aus FR-01) |
|---|---|---|---|
| `id` | Ganzzahl | automatisch | Primärschlüssel |
| `name` | Text | ja | 1 bis 100 Zeichen, Leerraum am Rand wird entfernt |
| `portionen` | Ganzzahl | ja | ganze Zahl von 1 bis 20 |
| `beschreibung` | Text | nein | höchstens 2000 Zeichen, leer wird zu "nicht gesetzt" |
| `schritte` | Text | nein | höchstens 5000 Zeichen, leer wird zu "nicht gesetzt" |
| `saison` | Aufzählung | ja | Frühling, Sommer, Herbst, Winter oder ganzjährig, Standard ganzjährig |

### Zutatenzeile

| Feld | Typ | Pflicht | Regel (aus FR-02) |
|---|---|---|---|
| `id` | Ganzzahl | automatisch | Primärschlüssel |
| `rezept_id` | Ganzzahl | ja | Fremdschlüssel auf `rezepte.id`, beim Löschen des Rezepts mitgelöscht |
| `name` | Text | ja | 1 bis 60 Zeichen |
| `name_key` | Text | automatisch | Name in Kleinschreibung, Grundlage der Eindeutigkeit |
| `menge` | Dezimalzahl | ja | größer 0 und höchstens 99999 |
| `einheit` | Aufzählung | ja | g, kg, ml, l, Stück, EL, TL |

**Eindeutigkeit:** Ein Zutatenname darf in einem Rezept nur einmal vorkommen, ohne Unterscheidung von Groß- und Kleinschreibung. Das sichern **zwei Ebenen**: die Methode `Rezept.add_zutat` (verständliche Fehlermeldung) und ein Eindeutigkeits-Constraint `(rezept_id, name_key)` in der Datenbank als letzte Absicherung.

**Fehlermeldungen:** Jede Validierung wirft einen `ValueError`, dessen Text das betroffene Feld nennt (z. B. "Portionen: ganze Zahl von 1 bis 20 erwartet"). Die spätere API setzt das in HTTP 422 um (FR-14).

## 5 Persistenz-Mapping

- **Relationale Persistenz** mit **PostgreSQL** (Entscheidung aus Lab 1, `docs/spec/tech-stack.md`), angesprochen über **SQLAlchemy 2** (objekt-relationales Mapping).
- Aufzählungen (`saison`, `einheit`) werden als **Text** gespeichert (nicht als native Datenbank-Aufzählung), damit sie sich leicht ändern lassen.
- Die **Menge** wird als `Numeric(12, 3)` gespeichert (exakte Dezimalzahl statt Gleitkomma).
- Tabellen entstehen beim Start der Anwendung (`create_all`). Eine Migrationsverwaltung nutzen wir in diesem Stadium nicht.
- Im **Testprofil** (`APP_ENV=test`) verwendet die Anwendung **SQLite im Arbeitsspeicher** statt PostgreSQL.

## 6 Designentscheidungen

1. **Validierung im Modell:** Die Regeln liegen direkt an den Entitäten, damit sie unabhängig von Oberfläche und Datenbank wirken und ohne Datenbank testbar sind.
2. **Kind-Entität heißt Zutatenzeile:** Eine Zutat hat Menge und Einheit nur im Zusammenhang mit einem Rezept. Die Liste aller bekannten Zutatennamen für die Auswahl (FR-07) ergibt sich aus den Zutatenzeilen aller Rezepte, wir führen dafür keine eigene Tabelle.
3. **`name_key` als gespeicherte Spalte:** So kann die Datenbank die Eindeutigkeit ohne Groß-/Kleinschreibung prüfen.
4. **Keine Benutzerkonten:** Es gibt keine Entität für Nutzer (FR-15, NFR-07).

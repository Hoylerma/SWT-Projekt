
## 1 Vorgehen

Wir verwenden das Qualitätsmodell **ISO/IEC 25010:2011** (acht Produktqualitätsmerkmale). Aus unseren Anforderungen (`docs/spec/requirements.md`) haben wir die **vier** Merkmale ausgewählt, die für WG Cook am wichtigsten sind, und jedes in drei Stufen beschrieben: **abstrakt** (Qualitätsziel), **spezifisch** (was das in unserem Problemraum bedeutet) und **messbar** (Indikator mit Zahl, Limit oder prüfbarem Szenario).

## 2 Auswahl der Merkmale

| Merkmal | Warum wichtig für WG Cook |
|---|---|
| **Functional suitability** | Der einzige Zweck der Anwendung ist, passende Rezepte korrekt zu finden. Falsche Treffer oder falsche fehlende Zutaten machen sie nutzlos. |
| **Reliability** | Die Saison-Funktion hängt von einem externen Dienst ab. Fällt er aus, muss die Anwendung trotzdem nutzbar bleiben. |
| **Usability** | WG-Mitglieder nutzen die Anwendung nebenbei in der Küche, oft am Smartphone und ohne Einweisung. |
| **Maintainability** | Wir arbeiten als Team über das Semester an der Anwendung und müssen sie ändern, erweitern und die externe Abhängigkeit ersetzen können, ohne alles umzubauen. |

## 3 Mini-Qualitätsmodelle

### 3.1 Functional suitability (Functional correctness)

| Stufe | Beschreibung |
|---|---|
| **Abstrakt** | Die Anwendung findet zu den vorhandenen Zutaten die richtigen Rezepte und zeigt korrekt, was fehlt. |
| **Spezifisch** | Für jede Auswahl wird je Rezept die Abdeckung richtig berechnet, die Treffer sind nach Abdeckung und dann nach Saison sortiert, und die angezeigten fehlenden Zutaten sind genau die Zutaten des Rezepts, die nicht in der Auswahl sind. Rezepte mit allen Zutaten sind als "vollständig" gekennzeichnet. |
| **Messbar** | Wir legen einen **Referenzbestand von 10 Rezepten** (mit insgesamt etwa 25 verschiedenen Zutaten) fest und erstellen **5 Zutatenauswahlen** mit von uns **von Hand ermittelter erwarteter Trefferliste** (Reihenfolge, Abdeckung, fehlende Zutaten). Ziel: **in 100 % der 5 Fälle** stimmt das Ergebnis der Anwendung vollständig mit der Erwartung überein. |
| Bezug | FR-07, FR-08, FR-09 |

### 3.2 Reliability (Fault tolerance)

| Stufe | Beschreibung |
|---|---|
| **Abstrakt** | Ein Ausfall des externen Kalender-Dienstes darf die Anwendung nicht unbrauchbar machen. |
| **Spezifisch** | Antwortet der Dienst nicht, zu langsam oder fehlerhaft, liefert die Rezeptsuche trotzdem ein Ergebnis (ohne Saison-Bevorzugung) und zeigt dem Nutzer einen verständlichen Hinweis. Es gibt keinen Absturz, keine leere Fehlerseite und keine doppelt gespeicherten Daten. |
| **Messbar** | (a) Bei **20 simulierten Ausfällen** (je 10 mal Timeout über 2 Sekunden und 10 mal Fehlerantwort oder ungültige Antwort) liefert die Suche in **20 von 20 Fällen** ein Ergebnis mit Hinweis. (b) Die **Antwortzeit** der Suche liegt dabei **höchstens bei 3 Sekunden** (2 Sekunden Timeout plus Verarbeitung). |
| Bezug | FR-12, NFR-02 |

### 3.3 Usability (Learnability, Operability)

| Stufe | Beschreibung |
|---|---|
| **Abstrakt** | Neue Nutzer kommen ohne Einarbeitung zum Ziel. |
| **Spezifisch** | Ein WG-Mitglied, das die Anwendung zum ersten Mal sieht, wählt Zutaten, bekommt Rezepte angezeigt und öffnet eines mit Zutatenliste, ohne dass wir ihm etwas erklären. Fehlende Zutaten sind auf einen Blick erkennbar. |
| **Messbar** | Mit **5 Testpersonen** aus unserem Umfeld, die die Anwendung nicht kennen: **mindestens 4 von 5** erreichen das Ziel "Rezept mit Zutatenliste öffnen" ohne Hilfe und mit **höchstens 3 Interaktionen** (Klicks oder Eingaben) von der Startseite. |
| Bezug | NFR-03, FR-09 |

### 3.4 Maintainability (Modularity, Testability)

| Stufe | Beschreibung |
|---|---|
| **Abstrakt** | Die Anwendung lässt sich leicht ändern und jederzeit zuverlässig überprüfen. |
| **Spezifisch** | Präsentation, Geschäftslogik und Datenzugriff liegen in getrennten Modulen, und der Kalender-Dienst ist hinter einer eigenen Schnittstelle gekapselt. Man kann die Anbindung austauschen und die Anwendung ohne den echten Dienst prüfen. |
| **Messbar** | (a) **0 direkte Zugriffe** der Präsentationsschicht auf die Datenzugriffsschicht (Prüfung durch Code-Review der Abhängigkeiten). (b) Der Kalender-Dienst wird **an genau einer Stelle** im Code aufgerufen (nur in der Implementierung hinter der Schnittstelle). (c) Ein **Austausch** der Implementierung (z. B. echter Dienst gegen Ersatz mit festen Antworten) erfordert **keine Änderung** in der Geschäftslogik. |
| Bezug | NFR-05, NFR-06 |

## 4 Maßnahmen zum Schutz der Testbarkeit

Testbarkeit (Maintainability/Testability nach ISO 25010) heißt: Man kann für das System Prüfkriterien festlegen und Prüfungen leicht durchführen. Folgende **konkrete Maßnahmen** schützen sie in unserem Repository und Prozess:

| # | Maßnahme | Wirkung |
|---|---|---|
| 1 | Der Kalender-Dienst ist hinter einer **Schnittstelle** gekapselt und wird per Übergabe (Dependency Injection) bereitgestellt. | Wir können ihn in Tests durch eine Ersatzimplementierung mit **kontrollierten Antworten** (auch Fehler) ersetzen, ohne den Live-Dienst aufzurufen. |
| 2 | Alle Funktionen sind über die **REST-API** erreichbar (Python FastAPI), unabhängig von der Oberfläche. | Wir können die Anwendungslogik ohne Browser prüfen. |
| 3 | **Drei Schichten** in getrennten Modulen, Zugriffe nur in eine Richtung (Präsentation → Geschäftslogik → Datenzugriff). | Jede Schicht ist einzeln prüfbar, Änderungen bleiben lokal. |
| 4 | **Feste Testdaten** (Referenzbestand aus 3.1) und **kein direkter Zugriff auf die Systemzeit** im Code, das Datum kommt über die Schnittstelle des Kalender-Dienstes. | Ergebnisse sind **wiederholbar** und vom aktuellen Datum unabhängig. |
| 5 | Eine **separate Test-Datenbank** (nicht die Produktionsdaten, gestartet über Docker Compose). | Tests verändern keine echten Daten und sind voneinander unabhängig. |
| 6 | Jede Anforderung hat eine **eindeutige ID** (FR-xx, NFR-xx). | Prüfungen können auf eine Anforderung verweisen, Lücken werden sichtbar. |
| 7 | **Prozess:** Entwicklung auf **Feature-Branches**, **Review durch ein anderes Teammitglied** vor jedem Merge auf `main` (wie in `docs/team.md` vereinbart), eine **Issue je Aufgabe**. Der Test Lead achtet darauf, dass zu neuen Funktionen Tests vorhanden sind. | Fehler werden früh gefunden, niemand merged unreviewed Code. |
| 8 | **Einheitlicher Testbefehl** (`pytest`, im Tech-Stack festgelegt), der **ohne Netzwerkzugriff auf den Kalender-Dienst** läuft. | Jeder im Team kann jederzeit mit einem Befehl prüfen, ob alles funktioniert. |

---


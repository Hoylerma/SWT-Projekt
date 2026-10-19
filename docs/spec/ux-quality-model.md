### Interaktionseffizienz
- **ISO-25010-Merkmal:** Usability, Performance
- **Messbares Kriterium:** Startseite → Rezept mit Zutatenliste ca. 3 Interaktionen. Zutatenfilterung reagiert in ca. 300 ms nach Tastenanschlag - bei 500 (oder wie viel auch immer) Rezepten.
- **Verifikation:** Klick-Zählung im Walkthrough, Antwortzeitmessung im Browser (DevTools)
- **Bezug Lab 2:** NFR-03, NFR-01, quality.md 3.3

### Klarheit / Verständlichkeit
- **ISO-25010-Merkmal:** Usability
- **Messbares Kriterium:** 4 von 5 Testpersonen beantworten „Was fehlt für dieses Rezept?" richtig in ca. 10 s ohne Hilfe. „Vollständig"-Status wird in 5 von 5 Fällen korrekt erkannt.
- **Verifikation:** Szenarioaufgabe mit Stoppuhr, Match zwischen System und menschlichen Verständnis
- **Bezug Lab 2:** FR-10, quality.md 3.3

### Fehlertoleranz & Wiederherstellung
- **ISO-25010-Merkmal:** Usability, Reliability
- **Messbares Kriterium:** Bei 10 definierten Fehleingaben (leere Pflichtfelder, Menge 0, doppelte Zutat usw.) zeigt die App in jedem Fall eine Meldung am betroffenen Feld. Eingegebene Daten bleiben erhalten.
- **Verifikation:** Negativtest-Katalog (manuell + API-Test)
- **Bezug Lab 2:** FR-14, UR-09

### Vertrauen & Transparenz
- **ISO-25010-Merkmal:** Reliability, Functional suitability
- **Messbares Kriterium:** Bei 10 simulierten Dienstausfällen erscheint der Hinweis in jedem Fall sichtbar oberhalb der Trefferliste, ohne technische Fehlertexte.
- **Verifikation:** Mock des Kalender-Dienstes
- **Bezug Lab 2:** FR-13, NFR-02, quality.md 3.2

### Erlernbarkeit
- **ISO-25010-Merkmal:** Usability
- **Messbares Kriterium:** 4 von 5 Erstnutzern erreichen „Rezept mit Zutatenliste öffnen" ohne Hilfe in ca. 2 Minuten.
- **Verifikation:** Beobachtungsprotokoll
- **Bezug Lab 2:** NFR-03, quality.md 3.3

Mit Ki "Bezug lab 2" rausgesucht, Claude Sonnet 5.5

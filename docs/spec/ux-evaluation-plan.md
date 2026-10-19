### 1. Evaluationsumfang
- Faktoren: alle fünf aus `ux-factors.md`.
- Nutzungsabläufe:
  - **1:** Zutaten auswählen → Trefferliste → Rezept öffnen (UC-01/UC-02)
  - **2:** Neues Rezept anlegen, inkl. absichtlicher Fehleingabe
  - **3:** Suche bei ausgefallenem Kalender-Dienst (Mock-Modus)

### 2. Methoden (in ca. 30 Minuten durchführbar)
- Heuristische Evaluation nach Nielsen (10 Heuristiken, 15 Min., pro Prüfer einzeln)
- Cognitive Walkthrough für J1 (10 Min.): „Weiß der Nutzer, was er tun soll? Sieht er die richtige Aktion? Versteht er das Feedback?"
- Szenariobasierter Test für J2/J3 (5 Min.)

### 3. Teilnehmende und Setup
- 2 Prüfende aus einem anderen Team (Studierende passen als WG-nahe Zielgruppe)
- Laptop und Smartphone, Testdaten aus quality.md (Referenzbestand 10 Rezepte), Mock-Schalter für den Kalender-Dienst
- Dauer insgesamt ca. 30 Min., Material: Aufgabenblatt, Befundvorlage, Stoppuhr

### 4. Metriken und Abnahmekriterien

| Metrik | Schwelle |
|---|---|
| Interaktionen bis Rezept (J1) | ≤ 3 |
| Erfolgsquote ohne Hilfe (J1) | ≥ 80 % |
| Zeit bis Rezept geöffnet (J1) | ≤ 2 Min. |
| Fehleingaben mit verständlicher Meldung (J2) | 100 % |
| Ausfallhinweis sichtbar (J3) | 100 % |
| Schwere Befunde (Severity 3–4) | 0 offen |

### 5. Befund-Vorlage

| ID | Beschreibung | Heuristik / Faktor | Schweregrad (0–4) | Nachweis (Screenshot/Beobachtung) | Empfehlung |
|---|---|---|---|---|---|

Schweregrad nach Nielsen: 0 kein Problem · 1 kosmetisch · 2 gering · 3 schwer · 4 Katastrophe.

### 6. Quality Gate
- **Blockiert die Freigabe:** Befund mit Schweregrad 4; Schweregrad 3 in J1 oder J3 (Kernfunktion bzw. Fehlerfall); verfehlte Abnahmeschwelle aus Abschnitt 4.
- **Blockiert nicht:** Schweregrad 0–2 sowie Schweregrad 3 in J2. Als Issue erfassen, nächster Sprint.
- Ein Befund aus dem Gate wird durch Retest derselben Aufgabe geschlossen.
- Verantwortlich: Test Lead, nach Rücksprache mit dem Team (laut `docs/team.md`).

aktuell pur ki schaut mal drüber bin jtz müde

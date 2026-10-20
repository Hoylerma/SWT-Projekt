KI Anwendung: Claude Sonnet 5.5, gesammelte Notizen ausformuliert und inhaltlich mit der Laboraufgabe und den Dokumenten aus Lab 2 abgeglichen.

# UX-Evaluationsplan WG Cook

Der Plan ist für Lab 11 gedacht: **2 Prüfende eines anderen Teams, ca. 30 Minuten**, ein kurzer Szenario-/Walkthrough-/Heuristik-Durchgang statt einer Nutzerstudie. Die Kriterien stammen aus `ux-quality-model.md` und sind dort mit `quality.md` (Lab 2) verknüpft. Die dort für 5 Testpersonen formulierten Schwellen sind hier auf 2 Prüfende skaliert (Abschnitt 4).

## 1 Evaluationsumfang

**Faktoren** (aus `ux-factors.md`): Erlernbarkeit, Klarheit/Verständlichkeit, Vertrauen/Transparenz, Fehlertoleranz/Wiederherstellung, Interaktionseffizienz.

**Nutzungsabläufe (Journeys):**

| ID | Ablauf | Bezug | Faktoren |
|---|---|---|---|
| **J1** | Startseite → Zutaten auswählen → Trefferliste → Rezept mit Zutatenliste öffnen. Aufgabe zusätzlich: „Was fehlt für Rezept X?“ und „Welche Rezepte sind vollständig?“ | UC-01, UC-02, FR-07 bis FR-10 | Erlernbarkeit, Klarheit, Interaktionseffizienz |
| **J2** | Neues Rezept anlegen, mit 5 absichtlichen Fehleingaben (Name leer, Menge 0, doppelte Zutat, Einheit fehlt, Portionszahl 21) | FR-01, FR-02, FR-14, UR-09 | Fehlertoleranz |
| **J3** | Suche bei ausgefallenem Kalender-Dienst (Mock: Timeout, Fehlerantwort, ungültige Antwort) | FR-13, NFR-02, UC „Saison ermitteln“ 3a | Vertrauen |

**Geräte:** Prüfer A auf dem Laptop, Prüfer B auf dem Smartphone (Breite 360 px, NFR-04, UR-08). Dadurch wird J1 auf beiden Geräteklassen abgedeckt.

**Nicht im Umfang:** Barrierefreiheit (kein ausgewählter Faktor), Last-/Langzeittests (NFR-01, wird vom Team vorab gemessen, siehe Abschnitt 4).

## 2 Methoden

Reihenfolge ist wichtig: Erst die ungeführten Aufgaben, dann die Analyse, sonst kennen die Prüfenden die App schon.

| Schritt | Methode | Dauer | Wer |
|---|---|---|---|
| 1 | Einführung (nur Kontext „WG, Kühlschrank“, **keine** Bedienerklärung) | 2 Min. | Moderation |
| 2 | **Szenariobasierter Test J1** mit Stoppuhr, Think-Aloud, ohne Hilfe | 5 Min. | beide einzeln |
| 3 | **Szenariobasierter Test J2 und J3** (J3 über Mock-Schalter) | 8 Min. | beide einzeln |
| 4 | **Cognitive Walkthrough J1** je Schritt: „Weiß der Nutzer, was er tun soll? Sieht er die richtige Aktion? Versteht er das Feedback?“ | 5 Min. | beide gemeinsam |
| 5 | **Heuristische Evaluation nach Nielsen** (10 Heuristiken, freie Erkundung) | 8 Min. | beide einzeln |
| 6 | Befunde zusammenführen, Schweregrad festlegen | 2 Min. | beide gemeinsam |

Gesamt ca. 30 Min. Die Moderation notiert nur, greift nicht ein. Hilfe gilt als „Hilfe gegeben“ und zählt als Misserfolg der Aufgabe.

## 3 Teilnehmende und Setup

- **2 Prüfende** eines anderen Teams. Studierende passen zur Zielgruppe (WG-Mitglieder), kennen WG Cook aber nicht.
- **Geräte:** Laptop (aktueller Chrome, Firefox oder Edge) und Smartphone.
- **Testdaten:** Referenzbestand mit 10 Rezepten aus `quality.md` 3.1, feste Zutatenauswahl für J1 (vom Team vorab festgelegt, erwartete Trefferliste von Hand ermittelt). Mindestens ein Rezept ist bei dieser Auswahl „vollständig“.
- **Kalender-Dienst:** Ersatzimplementierung mit festen Antworten (`quality.md` Maßnahme 1 und 4), Schalter für: *normal*, *Timeout > 2 s*, *Fehlerantwort*, *ungültige Antwort*. Der Live-Dienst wird nicht benutzt, das Datum ist fest.
- **Material:** Aufgabenblatt (J1 bis J3 ohne Bedienhinweise), Befundvorlage (Abschnitt 5), Stoppuhr, Beobachtungsprotokoll (je Prüfer: Hilfe ja/nein, Zeit, Interaktionen).

## 4 Metriken und Abnahmekriterien

Gemessen pro Prüfenden und Aufgabe. Die Schwellen entsprechen den Kriterien in `ux-quality-model.md`. Wo dort „4 von 5“ steht, gilt hier **2 von 2**, weil bei 2 Prüfenden 80 % nicht erreichbar sind. Eine größere Studie mit 5 Testpersonen verwendet die Originalwerte.

| # | Metrik | Faktor | Schwelle | Messung | Bezug |
|---|---|---|---|---|---|
| M1 | Aufgabe J1 ohne Hilfe geschafft | Erlernbarkeit | 2 von 2 | Beobachtung | NFR-03, quality 3.3 |
| M2 | Zeit Startseite → Rezept mit Zutatenliste | Erlernbarkeit | ≤ 2 Min. | Stoppuhr | NFR-03 |
| M3 | Interaktionen Startseite → Rezept (Klicks/Eingaben) | Interaktionseffizienz | ≤ 3 | Zählung | NFR-03, quality 3.3 |
| M4 | „Was fehlt für Rezept X?“ richtig beantwortet | Klarheit | 2 von 2, je ≤ 10 s | Stoppuhr | FR-10 |
| M5 | Von 3 vorgegebenen Treffern (davon 1 vollständig) „vollständig“ korrekt erkannt | Klarheit | 100 % (6 von 6) | Beobachtung | FR-10 |
| M6 | Fehleingabe zeigt Meldung **am betroffenen Feld** und Eingaben bleiben erhalten | Fehlertoleranz | 5 von 5 Fehleingaben | Beobachtung | FR-14, UR-09 |
| M7 | Ausfallhinweis „Saisonale Sortierung ist gerade nicht verfügbar“ sichtbar **oberhalb der Trefferliste**, ohne technischen Fehlertext, Trefferliste trotzdem vorhanden | Vertrauen | 3 von 3 Ausfallvarianten | Beobachtung | FR-13, NFR-02, quality 3.2 |
| M8 | Suchergebnis bei Ausfall nach höchstens | Vertrauen | ≤ 3 Sek. | Stoppuhr / DevTools | quality 3.2 (b) |
| M9 | Liste von Rezepten stimmt mit der von Hand ermittelten Erwartung überein (Reihenfolge, Abdeckung, fehlende Zutaten) | Klarheit / Funktionale Eignung | 100 % | Vergleich mit Erwartung | FR-08 bis FR-10, quality 3.1 |
| M10 | Bedienbar bei 360 px Breite ohne horizontales Scrollen auf der Hauptseite | Erlernbarkeit | erfüllt | Smartphone | NFR-04 |
| M11 | Offene Befunde mit Schweregrad 4 | alle | 0 | Befundliste | Abschnitt 6 |
| M12 | Offene Befunde mit Schweregrad ≥ 3 in J1 oder J3 | alle | 0 | Befundliste | Abschnitt 6 |

**Vom Team vorab zu messen (nicht von den Prüfenden):** Zutatenfilter reagiert ≤ 300 ms nach Tastenanschlag (DevTools, auf dem Laptop, mit Testbestand von 500 Rezepten, falls bis Lab 11 vorhanden, sonst mit Referenzbestand). Ergebnis wird in den Plan-Lauf eingetragen.

## 5 Befund-Vorlage

| ID | Journey / Schritt | Beschreibung des Problems | Heuristik / Faktor | Schweregrad (0–4) | Nachweis | Empfehlung |
|---|---|---|---|---|---|---|
| F-01 | | | | | Screenshot, Zeit, Zitat | |

Schweregrad nach Nielsen (Häufigkeit, Auswirkung, Persistenz):

| Grad | Bedeutung | Beispiel bei WG Cook |
|---|---|---|
| 0 | kein Problem | |
| 1 | kosmetisch | Abstand uneinheitlich |
| 2 | gering | Label missverständlich, Ziel trotzdem erreichbar |
| 3 | schwer | Rezept nur mit Hilfe auffindbar, Hinweis bei Ausfall fehlt |
| 4 | Katastrophe | Absturz oder Fehlerseite bei Dienstausfall, Datenverlust beim Speichern |

Jeder Befund nennt genau eine ID, eine Journey, einen Nachweis und eine konkrete Empfehlung. Befunde ohne Nachweis gelten als nicht bestätigt.

## 6 Qualitätsgate

**Vorbedingung (Testbarkeit, sonst findet die Evaluation nicht statt):**
- Der einheitliche Testbefehl (`pytest`) läuft grün und ohne Netzwerk zum Kalender-Dienst (`quality.md` Maßnahme 8).
- Mock-Schalter und Referenzbestand aus Abschnitt 3 sind vorhanden. Ohne sie sind M7 bis M9 nicht reproduzierbar.

**Blockiert die Freigabe:**
- Befund mit Schweregrad 4 (M11).
- Befund mit Schweregrad 3 in J1 (Kernfunktion) oder J3 (Fehlerfall) (M12).
- Eine verfehlte Schwelle bei M1, M3, M6, M7 oder M9. Diese stehen für die Qualitätsziele aus `quality.md` (Funktionale Eignung, Zuverlässigkeit, Benutzbarkeit).

**Blockiert nicht:** Schweregrad 0 bis 2 sowie Schweregrad 3 in J2. Als Issue erfassen, Bearbeitung im nächsten Sprint. Verfehlte Schwellen M2, M4, M5, M8 und M10 werden als Befund mit mindestens Schweregrad 2 erfasst und mit dem Team entschieden.

**Ablauf:**
1. Befund wird als Issue angelegt, Schweregrad und Journey stehen im Titel.
2. Ein Gate-Befund gilt erst nach einem **Retest derselben Aufgabe** als geschlossen.
3. Entscheidung über Freigabe: Test Lead nach Rücksprache mit dem Team (laut `docs/team.md`).

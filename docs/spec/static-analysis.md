# Statische Codeanalyse (Lab 6.3)

Geprüft wird das Backend von WG Cook (`backend/`, Python 3.12, FastAPI, SQLAlchemy, behave): Anwendungscode in `app/`, Tests, Stubs und Step-Definitionen in `tests/` sowie `run_tests.py`. Das sind 20 Python-Dateien mit rund 500 Codezeilen ohne Kommentare und Leerzeilen. Das Frontend ist in Lab 6 noch ein Skelett ohne eigene Logik und wird daher nicht geprüft.

## 1. Gewählte Kategorien und Werkzeuge

| Kategorie | Werkzeug | Version | Konfiguration |
|---|---|---|---|
| Linter | Pylint | 4.1 | `backend/pyproject.toml`, Abschnitt `[tool.pylint.*]` |
| Stil-/Formatprüfer | ruff format | 0.17 | `backend/pyproject.toml`, Abschnitt `[tool.ruff]` |

### Begründung

**Linter (Pylint):** WG Cook hat seine Logik vor allem in `rezept_service.py`. Dort werden Eingaben geprüft, Treffer nach Zutatenabdeckung bewertet und sortiert, und es gibt eine Grenze zur externen Abhängigkeit, dem Kalender-Dienst (`kalender.py`). Fehler in diesen Bereichen fallen in Python oft erst zur Laufzeit auf, weil es keinen Compiler gibt. Ein Linter findet typische Fehlerquellen schon vorher, zum Beispiel unbenutzte Argumente, falsch aufgerufene Funktionen, fehlende Fehlerbehandlung bei `subprocess` oder zu komplexe Funktionen. Pylint analysiert auch Importe aus FastAPI und SQLAlchemy mit und bewertet den Code zusätzlich mit einer Note von 0 bis 10. Dadurch sind Verbesserungen messbar.

**Formatprüfer (ruff format):** Fünf Personen arbeiten am selben Code, teilweise mit KI-Unterstützung und mit verschiedenen Editoren. Vor Lab 6 gab es deshalb unterschiedliche Stile: Leerzeichen am Zeilenende, fehlende Zeilenumbrüche am Dateiende und von Hand ausgerichtete Kommentare. Ein Formatierer macht den Stil automatisch einheitlich. Dadurch bestehen Pull Requests nur noch aus inhaltlichen Änderungen und nicht mehr aus Leerzeichen-Diffs, was auch Reviews wie in Lab 6.1 erleichtert. ruff ist sehr schnell (unter einer Sekunde) und eignet sich deshalb als Prüfung in der CI in Lab 9.

Beide Werkzeuge stammen aus verschiedenen Kategorien und ergänzen sich: ruff kümmert sich nur um das Aussehen, Pylint um die inhaltliche Qualität. Die Kategorien wurden aus der Tabelle in der Aufgabe zu Lab 6 übernommen und passen zu unserem Python-Stack.

**Code-Coverage** ist eine dynamische Technik, weil die Tests dafür ausgeführt werden müssen. Sie zählt deshalb nicht als eines der beiden Werkzeuge. Ergänzend wäre sie trotzdem sinnvoll, um zu sehen, welche Zweige von `rezept_service.py` die Unit- und BDD-Tests nicht abdecken.

## 2. Konfiguration und Entscheidungen

Grundsatz: Standardwerte und nur wenige projektspezifische Regeln. Die Konfiguration liegt in `backend/pyproject.toml`.

| Einstellung | Wert | Begründung |
|---|---|---|
| Pylint `disable` | `missing-*-docstring`, `too-few-public-methods` | Docstrings sind im Team nicht vereinbart. Kleine Datenklassen (z. B. `RezeptEingabe`) und Stubs haben bewusst wenige Methoden. |
| Pylint `max-line-length` | 100 | Pylint-Standard, wird ausdrücklich gesetzt, damit er zu ruff passt |
| ruff `line-length` | 100 | Der Standard von ruff wäre 88. Ohne Angleichung würden ruff und Pylint unterschiedliche Zeilenlängen verlangen. |
| ruff `indent-style` | `space` | Ursprünglich stand hier `tab`. Der gesamte Code ist aber mit 4 Leerzeichen eingerückt (PEP 8), und mit `tab` hätte ruff 19 von 20 Dateien komplett umformatiert. |
| ruff `quote-style` | `double` | entspricht dem bestehenden Code |
| `# pylint: disable=not-callable` | nur in den drei Step-Dateien in `tests/features/steps/` | Falsch-Positiv, siehe Abschnitt 4. Die Regel bleibt für den Rest des Codes aktiv, deshalb wird sie nicht global abgeschaltet. |

## 3. Lokale Ausführung

Einmalig einrichten (im Ordner `backend/`):

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt      # enthält pylint und ruff
```

Prüfen:

```bash
ruff format --check .                    # meldet nur, welche Dateien nicht formatiert sind
ruff format --diff .                     # zeigt die Änderungen, ohne sie anzuwenden
ruff format .                            # formatiert alle Dateien automatisch

pylint app tests run_tests.py            # Linter mit Note 0–10
```

Erwartete Ausgabe auf einem sauberen Stand:

```text
$ ruff format --check .
20 files already formatted

$ pylint app tests run_tests.py
Your code has been rated at 10.00/10
```

## 4. Ergebnisse

### Erster Lauf (Ausgangszustand, ursprüngliche Konfiguration)

**ruff format:** 19 von 20 Dateien wären umformatiert worden, fast nur wegen der Einstellung `tab`. Nach der Umstellung auf `space` und Zeilenlänge 100 blieben **14 Dateien** mit echten Abweichungen übrig:
- Leerzeichen am Zeilenende und fehlender Zeilenumbruch am Dateiende
- von Hand ausgerichtete Kommentare in `rezept_service.py`
- eine Docstring-Zeile mit überflüssigem Umbruch in `kalender.py`
- fehlende Leerzeile nach Modul-Docstrings

**Pylint: Note 6,12 / 10** mit 51 Meldungen:

| Anzahl | Meldung | Bewertung |
|---:|---|---|
| 25 | `E1102 not-callable` (`given/when/then is not callable`) | **Falsch-Positiv** |
| 12 | `C0303 trailing-whitespace` | echt, nur Stil |
| 9 | `C0304 missing-final-newline` | echt, nur Stil |
| 1 | `C0305 trailing-newlines` | echt, nur Stil |
| 1 | `C0301 line-too-long` (Step-Definition, 105 Zeichen) | echt, nur Stil |
| 2 | `W0613 unused-argument` (`scenario` in `environment.py`) | echt, harmlos |
| 1 | `W1510 subprocess-run-check` (`run_tests.py`) | echt, sinnvoller Hinweis |

### Maßnahmen

1. `ruff format .` ausgeführt: 14 Dateien formatiert. Damit waren auch alle 22 Pylint-Meldungen zu Leerzeichen und Zeilenenden erledigt (Note danach 6,68).
2. **Falsch-Positiv E1102:** Die Decorators `given`, `when` und `then` von behave sind Objekte einer Klasse mit `__call__`-Methode. Zur Laufzeit funktionieren sie, Pylint kann das bei der statischen Analyse aber nicht erkennen. Die Regel wird deshalb nur in den drei Step-Dateien mit Kommentar und Begründung abgeschaltet.
3. `unused-argument`: Die Hook-Parameter in `environment.py` heißen jetzt `_scenario`. Behave übergibt sie per Position, sie werden also weiterhin gebraucht, aber das Unterstrich-Präfix zeigt, dass sie bewusst nicht genutzt werden.
4. `subprocess-run-check`: In `run_tests.py` steht jetzt `check=False` mit Kommentar, weil der Rückgabecode direkt danach selbst geprüft wird.
5. Die zu lange Gherkin-Schrittzeile wurde in zwei Strings aufgeteilt, die Python automatisch zusammenfügt. Das Verhalten bleibt gleich.

### Endstand

| Werkzeug | Vorher | Nachher |
|---|---|---|
| ruff format | 14 von 20 Dateien nicht formatiert | 20 von 20 formatiert |
| Pylint | 6,12 / 10, 51 Meldungen | **10,00 / 10**, 0 Meldungen |
| Tests (`python run_tests.py`) | grün | grün: 18 pytest-Tests, 6 BDD-Szenarien |

Alle Änderungen betreffen nur Formatierung und Stil. Die Programmlogik wurde nicht verändert, was die unverändert grüne Testsuite bestätigt.

## 5. Bewertung

**Nutzen für Codequalität und Fehlervermeidung**
- ruff hat den uneinheitlichen Stil aus mehreren Labs und von mehreren Personen in einem Schritt vereinheitlicht. Das hat keine Fehler verhindert, macht aber Diffs und Reviews deutlich übersichtlicher. Formatierung muss im Review nicht mehr diskutiert werden.
- Pylint hat in unserem kleinen Code keinen echten Laufzeitfehler gefunden. Der Hinweis zu `subprocess.run` ohne `check` ist aber genau die Art Fehlerquelle, die ein Linter früh aufdecken soll: Ein vergessener Rückgabecode führt dazu, dass ein Testlauf grün meldet, obwohl er fehlgeschlagen ist. In `run_tests.py` war das schon richtig gelöst, jetzt ist es ausdrücklich gekennzeichnet.
- Der größere Nutzen kommt erst noch: In Lab 7–11 wachsen API, Persistenz und die Anbindung an den Kalender-Dienst. Dann helfen Regeln wie unbenutzte Variablen, nicht erreichbarer Code oder zu viele Verzweigungen mehr als jetzt.

**Rauschen und Falsch-Positive**
- Im ersten Lauf war fast die Hälfte der Pylint-Meldungen (25 von 51) falsch-positiv, nämlich das behave-Problem. Weil Pylint diese als Fehler (`E`) wertet, lag die Note bei nur 6,12, obwohl der Code funktioniert. Ohne Einordnung wirkt das abschreckend und kann dazu führen, dass das Team die Ausgabe ignoriert. Eine gezielte Ausnahme pro Datei mit Begründung ist deshalb besser als eine globale Abschaltung.
- Die meisten übrigen Meldungen waren reine Stilfragen, die ruff ohnehin behebt. Pylint und ruff überschneiden sich hier. Wenn zuerst ruff läuft, bleiben für Pylint nur noch inhaltliche Meldungen übrig.
- Bei ruff gab es kein Rauschen. Die Ausgabe ist eindeutig, und `ruff format .` behebt alles automatisch. Einzige Falle war die anfänglich falsche Konfiguration (`tab`), die fast jede Datei als fehlerhaft gemeldet hätte.

**Was wir (noch) nicht in die CI-Pipeline übernehmen würden**
- **ruff format --check** wird in Lab 9 die CI-Prüfung: Es ist schnell, liefert eindeutige Ergebnisse und erzeugt keine Falsch-Positive.
- **Pylint** würden wir vorerst nicht als harte Prüfung einbauen, die einen Pull Request blockiert, weil es langsam ist und Falsch-Positive bei Bibliotheken wie behave liefert. Denkbar ist es später mit einer Mindestnote, z. B. `pylint --fail-under=9`, sobald sich die Konfiguration bewährt hat.

## KI-Nutzung

Claude Code (Modell Claude Opus 5.5) wurde für Lab 6.3 genutzt. Es hat eine erste Fassung dieses Dokuments geschrieben (Formulierungen anhand der Ergebnisse für ein übersichtliches Dokument). 

### Begriffe

| Begriff                  | Bedeutung                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rezept**               | Primärentität. Besteht aus Name, Beschreibung, Portionszahl, optionalen Zubereitungsschritten, einer Saison-Zuordnung und mindestens einer Zutatenzeile. |
| **Zutat / Zutatenzeile** | Kind-Entität eines Rezepts: Zutatenname, Menge und Einheit. Ein Rezept hat eine bis viele Zutatenzeilen, jede Zutatenzeile gehört genau zu einem Rezept. |
| **Auswahl**              | Die Zutaten, die ein WG-Mitglied für eine Suche als "vorhanden" markiert. Sie gilt nur für die aktuelle Suche und wird nicht dauerhaft gespeichert.      |
| **Abdeckung**            | Anteil der Zutaten eines Rezepts, die in der Auswahl enthalten sind (Anzahl abgedeckter Zutaten geteilt durch Gesamtzahl der Zutaten des Rezepts).       |
| **Saison**               | Frühling, Sommer, Herbst oder Winter. Jedes Rezept ist einer Saison oder "ganzjährig" zugeordnet.                                                        |
| **Kalender-Dienst**      | Externe Abhängigkeit. Liefert das aktuelle Datum, aus dem das System die aktuelle Saison ableitet.                                                       |
|                          |                                                                                                                                                          |

## 2 User Requirements (Problemraum)


| ID    | Anforderung                                                                                                                       | Nutzen                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| UR-01 | Als WG-Mitglied möchte ich angeben, welche Zutaten vorhanden sind, und Rezepte finden, die ich damit kochen kann.                 | Wir müssen nicht lange überlegen oder suchen.                         |
| UR-02 | Als WG-Mitglied möchte ich ein Rezept mit allen Zutaten und Mengen ansehen.                                                       | Wir wissen, was wir brauchen.                                         |
| UR-03 | Als WG-Mitglied möchte ich sehen, welche Zutaten für ein Rezept noch fehlen.                                                      | Wir entscheiden, ob wir es kochen oder noch etwas besorgen.           |
| UR-04 | Als WG-Mitglied möchte ich, dass saisonal passende Rezepte bevorzugt vorgeschlagen werden.                                        | Die Vorschläge passen zur Jahreszeit.                                 |
| UR-05 | Als WG-Mitglied möchte ich den Rezeptbestand pflegen (Rezepte anlegen, ändern, löschen).                                          | Die Anwendung enthält die Rezepte, die wir wirklich kochen.           |
| UR-06 | Als WG möchten wir die Anwendung gemeinsam und ohne Anmeldung nutzen.                                                             | Kein Aufwand durch Konten, jede Person sieht denselben Rezeptbestand. |
| UR-07 | Als WG-Mitglied möchte ich die Anwendung am Laptop und am Smartphone nutzen.                                                      | Wir benutzen sie in der Küche mit dem Handy.                          |
| UR-08 | Als WG-Mitglied möchte ich verständliche Rückmeldungen bei falschen Eingaben und wenn ein Teil der Anwendung nicht verfügbar ist. | Wir wissen, was wir tun müssen und die Anwendung bleibt benutzbar.    |

## 3 System Requirements (Lösungsraum)

### 3.1 Funktionale Anforderungen


| ID | Anforderung | Herleitung | Prio |
|---|---|---|---|
| FR-01 | Das System ermöglicht, ein **Rezept anzulegen** mit: Name (Pflicht, 1 bis 100 Zeichen), Portionszahl (Pflicht, ganze Zahl von 1 bis 20), Beschreibung (optional, höchstens 2000 Zeichen), Zubereitungsschritte (optional, höchstens 5000 Zeichen), Saison (Frühling, Sommer, Herbst, Winter oder ganzjährig, Standard ganzjährig) und **mindestens einer Zutatenzeile**. | UR-05 | Must |
| FR-02 | Eine **Zutatenzeile** besteht aus Zutatenname (Pflicht, 1 bis 60 Zeichen), Menge (Pflicht, Zahl größer 0 und höchstens 99999) und Einheit (Pflicht, aus der Liste g, kg, ml, l, Stück, EL, TL). Ein Zutatenname darf in einem Rezept **nur einmal** vorkommen (Groß-/Kleinschreibung wird nicht unterschieden). | UR-02, UR-05 | Must |
| FR-03 | Das System zeigt die **Liste aller Rezepte** (alphabetisch nach Name) und ein einzelnes Rezept mit **allen Details und allen Zutatenzeilen**. | UR-02 | Must |
| FR-04 | Das System ermöglicht, an einem bestehenden Rezept Zutatenzeilen **hinzuzufügen und zu entfernen** sowie die Rezeptdaten zu ändern. Ein Rezept muss mindestens eine Zutatenzeile behalten. | UR-05 | Should |
| FR-05 | Das System ermöglicht, ein Rezept zu **löschen**. Die zugehörigen Zutatenzeilen werden mitgelöscht. | UR-05 | Should |
| FR-06 | Das System bietet eine **Zutatenauswahl**: Der Nutzer kann eine oder mehrere Zutaten markieren. Zur Auswahl stehen alle im System bekannten Zutatennamen (aus den Zutatenzeilen aller Rezepte), mit Suche nach Teiltext. | UR-01 | Must |
| FR-07 | Das System ermittelt zu einer Auswahl für **jedes Rezept die Abdeckung** und liefert alle Rezepte mit Abdeckung größer 0. Rezepte ohne eine einzige ausgewählte Zutat werden nicht angezeigt. | UR-01 | Must |
| FR-08 | Das System **sortiert** die Treffer in dieser Reihenfolge: (1) Abdeckung absteigend, (2) bei gleicher Abdeckung zuerst Rezepte der **aktuellen Saison**, danach ganzjährige, danach Rezepte anderer Saisons, (3) alphabetisch nach Name. | UR-01, UR-04 | Must |
| FR-09 | Das System zeigt je Treffer an, **wie viele Zutaten abgedeckt sind** (z. B. "3 von 5") und **welche Zutaten fehlen**. Rezepte mit Abdeckung 100 % werden als **"vollständig"** gekennzeichnet. | UR-03 | Must |
| FR-10 | Das System ermittelt die **aktuelle Saison** über den **externen Kalender-Dienst**. Aus dem gelieferten Datum wird die Saison abgeleitet: Dezember bis Februar Winter, März bis Mai Frühling, Juni bis August Sommer, September bis November Herbst. | UR-04 | Should |
| FR-11 | Die vom Kalender-Dienst gelieferte Saison wird **zwischengespeichert** (höchstens 24 Stunden), damit der Dienst nicht bei jeder Suche aufgerufen wird. | UR-04 | Should |
| FR-12 | Antwortet der Kalender-Dienst **nicht innerhalb von 2 Sekunden**, liefert er einen Fehler oder eine **ungültige Antwort**, wird die Suche **ohne Saison-Bevorzugung** (Sortierung nach FR-08 ohne Punkt 2) fortgesetzt. Das System zeigt einen **sichtbaren Hinweis** ("Saisonale Sortierung ist gerade nicht verfügbar"). Es gibt **keinen Abbruch und keine Fehlerseite**, und es wird **nichts doppelt gespeichert**. | UR-04, UR-08 | Must |
| FR-13 | Das System **prüft alle Eingaben** (Pflichtfelder, Längen, Wertebereiche aus FR-01 und FR-02) und lehnt ungültige Eingaben mit einer **verständlichen Meldung** ab. Der Datenbestand bleibt dabei unverändert. Wird ein nicht vorhandenes Rezept aufgerufen, zeigt das System die Meldung "Rezept nicht gefunden". | UR-08 | Must |
| FR-14 | Mehrere Nutzer können **gleichzeitig** mit demselben gemeinsamen Rezeptbestand arbeiten. Es gibt **keine Benutzerkonten und keine Anmeldung**. | UR-06 | Must |

### 3.2 Nicht-funktionale Anforderungen

| ID | Anforderung | ISO-25010-Merkmal | Prio | Messung / Prüfung |
|---|---|---|---|---|
| NFR-01 | Die **Rezeptsuche** (FR-06 bis FR-09) antwortet bei **20 gleichzeitigen Nutzern** und einem Bestand von bis zu **500 Rezepten** in **95 % der Anfragen innerhalb von 1 Sekunde**. | Performance efficiency (Time behavior) | Should | Messung der Antwortzeit bei parallelen Anfragen |
| NFR-02 | Fällt der Kalender-Dienst aus, bleiben **alle übrigen Funktionen** (FR-01 bis FR-09, FR-13) **uneingeschränkt** nutzbar. Die Suche liefert auch dann ein Ergebnis (FR-12). | Reliability (Fault tolerance) | Must | simulierter Ausfall des Dienstes, Ergebnis prüfen |
| NFR-03 | Ein Nutzer ohne Einweisung findet innerhalb von **höchstens 3 Interaktionen** (Klicks oder Eingaben) von der Startseite ein passendes Rezept mit Zutatenliste. | Usability (Learnability, Operability) | Should | Beobachtung von Testpersonen |
| NFR-04 | Die Anwendung funktioniert in den **aktuellen Versionen von Chrome, Firefox und Edge** sowie in **Smartphone-Browsern** und ist ab einer Bildschirmbreite von **360 px** bedienbar. | Compatibility, Portability | Should | manuelle Prüfung in den Browsern |
| NFR-05 | Die Anwendung besteht aus **drei getrennten Schichten** (Präsentation, Geschäftslogik, Datenzugriff) in getrennten Modulen. Die Präsentationsschicht greift nicht direkt auf die Datenzugriffsschicht zu. | Maintainability (Modularity) | Must | Code-Review der Abhängigkeiten |
| NFR-06 | Der Zugriff auf den Kalender-Dienst ist **hinter einer eigenen Schnittstelle gekapselt** und lässt sich durch eine andere Implementierung ersetzen, ohne die Geschäftslogik zu ändern. | Maintainability (Modifiability, Testability) | Must | Code-Review, Austausch der Implementierung |
| NFR-07 | Die Anwendung speichert **keine personenbezogenen Daten**. Alle Eingaben werden validiert, Datenbankzugriffe erfolgen **parametrisiert**. Im Betrieb ist die Verbindung **HTTPS**-gesichert. | Security | Should | Review, Prüfung der Datenbankzugriffe |
| NFR-08 | Die Anwendung lässt sich **mit einem Befehl** (`docker compose up`) lokal starten. | Portability (Installability) | Should | frischer Checkout, Start ausprobieren |

## 4 Workflows

### 4.1 Primärentität Rezept und Kind-Entität Zutat

- **Rezept anlegen:** Der Nutzer gibt Rezeptdaten und mindestens eine Zutatenzeile ein, das System prüft (FR-13) und speichert Rezept und Zutatenzeilen gemeinsam. Bei einem Fehler wird nichts gespeichert.
- **Rezept ansehen:** Das System lädt das Rezept mit allen Zutatenzeilen und zeigt sie an (FR-03).
- **Rezept ändern:** Der Nutzer ändert Rezeptdaten oder fügt Zutatenzeilen hinzu oder entfernt sie (FR-04). Das Rezept behält mindestens eine Zutatenzeile.
- **Rezept löschen:** Das System löscht das Rezept und alle zugehörigen Zutatenzeilen (FR-05).

Die Beziehung ist **1 zu n**: ein Rezept hat mehrere Zutatenzeilen, eine Zutatenzeile gehört zu genau einem Rezept. Die Abdeckung eines Rezepts (FR-07) ergibt sich aus seinen Zutatenzeilen.

### 4.2 Rezeptfindung (Hauptablauf)

1. Der Nutzer wählt die vorhandenen Zutaten aus (FR-06).
2. Das System berechnet für jedes Rezept die Abdeckung (FR-07).
3. Das System ermittelt die aktuelle Saison über den Kalender-Dienst (FR-10, FR-11).
4. Das System sortiert die Treffer nach FR-08 und zeigt je Treffer abgedeckte und fehlende Zutaten (FR-09).
5. Der Nutzer öffnet ein Rezept und sieht alle Zutaten (FR-03).

### 4.3 Interaktion mit der externen Abhängigkeit (Kalender-Dienst)

- **Wofür:** Der Dienst liefert das aktuelle Datum, aus dem das System die Saison ableitet und saisonal passende Rezepte bevorzugt (FR-08, FR-10).
- **Wann:** Bei einer Suche, wenn keine gültige zwischengespeicherte Saison vorliegt (FR-11).
- **Fehlerfall:** Antwortet der Dienst nicht, fehlerhaft oder zu spät, läuft die Suche ohne Saison-Bevorzugung weiter und der Nutzer sieht einen Hinweis (FR-12, NFR-02).
- **Warum der Dienst nicht in jedem automatisierten Test live aufgerufen werden soll:** Sein Ergebnis hängt vom Datum ab und ist damit **nicht deterministisch**, er braucht eine **Netzwerkverbindung**, und ein einziger Aufruf genügt, weil sich die Saison nur viermal im Jahr ändert. In automatisierten Tests wird er deshalb durch eine Ersatzimplementierung mit **kontrollierten Antworten** ersetzt (auch für Fehlerfälle). Das ist durch die Kapselung in NFR-06 möglich.




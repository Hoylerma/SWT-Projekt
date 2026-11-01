Feature: Rezepte anhand vorhandener Zutaten finden
  Als WG-Mitglied möchte ich angeben, welche Zutaten vorhanden sind,
  und die dazu passenden Rezepte mit den fehlenden Zutaten sehen.
  (UC-01, UC-02, FR-07 bis FR-10, UR-01, UR-03)

  Background:
    Given der Rezeptbestand enthält diese Rezepte:
      | Rezept             | Saison     | Zutaten                                 |
      | Tomatensalat       | Sommer     | Tomate, Zwiebel, Olivenöl               |
      | Spaghetti Pomodoro | Sommer     | Spaghetti, Tomate, Basilikum, Knoblauch |
      | Kürbissuppe        | Herbst     | Kürbis, Zwiebel, Sahne                  |
      | Linseneintopf      | Winter     | Linsen, Zwiebel, Karotte                |
      | Rührei             | ganzjährig | Ei, Butter, Salz                        |
    And der Kalender-Dienst liefert als Datum den "2026-07-15"

  Scenario: Trefferliste nach Abdeckung sortiert, mit fehlenden Zutaten
    When ich die Zutaten "Tomate, Zwiebel, Olivenöl" auswähle
    And ich die Rezepte suche
    Then lautet die Trefferliste in dieser Reihenfolge:
      | Rezept             | Abdeckung | Fehlende Zutaten                |
      | Tomatensalat       | 3 von 3   |                                 |
      | Kürbissuppe        | 1 von 3   | Kürbis, Sahne                   |
      | Linseneintopf      | 1 von 3   | Linsen, Karotte                 |
      | Spaghetti Pomodoro | 1 von 4   | Spaghetti, Basilikum, Knoblauch |
    And das Rezept "Tomatensalat" ist als "vollständig" gekennzeichnet
    And das Rezept "Kürbissuppe" ist nicht als "vollständig" gekennzeichnet
    And das Rezept "Rührei" ist nicht in der Trefferliste

  Scenario: Die Suche verändert den Rezeptbestand nicht
    When ich die Zutaten "Tomate" auswähle
    And ich die Rezepte suche
    Then enthält der Rezeptbestand weiterhin 5 Rezepte

  Scenario: Kein Rezept enthält eine ausgewählte Zutat
    When ich die Zutaten "Schokolade" auswähle
    And ich die Rezepte suche
    Then ist die Trefferliste leer
    And die Meldung lautet "Keine passenden Rezepte gefunden"

  Scenario: Suche ohne Auswahl wird abgelehnt
    When ich keine Zutat auswähle
    And ich die Rezepte suche
    Then wird die Suche abgelehnt
    And die Meldung lautet "Bitte mindestens eine Zutat auswählen"

  Scenario: Ein Treffer lässt sich mit allen Zutaten öffnen
    Given ich habe die Zutaten "Tomate, Zwiebel" ausgewählt und gesucht
    When ich das Rezept "Tomatensalat" öffne
    Then sehe ich die Zutaten "Tomate, Zwiebel, Olivenöl" mit Menge und Einheit

  Scenario: Ein nicht vorhandenes Rezept wird gemeldet
    When ich ein Rezept mit der Nummer 9999 öffne
    Then lautet die Meldung "Rezept nicht gefunden"

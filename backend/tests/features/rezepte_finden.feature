Feature: Rezepte anhand vorhandener Zutaten finden

  Szenario: Bei keiner Zutatenangabe wir das WG Mitglied mit einer Fehlermeldung
  darauf hingewiesen, dass mindestens 1 Zutat angegeben werden muss
    Given ein WG Mitglied möchte Rezepte anhand angegebener Zutaten sehen
    When das WG Mitglied keine Zutat auswählt 
    Then wird eine Fehlermeldung ausgegeben

  Szenario: Ein Treffer lässt sich mit allen Zutaten öffnen
    Given ein WG Mitglied hat die Zutaten "Tomate, Zwiebel" ausgewählt und gesucht
    When das WG Mitglied das Rezept "Tomatensalat" öffnet
    Then sieht das WG Mitglied die Zutaten "Tomate, Zwiebel, Olivenöl" mit Menge und Einheit

  Beispiele:
      | Rezept             | Saison     | Zutaten                                 |
      | Tomatensalat       | Sommer     | Tomate, Zwiebel, Olivenöl               |
      | Spaghetti Pomodoro | Sommer     | Spaghetti, Tomate, Basilikum, Knoblauch |
      | Kürbissuppe        | Herbst     | Kürbis, Zwiebel, Sahne                  |
      | Linseneintopf      | Winter     | Linsen, Zwiebel, Karotte                |
      | Rührei             | ganzjährig | Ei, Butter, Salz                        |
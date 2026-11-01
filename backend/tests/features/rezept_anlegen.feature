Feature: Rezept anlegen
  Als WG-Mitglied möchte ich ein Rezept mit Zutaten anlegen,
  damit der Rezeptbestand die Rezepte enthält, die wir wirklich kochen.
  (FR-01, FR-02, FR-14, UR-06)

  Background:
    Given der Rezeptbestand ist leer

  Scenario: Rezept mit mehreren Zutaten wird gespeichert
    When ich ein Rezept "Tomatensalat" für 2 Portionen mit der Saison "Sommer" anlege
    And ich die Zutat "Tomate" mit 400 "g" hinzufüge
    And ich die Zutat "Olivenöl" mit 2 "EL" hinzufüge
    And ich das Rezept speichere
    Then wird das Rezept gespeichert
    And der Rezeptbestand enthält 1 Rezept
    And das Rezept "Tomatensalat" hat 2 Zutatenzeilen

  Scenario: Ohne Angabe ist die Saison ganzjährig
    When ich ein Rezept "Rührei" für 1 Portionen ohne Saison anlege
    And ich die Zutat "Ei" mit 3 "Stück" hinzufüge
    And ich das Rezept speichere
    Then wird das Rezept gespeichert
    And das Rezept "Rührei" hat die Saison "ganzjährig"

  Scenario: Rezept ohne Zutatenzeile wird abgelehnt
    When ich ein Rezept "Leeres Rezept" für 2 Portionen anlege
    And ich das Rezept speichere
    Then wird das Rezept abgelehnt
    And die Meldung lautet "Mindestens eine Zutat ist erforderlich"
    And der Rezeptbestand enthält 0 Rezepte

  Scenario: Dieselbe Zutat darf in einem Rezept nicht zweimal vorkommen
    When ich ein Rezept "Tomatensalat" für 2 Portionen anlege
    And ich die Zutat "Tomate" mit 400 "g" hinzufüge
    And ich die Zutat "tomate" mit 100 "g" hinzufüge
    And ich das Rezept speichere
    Then wird das Rezept abgelehnt
    And die Meldung lautet "Die Zutat tomate kommt bereits vor"
    And der Rezeptbestand enthält 0 Rezepte

  Scenario Outline: Ungültige Eingaben werden mit verständlicher Meldung abgelehnt
    When ich ein Rezept "<name>" für <portionen> Portionen anlege
    And ich die Zutat "Tomate" mit <menge> "<einheit>" hinzufüge
    And ich das Rezept speichere
    Then wird das Rezept abgelehnt
    And die Meldung lautet "<meldung>"
    And der Rezeptbestand enthält 0 Rezepte

    Examples:
      | name         | portionen | menge | einheit | meldung                                    |
      |              | 2         | 100   | g       | Name ist ein Pflichtfeld                   |
      | Tomatensalat | 0         | 100   | g       | Portionszahl muss zwischen 1 und 20 liegen |
      | Tomatensalat | 21        | 100   | g       | Portionszahl muss zwischen 1 und 20 liegen |
      | Tomatensalat | 2         | 0     | g       | Menge muss größer als 0 sein               |
      | Tomatensalat | 2         | 100   | Tasse   | Bitte eine gültige Einheit wählen          |

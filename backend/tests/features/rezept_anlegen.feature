Feature: Rezept anlegen

  Background:
    Given der Rezeptbestand ist leer

  Szenario: Rezept mit mehreren Zutaten wird gespeichert
    When ein WG Mitglied ein Rezept "Tomatensalat" für 2 Portionen mit der Saison "Sommer" anlegt
    And das WG Mitglied die Zutat "Tomate" mit 400 "g" hinzufügt
    And das WG Mitglied die Zutat "Olivenöl" mit 2 "EL" hinzufügt
    And das WG Mitglied das Rezept speichert
    Then wird das Rezept gespeichert
    And der Rezeptbestand enthält 1 Rezept
    And das Rezept "Tomatensalat" hat 2 Zutatenzeilen

  Szenario: Rezept ohne Zutatenzeile wird abgelehnt
    When ein WG Mitglied ein Rezept "Leeres Rezept" für 2 Portionen anlegt
    And das WG Mitglied das Rezept speichert
    Then wird das Rezept abgelehnt
    And die Meldung lautet "Mindestens eine Zutat ist erforderlich"
    And der Rezeptbestand enthält 0 Rezepte


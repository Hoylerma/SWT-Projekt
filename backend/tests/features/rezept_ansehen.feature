Feature: Rezept mit Zutaten ansehen 

Szenario: Rezept wird angezeigt
    Given es sind Rezepte angelegt 
    When ein WG Mitglied ein Rezept auswählt 
    Then wird es angezeigt 

Szenario: Rezept existiert nicht (mehr)
    Given das gesuchte Rezept ist nicht angelegt
    When ein WG Mitglied ein Rezept auswählt 
    Then wird es nicht angezeigt
    And eine Fehlermeldung wird angezeigt 
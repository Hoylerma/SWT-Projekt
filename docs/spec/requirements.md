| Begriff                  | Bedeutung                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rezept               | Primärentität. Besteht aus Name, Beschreibung, Portionszahl, optionalen Zubereitungsschritten, einer Saison-Zuordnung und mindestens einer Zutatenzeile. |
| Zutat / Zutatenzeile | Kind-Entität eines Rezepts: Zutatenname, Menge und Einheit. Ein Rezept hat eine bis viele Zutatenzeilen, jede Zutatenzeile gehört genau zu einem Rezept. |
| Auswahl              | Die Zutaten, die ein WG-Mitglied für eine Suche als "vorhanden" markiert. Sie gilt nur für die aktuelle Suche und wird nicht dauerhaft gespeichert.      |
| Abdeckung            | Anteil der Zutaten eines Rezepts, die in der Auswahl enthalten sind (Anzahl abgedeckter Zutaten geteilt durch Gesamtzahl der Zutaten des Rezepts).       |
| Saison               | Frühling, Sommer, Herbst oder Winter. Jedes Rezept ist einer Saison oder "ganzjährig" zugeordnet.                                                        |
| Kalender-Dienst      | Externe Abhängigkeit. Liefert das aktuelle Datum, aus dem das System die aktuelle Saison ableitet.                                                       |

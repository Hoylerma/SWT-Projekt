# WG Cook Lab 7

# Exercise 7.1 (20 Points): Black-Box Testing Techniques

| Parameter | Class ID | Class Type | Partition Description | Representative Test Value |
|---|---|---|---|---|
| Zutatenname | EC-1 | valid | lenght from 1 - 100 characters | "tomato" |
| Zutatenname | EC-2 | invalid | no character or empty | "" |
| Zutatenname | EC-3 | invalid | lenght more then 100 characters | 17 * "tomato" |
| Zutatenname | EC-4 | invalid | ingredient may only appear once per recipe | "Tomato", "tomato" |

| Parameter | Class ID | Class Type | Partition Description | Representative Test Value |
| Zutatenanzahl | EC-5 | valid | lenght from 1 - 99999 characters | 3 |
| Zutatenanzahl | EC-6 | invalid | input other then a number | "a" |
| Zutatenanzahl | EC-7 | invalid | greater 99999 | "100000" |
| Zutatenanzahl | EC-8 | invalid | no character or empty | "" |

| Parameter | Class ID | Class Type | Partition Description | Representative Test Value |
| Zutateneinheit | EC-9| valid | dropdown list | "ml" |
| Zutateneinheit | EC-10 | invalid | no selection | "" |


- EC-1: Die Spezifikation behandelt jeden Namen mit 1 bis 100 Zeichen gleich, deshalb vertritt ein beliebiger mittlerer Wert die Klasse. Die Grenzwerte werden in der Grenzwerttabelle einzeln getestet (1 und 100). (FR-02)
- EC-2: Ein leeres Pflichtfeld ist der typische Bedienfehler. Die Länge 0 liegt knapp unter der unteren Grenze 1. (FR-14)
- EC-3: Alle Namen über 100 Zeichen werden gleich abgelehnt, 101 Zeichen ist der Wert knapp oberhalb der oberen Grenze. (FR-02)
- EC-4: Zutatennamen dürfen nicht mehrmals in einem Rezept vorkommen, zwischen Groß- und Kleinschreibung wird nicht unterschieden. Es reicht ein Zutat in Groß- / Kleinschreibung für das Prinzip zu testen. (FR-02)

- EC-5: Die Spezifikation behandelt jede Anzahl von 1 bis 99999 gleich, deshalb vertritt ein beliebiger mittlerer Wert die Klasse.  Die Grenzwerte werden in der Grenzwerttabelle einzeln getestet (1 und 99999). (FR-02)
- EC-6: Alle anderen Inputs außer Zahlen sind invalide und führen nicht zu einem Ergebnis. (FR-14)
- EC-7: Alle Zahlen über 99999 werden gleich abgelehnt, 100000 ist der Wert knapp oberhalb der oberen Grenze. (FR-02)
- EC-8: Ein leeres Pflichtfeld ist der typische Bedienfehler. Die Zahl 0 liegt knapp unter der unteren Grenze 1. (FR-14)

- EC-9: Eine Auswahl zwischen 7 gegebenen Möglichkeiten ist, deshalb ist die Auswahl nicht relevant für Validierung. (FR-02)
- EC-10: Ein leeres Pflichtfeld ist der typische Bedienfehler. Keine Auswahl führt zum Fehler. (FR-14)

| Parameter | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| Zutatenname | valid | invalid | valid | invalid | valid | invalid | valid | invalid |
| Menge | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| Einheit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

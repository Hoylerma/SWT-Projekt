from behave import given, when, then
from app.rezept_service import EingabeFehler, RezeptEingabe, ZutatEingabe


def liste(text):
    """ "Tomate, Zwiebel" -> ["Tomate", "Zwiebel"] """
    return [teil.strip() for teil in text.split(",") if teil.strip()]


@given("der Rezeptbestand enthält diese Rezepte:")
def step_bestand_mit_rezepten(context):
    for zeile in context.table:
        zutaten = [ZutatEingabe(name, 1, "Stück") for name in liste(zeile["Zutaten"])]
        context.service.rezept_anlegen(RezeptEingabe(zeile["Rezept"], 2, zeile["Saison"], zutaten))


@given('der Kalender-Dienst liefert als Datum den "{datum}"')
def step_kalender_datum(context, datum):
    context.kalender.liefere_datum(datum)


@given("ein WG Mitglied möchte Rezepte anhand angegebener Zutaten sehen")
def step_moechte_suchen(context):
    context.suchergebnis = None


@when("das WG Mitglied keine Zutat auswählt")
def step_keine_zutat(context):
    try:
        context.suchergebnis = context.service.rezepte_suchen([])
    except EingabeFehler as e:
        context.meldung = str(e)


@then("wird eine Fehlermeldung ausgegeben")
def step_fehlermeldung(context):
    assert context.suchergebnis is None
    assert context.meldung == "Bitte mindestens eine Zutat auswählen"


@given('ein WG Mitglied hat die Zutaten "{zutaten}" ausgewählt und gesucht')
def step_ausgewaehlt_und_gesucht(context, zutaten):
    context.suchergebnis = context.service.rezepte_suchen(liste(zutaten))


@when('das WG Mitglied das Rezept "{name}" öffnet')
def step_treffer_oeffnen(context, name):
    treffer = next(t for t in context.suchergebnis.treffer if t.rezept.name == name)
    context.rezept = context.service.rezept_oeffnen(treffer.rezept.id)


@then('sieht das WG Mitglied die Zutaten "{zutaten}" mit Menge und Einheit')
def step_zutaten_mit_menge(context, zutaten):
    assert [z.name for z in context.rezept.zutaten] == liste(zutaten)
    for z in context.rezept.zutaten:
        assert z.menge > 0 and z.einheit
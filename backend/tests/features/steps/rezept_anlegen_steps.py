from behave import given, when, then
from app.rezept_service import EingabeFehler, RezeptEingabe, ZutatEingabe


@given("der Rezeptbestand ist leer")
def step_bestand_leer(context):
    context.repository.leeren()


@when('ein WG Mitglied ein Rezept "{name}" für {portionen:d} Portionen mit der Saison "{saison}" anlegt')
def step_rezept_mit_saison(context, name, portionen, saison):
    context.eingabe = RezeptEingabe(name, portionen, saison)


@when('ein WG Mitglied ein Rezept "{name}" für {portionen:d} Portionen anlegt')
def step_rezept_anlegen(context, name, portionen):
    context.eingabe = RezeptEingabe(name, portionen)


@when('das WG Mitglied die Zutat "{name}" mit {menge:d} "{einheit}" hinzufügt')
def step_zutat_hinzufuegen(context, name, menge, einheit):
    context.eingabe.zutaten.append(ZutatEingabe(name, menge, einheit))


@when("das WG Mitglied das Rezept speichert")
def step_speichern(context):
    try:
        context.rezept = context.service.rezept_anlegen(context.eingabe)
    except EingabeFehler as e:
        context.meldung = str(e)


@then("wird das Rezept gespeichert")
def step_gespeichert(context):
    assert context.rezept is not None


@then("wird das Rezept abgelehnt")
def step_abgelehnt(context):
    assert context.rezept is None


@then('die Meldung lautet "{meldung}"')
def step_meldung(context, meldung):
    assert context.meldung == meldung


@then("der Rezeptbestand enthält {anzahl:d} Rezept")
@then("der Rezeptbestand enthält {anzahl:d} Rezepte")
def step_bestand_enthaelt(context, anzahl):
    assert len(context.service.rezepte_auflisten()) == anzahl


@then('das Rezept "{name}" hat {anzahl:d} Zutatenzeilen')
def step_zutatenzeilen(context, name, anzahl):
    rezept = next(r for r in context.service.rezepte_auflisten() if r.name == name)
    assert len(rezept.zutaten) == anzahl
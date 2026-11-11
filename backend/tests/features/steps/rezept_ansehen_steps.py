from behave import given, when, then
from app.rezept_service import RezeptEingabe, RezeptNichtGefunden, ZutatEingabe


@given("es sind Rezepte angelegt")
def step_rezepte_angelegt(context):
    rezept = context.service.rezept_anlegen(RezeptEingabe(
        "Tomatensalat", 2, "Sommer",
        [ZutatEingabe("Tomate", 400, "g"), ZutatEingabe("Olivenöl", 2, "EL")]))
    context.rezept_id = rezept.id


@given("das gesuchte Rezept ist nicht angelegt")
def step_rezept_nicht_angelegt(context):
    context.rezept_id = 9999


@when("ein WG Mitglied ein Rezept auswählt")
def step_rezept_auswaehlen(context):
    try:
        context.rezept = context.service.rezept_oeffnen(context.rezept_id)
    except RezeptNichtGefunden as e:
        context.meldung = str(e)


@then("wird es angezeigt")
def step_angezeigt(context):
    assert context.rezept is not None
    assert context.rezept.name == "Tomatensalat"
    assert len(context.rezept.zutaten) == 2


@then("wird es nicht angezeigt")
def step_nicht_angezeigt(context):
    assert context.rezept is None


@then("eine Fehlermeldung wird angezeigt")
def step_fehlermeldung_angezeigt(context):
    assert context.meldung == "Rezept nicht gefunden"
import pytest

from app.models import Rezept


def test_gueltiges_rezept_hat_die_gesetzten_werte():
    r = Rezept(name="Pasta", portionen=2)
    assert r.name == "Pasta"
    assert r.portionen == 2


@pytest.mark.parametrize("name", [None, "", "   "])
def test_fehlender_name_wird_abgelehnt(name):
    with pytest.raises(ValueError):
        Rezept(name=name, portionen=2)


def test_fehlende_portionen_werden_abgelehnt():
    with pytest.raises(ValueError):
        Rezept(name="Pasta", portionen=None)


def test_add_zutat_haengt_zeile_an_und_gibt_sie_zurueck():
    r = Rezept(name="Pasta", portionen=2)
    zeile = r.add_zutat("Nudeln", 500, "g")
    assert zeile in r.zutaten
    assert len(r.zutaten) == 1

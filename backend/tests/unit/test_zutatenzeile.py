import pytest

from app.models import Zutatenzeile


def test_gueltige_zutatenzeile_hat_die_gesetzten_werte():
    z = Zutatenzeile(name="Nudeln", menge=500, einheit="g")
    assert (z.name, z.menge, z.einheit) == ("Nudeln", 500, "g")


@pytest.mark.parametrize("name", [None, "", "  "])
def test_fehlender_name_wird_abgelehnt(name):
    with pytest.raises(ValueError):
        Zutatenzeile(name=name, menge=1, einheit="g")


def test_fehlende_menge_wird_abgelehnt():
    with pytest.raises(ValueError):
        Zutatenzeile(name="Nudeln", menge=None, einheit="g")


@pytest.mark.parametrize("einheit", [None, "", " "])
def test_fehlende_einheit_wird_abgelehnt(einheit):
    with pytest.raises(ValueError):
        Zutatenzeile(name="Nudeln", menge=1, einheit=einheit)

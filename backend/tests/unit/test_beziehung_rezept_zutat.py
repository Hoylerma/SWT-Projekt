from app.models import Rezept, Zutatenzeile


def test_hinzugefuegte_zutat_ist_ueber_das_rezept_sichtbar():
    r = Rezept(name="Pasta", portionen=2)
    z = r.add_zutat("Nudeln", 500, "g")
    assert r.zutaten == [z]


def test_zutat_zeigt_auf_ihr_rezept_zurueck():
    r = Rezept(name="Pasta", portionen=2)
    z = r.add_zutat("Nudeln", 500, "g")
    assert z.rezept is r


def test_manuell_gesetztes_rezept_erscheint_in_der_liste():
    r = Rezept(name="Pasta", portionen=2)
    z = Zutatenzeile(name="Salz", menge=1, einheit="TL")
    z.rezept = r
    assert z in r.zutaten

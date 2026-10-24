"""Unit-Tests der Kind-Entität Zutatenzeile (ohne Datenbank, ohne Kalender-Dienst)."""
from decimal import Decimal

import pytest

from app.models import MENGE_MAX, ZUTAT_NAME_MAX, Einheit, Zutatenzeile


# --- Erzeugung mit gültigen Daten -------------------------------------------
def test_zutatenzeile_wird_mit_gueltigen_daten_erzeugt():
    zeile = Zutatenzeile("Tomate", 3, Einheit.STUECK)

    assert zeile.name == "Tomate"
    assert zeile.menge == Decimal("3")
    assert zeile.einheit is Einheit.STUECK
    assert zeile.rezept is None


def test_name_wird_bereinigt_und_schluessel_ohne_grossschreibung_gebildet():
    zeile = Zutatenzeile("  Olivenöl ", 2, "EL")

    assert zeile.name == "Olivenöl"
    assert zeile.name_key == "olivenöl"


def test_dezimale_menge_wird_exakt_gespeichert():
    assert Zutatenzeile("Mehl", 2.5, "kg").menge == Decimal("2.5")


# --- Name (1 bis 60 Zeichen, Pflicht) ---------------------------------------
@pytest.mark.parametrize("name", ["a", "x" * ZUTAT_NAME_MAX])
def test_name_an_den_grenzen_ist_gueltig(name):
    assert Zutatenzeile(name, 1, "g").name == name


@pytest.mark.parametrize("name", ["", "   ", None, "x" * (ZUTAT_NAME_MAX + 1)])
def test_ungueltiger_zutatenname_wird_abgelehnt(name):
    with pytest.raises(ValueError, match="Zutatenname"):
        Zutatenzeile(name, 1, "g")


# --- Menge (größer 0, höchstens 99999) --------------------------------------
@pytest.mark.parametrize("menge", [0.001, 1, 250, 99999, MENGE_MAX, "12.5"])
def test_gueltige_mengen_werden_akzeptiert(menge):
    assert Zutatenzeile("Zucker", menge, "g").menge > 0


@pytest.mark.parametrize("menge", [0, -1, -0.5, "0"])
def test_menge_null_oder_negativ_wird_abgelehnt(menge):
    with pytest.raises(ValueError, match="Menge"):
        Zutatenzeile("Zucker", menge, "g")


@pytest.mark.parametrize("menge", [99999.01, 100000, 1e9])
def test_zu_grosse_menge_wird_abgelehnt(menge):
    with pytest.raises(ValueError, match="Menge"):
        Zutatenzeile("Zucker", menge, "g")


@pytest.mark.parametrize("menge", [None, "abc", "", float("nan"), float("inf"), True])
def test_keine_zahl_als_menge_wird_abgelehnt(menge):
    with pytest.raises(ValueError, match="Menge"):
        Zutatenzeile("Zucker", menge, "g")


# --- Einheit (g, kg, ml, l, Stück, EL, TL) ----------------------------------
@pytest.mark.parametrize("einheit", list(Einheit))
def test_alle_erlaubten_einheiten_werden_akzeptiert(einheit):
    assert Zutatenzeile("Wasser", 1, einheit).einheit is einheit


@pytest.mark.parametrize(
    "text, erwartet",
    [("g", Einheit.G), ("kg", Einheit.KG), ("Stück", Einheit.STUECK), ("el", Einheit.EL), ("TL", Einheit.TL)],
)
def test_einheit_wird_aus_text_erkannt(text, erwartet):
    assert Zutatenzeile("Wasser", 1, text).einheit is erwartet


@pytest.mark.parametrize("einheit", ["Tasse", "", None, 5])
def test_ungueltige_einheit_wird_abgelehnt(einheit):
    with pytest.raises(ValueError, match="Einheit"):
        Zutatenzeile("Wasser", 1, einheit)

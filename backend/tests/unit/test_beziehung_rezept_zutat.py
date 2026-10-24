"""Unit-Tests der 1:n-Beziehung Rezept → Zutatenzeile und der Hilfsmethoden (ohne Datenbank)."""
from decimal import Decimal

import pytest

from app.models import Einheit, Rezept, Zutatenzeile


@pytest.fixture
def rezept():
    return Rezept("Tomatensuppe", 4)


# --- Beziehung in beide Richtungen ------------------------------------------
def test_hinzugefuegte_zutat_ist_vom_rezept_abrufbar_und_zeigt_zurueck(rezept):
    zeile = rezept.add_zutat("Tomate", 6, "Stück")

    assert zeile in rezept.zutaten
    assert zeile.rezept is rezept
    assert rezept.zutaten == [zeile]


def test_zutatenzeile_mit_rezept_im_konstruktor_erscheint_in_der_liste_des_rezepts(rezept):
    zeile = Zutatenzeile("Zwiebel", 1, "Stück", rezept=rezept)

    assert rezept.zutaten == [zeile]
    assert zeile.rezept is rezept


def test_zutatenzeile_ohne_rezept_taucht_in_keinem_rezept_auf(rezept):
    Zutatenzeile("Zwiebel", 1, "Stück")

    assert rezept.zutaten == []


def test_mehrere_zutaten_bleiben_in_der_reihenfolge_des_hinzufuegens(rezept):
    rezept.add_zutat("Tomate", 6, "Stück")
    rezept.add_zutat("Sahne", 100, "ml")
    rezept.add_zutat("Salz", 1, "TL")

    assert [z.name for z in rezept.zutaten] == ["Tomate", "Sahne", "Salz"]


def test_zutaten_zweier_rezepte_sind_getrennt():
    suppe = Rezept("Suppe", 2)
    salat = Rezept("Salat", 2)
    suppe.add_zutat("Tomate", 2, "Stück")
    salat.add_zutat("Gurke", 1, "Stück")

    assert [z.name for z in suppe.zutaten] == ["Tomate"]
    assert [z.name for z in salat.zutaten] == ["Gurke"]


# --- add_zutat ---------------------------------------------------------------
def test_add_zutat_gibt_die_neue_zeile_mit_den_werten_zurueck(rezept):
    zeile = rezept.add_zutat("Sahne", "100", "ml")

    assert zeile.name == "Sahne"
    assert zeile.menge == Decimal("100")
    assert zeile.einheit is Einheit.ML


def test_zutatenname_darf_nur_einmal_vorkommen(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")

    with pytest.raises(ValueError, match="bereits vorhanden"):
        rezept.add_zutat("Tomate", 5, "Stück")
    assert len(rezept.zutaten) == 1


def test_doppelte_zutat_wird_ohne_beachtung_der_grossschreibung_erkannt(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")

    with pytest.raises(ValueError, match="bereits vorhanden"):
        rezept.add_zutat("  tOMATE ", 1, "kg")


def test_ungueltige_zutat_aendert_das_rezept_nicht(rezept):
    with pytest.raises(ValueError, match="Menge"):
        rezept.add_zutat("Tomate", 0, "Stück")

    assert rezept.zutaten == []


# --- remove_zutat ------------------------------------------------------------
def test_zutat_kann_entfernt_werden_solange_eine_uebrig_bleibt(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")
    rezept.add_zutat("Salz", 1, "TL")

    rezept.remove_zutat("salz")

    assert [z.name for z in rezept.zutaten] == ["Tomate"]


def test_entfernte_zutat_zeigt_nicht_mehr_auf_das_rezept(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")
    salz = rezept.add_zutat("Salz", 1, "TL")

    rezept.remove_zutat("Salz")

    assert salz.rezept is None


def test_letzte_zutat_kann_nicht_entfernt_werden(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")

    with pytest.raises(ValueError, match="mindestens eine Zutat"):
        rezept.remove_zutat("Tomate")
    assert len(rezept.zutaten) == 1


def test_unbekannte_zutat_kann_nicht_entfernt_werden(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")

    with pytest.raises(ValueError, match="nicht vorhanden"):
        rezept.remove_zutat("Banane")


# --- zutat_schluessel --------------------------------------------------------
def test_zutat_schluessel_liefert_namen_in_kleinschreibung(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")
    rezept.add_zutat("Olivenöl", 2, "EL")

    assert rezept.zutat_schluessel() == {"tomate", "olivenöl"}


def test_zutat_schluessel_eines_leeren_rezepts_ist_leer(rezept):
    assert rezept.zutat_schluessel() == set()


# --- erstelle (Fabrikmethode) und validiere ---------------------------------
def test_erstelle_legt_rezept_mit_allen_zutaten_an():
    rezept = Rezept.erstelle(
        "Rührei",
        2,
        [("Ei", 4, "Stück"), ("Butter", 10, "g")],
        beschreibung="Schnell und einfach",
    )

    assert rezept.name == "Rührei"
    assert rezept.beschreibung == "Schnell und einfach"
    assert [z.name for z in rezept.zutaten] == ["Ei", "Butter"]
    assert all(z.rezept is rezept for z in rezept.zutaten)


def test_erstelle_ohne_zutaten_wird_abgelehnt():
    with pytest.raises(ValueError, match="mindestens eine Zutat"):
        Rezept.erstelle("Leer", 2, [])


def test_erstelle_mit_doppelter_zutat_wird_abgelehnt():
    with pytest.raises(ValueError, match="bereits vorhanden"):
        Rezept.erstelle("Doppelt", 2, [("Ei", 2, "Stück"), ("ei", 1, "Stück")])


def test_validiere_lehnt_rezept_ohne_zutaten_ab(rezept):
    with pytest.raises(ValueError, match="mindestens eine Zutat"):
        rezept.validiere()


def test_validiere_akzeptiert_vollstaendiges_rezept(rezept):
    rezept.add_zutat("Tomate", 2, "Stück")

    rezept.validiere()  # wirft nichts


def test_validiere_erkennt_doppelte_zutat_die_am_konstruktor_vorbei_eingefuegt_wurde(rezept):
    Zutatenzeile("Tomate", 1, "Stück", rezept=rezept)
    Zutatenzeile("tomate", 2, "Stück", rezept=rezept)

    with pytest.raises(ValueError, match="nur einmal"):
        rezept.validiere()

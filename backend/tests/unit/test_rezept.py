"""Unit-Tests der Primärentität Rezept (ohne Datenbank, ohne Kalender-Dienst)."""
import pytest

from app.models import (
    BESCHREIBUNG_MAX,
    PORTIONEN_MAX,
    PORTIONEN_MIN,
    REZEPT_NAME_MAX,
    SCHRITTE_MAX,
    Rezept,
    Saison,
)


# --- Erzeugung mit gültigen Daten -------------------------------------------
def test_rezept_mit_pflichtfeldern_wird_erzeugt():
    rezept = Rezept("Tomatensuppe", 4)

    assert rezept.name == "Tomatensuppe"
    assert rezept.portionen == 4
    assert rezept.beschreibung is None
    assert rezept.schritte is None
    assert rezept.zutaten == []


def test_saison_ist_standardmaessig_ganzjaehrig():
    assert Rezept("Nudeln", 2).saison is Saison.GANZJAEHRIG


def test_rezept_mit_allen_feldern_wird_erzeugt():
    rezept = Rezept(
        "Spargelsalat",
        2,
        beschreibung="Frisch und leicht",
        schritte="Spargel kochen, abkühlen lassen, anmachen.",
        saison=Saison.FRUEHLING,
    )

    assert rezept.beschreibung == "Frisch und leicht"
    assert rezept.schritte.startswith("Spargel kochen")
    assert rezept.saison is Saison.FRUEHLING


def test_name_wird_von_leerraum_befreit():
    assert Rezept("  Pfannkuchen  ", 2).name == "Pfannkuchen"


# --- Name (1 bis 100 Zeichen, Pflicht) --------------------------------------
@pytest.mark.parametrize("name", ["a", "x" * REZEPT_NAME_MAX])
def test_name_an_den_grenzen_ist_gueltig(name):
    assert Rezept(name, 2).name == name


@pytest.mark.parametrize("name", ["", "   ", None, "x" * (REZEPT_NAME_MAX + 1)])
def test_ungueltiger_name_wird_abgelehnt(name):
    with pytest.raises(ValueError, match="Name"):
        Rezept(name, 2)


def test_name_muss_ein_text_sein():
    with pytest.raises(ValueError, match="Name"):
        Rezept(123, 2)


# --- Portionen (ganze Zahl 1 bis 20) ----------------------------------------
@pytest.mark.parametrize("portionen", [PORTIONEN_MIN, 10, PORTIONEN_MAX])
def test_portionen_im_bereich_sind_gueltig(portionen):
    assert Rezept("Eintopf", portionen).portionen == portionen


@pytest.mark.parametrize("portionen", [0, -1, PORTIONEN_MAX + 1, 100])
def test_portionen_ausserhalb_des_bereichs_werden_abgelehnt(portionen):
    with pytest.raises(ValueError, match="Portionen"):
        Rezept("Eintopf", portionen)


@pytest.mark.parametrize("portionen", [2.5, "3", None, True])
def test_portionen_muessen_eine_ganze_zahl_sein(portionen):
    with pytest.raises(ValueError, match="Portionen"):
        Rezept("Eintopf", portionen)


# --- Optionale Felder --------------------------------------------------------
def test_beschreibung_an_der_grenze_ist_gueltig():
    assert len(Rezept("A", 1, beschreibung="x" * BESCHREIBUNG_MAX).beschreibung) == BESCHREIBUNG_MAX


def test_zu_lange_beschreibung_wird_abgelehnt():
    with pytest.raises(ValueError, match="Beschreibung"):
        Rezept("A", 1, beschreibung="x" * (BESCHREIBUNG_MAX + 1))


def test_schritte_an_der_grenze_sind_gueltig():
    assert len(Rezept("A", 1, schritte="x" * SCHRITTE_MAX).schritte) == SCHRITTE_MAX


def test_zu_lange_schritte_werden_abgelehnt():
    with pytest.raises(ValueError, match="Zubereitungsschritte"):
        Rezept("A", 1, schritte="x" * (SCHRITTE_MAX + 1))


def test_leere_optionale_texte_werden_zu_none():
    rezept = Rezept("A", 1, beschreibung="   ", schritte="")
    assert rezept.beschreibung is None
    assert rezept.schritte is None


# --- Saison ------------------------------------------------------------------
@pytest.mark.parametrize(
    "eingabe, erwartet",
    [
        (Saison.WINTER, Saison.WINTER),
        ("Sommer", Saison.SOMMER),
        ("herbst", Saison.HERBST),
        ("FRUEHLING", Saison.FRUEHLING),
        ("ganzjährig", Saison.GANZJAEHRIG),
    ],
)
def test_saison_wird_aus_mitglied_wert_oder_name_erkannt(eingabe, erwartet):
    assert Rezept("A", 1, saison=eingabe).saison is erwartet


@pytest.mark.parametrize("saison", ["Monsun", "", None, 3])
def test_ungueltige_saison_wird_abgelehnt(saison):
    with pytest.raises(ValueError, match="Saison"):
        Rezept("A", 1, saison=saison)


def test_ungueltiger_wert_beim_aendern_wird_ebenfalls_abgelehnt():
    rezept = Rezept("A", 1)
    with pytest.raises(ValueError, match="Portionen"):
        rezept.portionen = 0
    assert rezept.portionen == 1

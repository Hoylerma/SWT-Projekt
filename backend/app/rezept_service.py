"""Anwendungsschicht (Use Cases) für Rezepte: anlegen, auflisten, öffnen, suchen.
Bekommt Repository und Kalender-Dienst über ihre Schnittstellen im Konstruktor.
Lab 5: Fake + Stub aus den Tests. Lab 8: echtes Repository + Mock bzw. echter Dienst.
KI GENERIERT CLaude Opus 5.5"""
from dataclasses import dataclass, field
from datetime import date
from fractions import Fraction

from app.kalender import KalenderDienst, KalenderDienstFehler, saison_aus_datum
from app.models import Rezept
from app.repository import RezeptRepository

GANZJAEHRIG = "ganzjährig"
SAISONS = ("Frühling", "Sommer", "Herbst", "Winter", GANZJAEHRIG)
EINHEITEN = ("g", "kg", "ml", "l", "Stück", "EL", "TL")

MELDUNG_KEINE_TREFFER = "Keine passenden Rezepte gefunden"
MELDUNG_LEERE_AUSWAHL = "Bitte mindestens eine Zutat auswählen"
MELDUNG_NICHT_GEFUNDEN = "Rezept nicht gefunden"
HINWEIS_OHNE_SAISON = "Saisonale Sortierung ist gerade nicht verfügbar"


class EingabeFehler(ValueError):
    """Ungültige Eingabe (FR-14). Die Nachricht ist für Nutzer lesbar."""


class RezeptNichtGefunden(LookupError):
    def __init__(self):
        super().__init__(MELDUNG_NICHT_GEFUNDEN)


# ---------- Ein- und Ausgabe-Objekte ----------

@dataclass
class ZutatEingabe:
    name: str
    menge: float
    einheit: str


@dataclass
class RezeptEingabe:
    """Was der Nutzer zum Anlegen eingibt (in Lab 8 der Request-Body der API)."""
    name: str
    portionen: int
    saison: str | None = None
    zutaten: list[ZutatEingabe] = field(default_factory=list)


@dataclass(frozen=True)
class Treffer:
    rezept: Rezept
    abgedeckt: int
    gesamt: int
    fehlende_zutaten: tuple[str, ...]

    @property
    def abdeckung(self) -> Fraction:
        return Fraction(self.abgedeckt, self.gesamt)

    @property
    def abdeckung_text(self) -> str:                      # FR-10: "3 von 3"
        return f"{self.abgedeckt} von {self.gesamt}"

    @property
    def kennzeichnung(self) -> str | None:                # FR-10: "vollständig"
        return "vollständig" if self.abgedeckt == self.gesamt else None


@dataclass(frozen=True)
class Suchergebnis:
    treffer: tuple[Treffer, ...]
    meldung: str | None = None                            # z. B. "Keine passenden Rezepte gefunden"
    hinweis: str | None = None                            # z. B. Saison nicht verfügbar


def _schluessel(text: str) -> str:
    """Vergleich ohne Leerzeichen am Rand und ohne Groß-/Kleinschreibung."""
    return text.strip().casefold()


# ---------- Der Service ----------

class RezeptService:
    def __init__(self, repository: RezeptRepository, kalender: KalenderDienst):
        self._repository = repository
        self._kalender = kalender

    # ----- UC-03 Rezept anlegen (FR-01, FR-02, FR-14) -----

    def rezept_anlegen(self, eingabe: RezeptEingabe) -> Rezept:
        self._pruefe_rezept(eingabe)                       # erst alles prüfen ...
        rezept = Rezept(
            name=eingabe.name.strip(),
            portionen=eingabe.portionen,
            saison=eingabe.saison or GANZJAEHRIG,          # Standard: ganzjährig
        )
        for z in eingabe.zutaten:
            rezept.add_zutat(z.name.strip(), z.menge, z.einheit)
        return self._repository.speichern(rezept)          # ... dann speichern

    def _pruefe_rezept(self, eingabe: RezeptEingabe):
        name = (eingabe.name or "").strip()
        if not name:
            raise EingabeFehler("Name ist ein Pflichtfeld")
        if len(name) > 100:
            raise EingabeFehler("Name darf höchstens 100 Zeichen lang sein")
        if eingabe.portionen is None or not 1 <= eingabe.portionen <= 20:
            raise EingabeFehler("Portionszahl muss zwischen 1 und 20 liegen")
        if eingabe.saison is not None and eingabe.saison not in SAISONS:
            raise EingabeFehler("Bitte eine gültige Saison wählen")
        if not eingabe.zutaten:
            raise EingabeFehler("Mindestens eine Zutat ist erforderlich")

        bekannte = set()
        for z in eingabe.zutaten:
            self._pruefe_zutat(z)
            if _schluessel(z.name) in bekannte:
                raise EingabeFehler(f"Die Zutat {z.name.strip()} kommt bereits vor")
            bekannte.add(_schluessel(z.name))

    @staticmethod
    def _pruefe_zutat(z: ZutatEingabe):
        if not (z.name or "").strip():
            raise EingabeFehler("Zutatenname ist ein Pflichtfeld")
        if z.menge is None or z.menge <= 0:
            raise EingabeFehler("Menge muss größer als 0 sein")
        if z.menge > 99999:
            raise EingabeFehler("Menge darf höchstens 99999 sein")
        if z.einheit not in EINHEITEN:
            raise EingabeFehler("Bitte eine gültige Einheit wählen")

    # ----- FR-03 / UC-02 Auflisten und Öffnen -----

    def rezepte_auflisten(self) -> list[Rezept]:
        return sorted(self._repository.alle(), key=lambda r: _schluessel(r.name))

    def rezept_oeffnen(self, rezept_id: int) -> Rezept:
        rezept = self._repository.finden(rezept_id)
        if rezept is None:
            raise RezeptNichtGefunden()
        return rezept

    # ----- UC-01 Rezepte finden (FR-08 bis FR-10, FR-13) -----

    def rezepte_suchen(self, auswahl: list[str]) -> Suchergebnis:
        gewaehlt = {_schluessel(z) for z in auswahl if z and z.strip()}
        if not gewaehlt:
            raise EingabeFehler(MELDUNG_LEERE_AUSWAHL)

        treffer = [t for r in self._repository.alle() if (t := self._bewerte(r, gewaehlt))]
        if not treffer:
            return Suchergebnis(treffer=(), meldung=MELDUNG_KEINE_TREFFER)

        aktuelle_saison = self._aktuelle_saison()          # fragt den Kalender-Dienst
        treffer.sort(key=lambda t: (
            -t.abdeckung,                                  # 1. Abdeckung absteigend
            self._saison_rang(t.rezept.saison, aktuelle_saison),  # 2. Saison
            _schluessel(t.rezept.name),                    # 3. alphabetisch
        ))
        hinweis = HINWEIS_OHNE_SAISON if aktuelle_saison is None else None
        return Suchergebnis(treffer=tuple(treffer), hinweis=hinweis)

    @staticmethod
    def _bewerte(rezept: Rezept, gewaehlt: set[str]) -> Treffer | None:
        fehlende = tuple(z.name for z in rezept.zutaten if _schluessel(z.name) not in gewaehlt)
        gesamt = len(rezept.zutaten)
        abgedeckt = gesamt - len(fehlende)
        if abgedeckt == 0:
            return None                                    # FR-08: nur Abdeckung > 0
        return Treffer(rezept, abgedeckt, gesamt, fehlende)

    def _aktuelle_saison(self) -> str | None:
        """FR-13: Bei Timeout, Fehler oder ungültigem Datum → None, Suche läuft weiter."""
        try:
            return saison_aus_datum(date.fromisoformat(self._kalender.aktuelles_datum()))
        except (KalenderDienstFehler, ValueError, TypeError):
            return None

    @staticmethod
    def _saison_rang(saison: str, aktuelle: str | None) -> int:
        if aktuelle is None:
            return 0                                       # ohne Saison zählt das Kriterium nicht
        if saison == aktuelle:
            return 0
        if saison == GANZJAEHRIG:
            return 1
        return 2
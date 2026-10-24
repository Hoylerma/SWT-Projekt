"""Domänenmodell von WG Cook.

Primärentität: Rezept. Kind-Entität: Zutatenzeile (Zutat mit Menge und Einheit).
Der Kalender-Dienst ist bewusst KEINE Entität, er ist eine externe Abhängigkeit
und wird später hinter einer eigenen Schnittstelle gekapselt.

Die Validierung folgt den Grenzen aus docs/spec/requirements.md (FR-01, FR-02, FR-14).
Alle Fehlermeldungen nennen das betroffene Feld, damit die Oberfläche sie anzeigen kann.
"""
from __future__ import annotations

import enum
from decimal import Decimal, InvalidOperation

from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, Numeric, String, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, validates

# --- Grenzen (FR-01, FR-02) -------------------------------------------------
REZEPT_NAME_MAX = 100
PORTIONEN_MIN, PORTIONEN_MAX = 1, 20
BESCHREIBUNG_MAX = 2000
SCHRITTE_MAX = 5000
ZUTAT_NAME_MAX = 60
MENGE_MAX = Decimal("99999")


class Saison(str, enum.Enum):
    FRUEHLING = "Frühling"
    SOMMER = "Sommer"
    HERBST = "Herbst"
    WINTER = "Winter"
    GANZJAEHRIG = "ganzjährig"


class Einheit(str, enum.Enum):
    G = "g"
    KG = "kg"
    ML = "ml"
    L = "l"
    STUECK = "Stück"
    EL = "EL"
    TL = "TL"


# --- Hilfsfunktionen für die Validierung ------------------------------------
def _pruefe_text(value, feld: str, max_len: int, *, pflicht: bool) -> str | None:
    """Schneidet Leerraum ab und prüft Länge. Optionale leere Texte werden zu None."""
    if value is None:
        if pflicht:
            raise ValueError(f"{feld}: Pflichtfeld, 1 bis {max_len} Zeichen")
        return None
    if not isinstance(value, str):
        raise ValueError(f"{feld}: Text erwartet")
    text = value.strip()
    if not text:
        if pflicht:
            raise ValueError(f"{feld}: Pflichtfeld, 1 bis {max_len} Zeichen")
        return None
    if len(text) > max_len:
        raise ValueError(f"{feld}: höchstens {max_len} Zeichen erlaubt")
    return text


def _pruefe_enum(value, enum_cls: type[enum.Enum], feld: str):
    """Akzeptiert ein Enum-Mitglied, seinen Wert ("Sommer") oder seinen Namen ("SOMMER")."""
    if isinstance(value, enum_cls):
        return value
    if isinstance(value, str):
        gesucht = value.strip().casefold()
        for mitglied in enum_cls:
            if gesucht in (str(mitglied.value).casefold(), mitglied.name.casefold()):
                return mitglied
    erlaubt = ", ".join(str(m.value) for m in enum_cls)
    raise ValueError(f"{feld}: ungültiger Wert, erlaubt sind {erlaubt}")


class Base(DeclarativeBase):
    pass


class Rezept(Base):
    """Primärentität: ein Rezept mit mindestens einer Zutatenzeile."""

    __tablename__ = "rezepte"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(REZEPT_NAME_MAX))
    portionen: Mapped[int]
    beschreibung: Mapped[str | None] = mapped_column(Text, nullable=True)
    schritte: Mapped[str | None] = mapped_column(Text, nullable=True)
    saison: Mapped[Saison] = mapped_column(SAEnum(Saison, native_enum=False, length=20))

    zutaten: Mapped[list[Zutatenzeile]] = relationship(
        back_populates="rezept",
        cascade="all, delete-orphan",
        order_by="Zutatenzeile.id",
    )

    def __init__(
        self,
        name: str,
        portionen: int,
        *,
        beschreibung: str | None = None,
        schritte: str | None = None,
        saison: Saison | str = Saison.GANZJAEHRIG,
    ) -> None:
        self.name = name
        self.portionen = portionen
        self.beschreibung = beschreibung
        self.schritte = schritte
        self.saison = saison

    # --- Validierung ---------------------------------------------------------
    @validates("name")
    def _validiere_name(self, _key, value):
        return _pruefe_text(value, "Name", REZEPT_NAME_MAX, pflicht=True)

    @validates("portionen")
    def _validiere_portionen(self, _key, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"Portionen: ganze Zahl von {PORTIONEN_MIN} bis {PORTIONEN_MAX} erwartet")
        if not PORTIONEN_MIN <= value <= PORTIONEN_MAX:
            raise ValueError(f"Portionen: ganze Zahl von {PORTIONEN_MIN} bis {PORTIONEN_MAX} erwartet")
        return value

    @validates("beschreibung")
    def _validiere_beschreibung(self, _key, value):
        return _pruefe_text(value, "Beschreibung", BESCHREIBUNG_MAX, pflicht=False)

    @validates("schritte")
    def _validiere_schritte(self, _key, value):
        return _pruefe_text(value, "Zubereitungsschritte", SCHRITTE_MAX, pflicht=False)

    @validates("saison")
    def _validiere_saison(self, _key, value):
        return _pruefe_enum(value, Saison, "Saison")

    # --- Fachliche Hilfsmethoden --------------------------------------------
    @classmethod
    def erstelle(cls, name: str, portionen: int, zutaten, **felder) -> "Rezept":
        """Fabrikmethode: legt ein Rezept samt Zutatenzeilen an (mindestens eine, FR-01).

        `zutaten` ist eine Liste von Tupeln (name, menge, einheit).
        """
        zutaten = list(zutaten)
        if not zutaten:
            raise ValueError("Zutaten: ein Rezept braucht mindestens eine Zutat")
        rezept = cls(name, portionen, **felder)
        for zutat_name, menge, einheit in zutaten:
            rezept.add_zutat(zutat_name, menge, einheit)
        return rezept

    def add_zutat(self, name: str, menge, einheit) -> "Zutatenzeile":
        """Fügt eine Zutatenzeile hinzu. Ein Zutatenname darf nur einmal vorkommen (FR-02)."""
        zeile = Zutatenzeile(name, menge, einheit)
        if zeile.name_key in self.zutat_schluessel():
            raise ValueError(f"Zutatenname: '{zeile.name}' ist in diesem Rezept bereits vorhanden")
        self.zutaten.append(zeile)
        return zeile

    def remove_zutat(self, name: str) -> None:
        """Entfernt eine Zutatenzeile. Das Rezept behält mindestens eine Zutat (FR-05)."""
        schluessel = str(name).strip().casefold()
        for zeile in self.zutaten:
            if zeile.name_key == schluessel:
                if len(self.zutaten) == 1:
                    raise ValueError("Zutaten: ein Rezept braucht mindestens eine Zutat")
                self.zutaten.remove(zeile)
                return
        raise ValueError(f"Zutatenname: '{name}' ist in diesem Rezept nicht vorhanden")

    def zutat_schluessel(self) -> set[str]:
        """Zutatennamen ohne Groß-/Kleinschreibung, für Vergleiche und die Abdeckung."""
        return {z.name_key for z in self.zutaten}

    def validiere(self) -> None:
        """Prüft die Regeln, die nur über das ganze Rezept sichtbar sind (vor dem Speichern)."""
        if not self.zutaten:
            raise ValueError("Zutaten: ein Rezept braucht mindestens eine Zutat")
        schluessel = [z.name_key for z in self.zutaten]
        if len(schluessel) != len(set(schluessel)):
            raise ValueError("Zutatenname: jede Zutat darf in einem Rezept nur einmal vorkommen")

    def __repr__(self) -> str:
        return f"Rezept(id={self.id!r}, name={self.name!r}, portionen={self.portionen!r})"


class Zutatenzeile(Base):
    """Kind-Entität: eine Zutat mit Menge und Einheit, gehört zu genau einem Rezept."""

    __tablename__ = "zutatenzeilen"
    __table_args__ = (UniqueConstraint("rezept_id", "name_key", name="uq_zutat_pro_rezept"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    rezept_id: Mapped[int] = mapped_column(ForeignKey("rezepte.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(ZUTAT_NAME_MAX))
    name_key: Mapped[str] = mapped_column(String(ZUTAT_NAME_MAX))
    menge: Mapped[Decimal] = mapped_column(Numeric(12, 3))
    einheit: Mapped[Einheit] = mapped_column(SAEnum(Einheit, native_enum=False, length=10))

    rezept: Mapped[Rezept | None] = relationship(back_populates="zutaten")

    def __init__(self, name: str, menge, einheit: Einheit | str, *, rezept: Rezept | None = None) -> None:
        self.name = name
        self.menge = menge
        self.einheit = einheit
        if rezept is not None:
            self.rezept = rezept

    @validates("name")
    def _validiere_name(self, _key, value):
        text = _pruefe_text(value, "Zutatenname", ZUTAT_NAME_MAX, pflicht=True)
        self.name_key = text.casefold()
        return text

    @validates("menge")
    def _validiere_menge(self, _key, value):
        if value is None or isinstance(value, bool):
            raise ValueError("Menge: Zahl größer 0 erwartet")
        try:
            zahl = Decimal(str(value))
        except InvalidOperation:
            raise ValueError("Menge: Zahl größer 0 erwartet") from None
        if not zahl.is_finite():
            raise ValueError("Menge: Zahl größer 0 erwartet")
        if zahl <= 0:
            raise ValueError("Menge: muss größer als 0 sein")
        if zahl > MENGE_MAX:
            raise ValueError(f"Menge: höchstens {MENGE_MAX} erlaubt")
        return zahl

    @validates("einheit")
    def _validiere_einheit(self, _key, value):
        return _pruefe_enum(value, Einheit, "Einheit")

    def __repr__(self) -> str:
        return f"Zutatenzeile(name={self.name!r}, menge={self.menge!r}, einheit={self.einheit!r})"

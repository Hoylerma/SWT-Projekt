"""Domänenmodell: Rezept (Primärentität) hat viele Zutatenzeilen (Kind-Entität)."""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, validates


class Base(DeclarativeBase):
    pass


def _nicht_leer(wert, feld):
    if wert is None or not str(wert).strip():
        raise ValueError(f"{feld} ist ein Pflichtfeld")
    return wert


class Rezept(Base):
    __tablename__ = "rezepte"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    portionen: Mapped[int]
    zutaten: Mapped[list["Zutatenzeile"]] = relationship(
        back_populates="rezept", cascade="all, delete-orphan"
    )

    @validates("name")
    def _pruefe_name(self, _key, wert):
        return _nicht_leer(wert, "name")

    @validates("portionen")
    def _pruefe_portionen(self, _key, wert):
        if wert is None:
            raise ValueError("portionen ist ein Pflichtfeld")
        return wert

    def add_zutat(self, name, menge, einheit):
        """Hilfsmethode: legt eine Zutatenzeile an und verknüpft beide Seiten."""
        zeile = Zutatenzeile(name=name, menge=menge, einheit=einheit)
        self.zutaten.append(zeile)  # setzt zeile.rezept automatisch
        return zeile


class Zutatenzeile(Base):
    __tablename__ = "zutatenzeilen"

    id: Mapped[int] = mapped_column(primary_key=True)
    rezept_id: Mapped[int] = mapped_column(ForeignKey("rezepte.id"))
    name: Mapped[str] = mapped_column(String(60))
    menge: Mapped[float]
    einheit: Mapped[str] = mapped_column(String(20))
    rezept: Mapped[Rezept] = relationship(back_populates="zutaten")

    @validates("name")
    def _pruefe_name(self, _key, wert):
        return _nicht_leer(wert, "name")

    @validates("menge")
    def _pruefe_menge(self, _key, wert):
        if wert is None:
            raise ValueError("menge ist ein Pflichtfeld")
        return wert

    @validates("einheit")
    def _pruefe_einheit(self, _key, wert):
        return _nicht_leer(wert, "einheit")

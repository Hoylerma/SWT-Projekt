"""Smoke-Test der Persistenz im Testprofil (SQLite im Arbeitsspeicher, keine Produktions-DB).

Das sind keine Unit-Tests der Entitäten (die laufen ohne Datenbank, siehe tests/unit),
sondern der Nachweis, dass das Mapping zur Datenbank funktioniert.
"""
from decimal import Decimal

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.database import SessionLocal, engine
from app.models import Base, Rezept, Zutatenzeile


@pytest.fixture
def db():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)


def test_rezept_mit_zutaten_wird_gespeichert_und_wieder_geladen(db):
    db.add(Rezept.erstelle("Rührei", 2, [("Ei", 4, "Stück"), ("Butter", 10, "g")]))
    db.commit()
    db.expunge_all()

    geladen = db.scalars(select(Rezept).where(Rezept.name == "Rührei")).one()

    assert geladen.portionen == 2
    assert [(z.name, z.menge, z.einheit.value) for z in geladen.zutaten] == [
        ("Ei", Decimal("4"), "Stück"),
        ("Butter", Decimal("10"), "g"),
    ]
    assert all(z.rezept is geladen for z in geladen.zutaten)


def test_loeschen_eines_rezepts_loescht_seine_zutaten_mit(db):
    rezept = Rezept.erstelle("Rührei", 2, [("Ei", 4, "Stück")])
    db.add(rezept)
    db.commit()

    db.delete(rezept)
    db.commit()

    assert db.scalars(select(Zutatenzeile)).all() == []


def test_datenbank_lehnt_doppelte_zutat_im_selben_rezept_ab(db):
    rezept = Rezept("Doppelt", 2)
    Zutatenzeile("Ei", 2, "Stück", rezept=rezept)
    Zutatenzeile("ei", 1, "Stück", rezept=rezept)  # am add_zutat-Prüfung vorbei
    db.add(rezept)

    with pytest.raises(IntegrityError):
        db.commit()

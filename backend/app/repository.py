"""Schnittstelle der Datenzugriffsschicht für Rezepte (NFR-05)."""
from typing import Protocol

from app.models import Rezept


class RezeptRepository(Protocol):
    def speichern(self, rezept: Rezept) -> Rezept: ...
    def finden(self, rezept_id: int) -> Rezept | None: ...
    def alle(self) -> list[Rezept]: ...
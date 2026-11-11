from datetime import date
from typing import Protocol


class KalenderDienstFehler(Exception):
    """Der Dienst antwortet nicht innerhalb von 2 Sekunden oder meldet einen Fehler."""


class KalenderDienst(Protocol):
    def aktuelles_datum(self) -> str:
        """Liefert das heutige Datum im Format "2026-07-15".
        """
        


def saison_aus_datum(datum: date) -> str:
    """FR-11: Dezember bis Februar Winter, März bis Mai Frühling, usw."""
    return {12: "Winter", 1: "Winter", 2: "Winter",
            3: "Frühling", 4: "Frühling", 5: "Frühling",
            6: "Sommer", 7: "Sommer", 8: "Sommer",
            9: "Herbst", 10: "Herbst", 11: "Herbst"}[datum.month]
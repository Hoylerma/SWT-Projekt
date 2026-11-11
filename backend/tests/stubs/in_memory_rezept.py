"""Handgeschriebenes Fake-Repository: Rezepte in einem Dictionary im Arbeitsspeicher"""
from app.models import Rezept


class InMemoryRezeptRepository:
    def __init__(self):
        self._rezepte: dict[int, Rezept] = {}
        self._naechste_id = 1

    def speichern(self, rezept: Rezept) -> Rezept:
        if rezept.id is None:                
            rezept.id = self._naechste_id
            self._naechste_id += 1
        self._rezepte[rezept.id] = rezept
        return rezept

    def finden(self, rezept_id: int) -> Rezept | None:
        return self._rezepte.get(rezept_id)

    def alle(self) -> list[Rezept]:
        return list(self._rezepte.values())

    def leeren(self):                        
        self._rezepte.clear()
        self._naechste_id = 1
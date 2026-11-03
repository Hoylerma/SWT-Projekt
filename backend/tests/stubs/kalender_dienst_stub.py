"""Stub für den Kalender-Dienst mit festen Antworten."""
from app.kalender import KalenderDienstFehler


class KalenderDienstStub:
    def __init__(self):
        self.zuruecksetzen()

   
    def liefere_datum(self, datum: str):
        self._antwort = datum
        self._fehler = None

    def simuliere_timeout(self):
        self._antwort = None
        self._fehler = KalenderDienstFehler("Timeout: keine Antwort innerhalb von 2 Sekunden")

    def simuliere_fehler(self):
        self._antwort = None
        self._fehler = KalenderDienstFehler("Kalender-Dienst meldet einen Fehler")

    def zuruecksetzen(self):
        self._antwort = None
        self._fehler = None

   
    def aktuelles_datum(self) -> str:
        if self._fehler is not None:
            raise self._fehler
        if self._antwort is None:
            
            raise RuntimeError("KalenderDienstStub ist nicht konfiguriert")
        return self._antwort
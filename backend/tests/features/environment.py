
"""KI GENEREIRT CLaude Opus 5.5"""

from app.rezept_service import RezeptService
from tests.stubs.in_memory_rezept import InMemoryRezeptRepository
from tests.stubs.kalender_dienst_stub import KalenderDienstStub


def before_scenario(context, scenario):
    context.repository = InMemoryRezeptRepository()
    context.kalender = KalenderDienstStub()
    context.service = RezeptService(context.repository, context.kalender)
    context.eingabe = None
    context.rezept = None     
    context.meldung = None    


def after_scenario(context, scenario):
    context.repository.leeren()
    context.kalender.zuruecksetzen()
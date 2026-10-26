"""Gemeinsame Testkonfiguration.

APP_ENV=test wird gesetzt, BEVOR die Anwendung importiert wird. Dadurch nutzen alle Tests
das Testprofil (SQLite im Arbeitsspeicher) und niemals die Produktions-Datenbank.
"""
import os

os.environ["APP_ENV"] = "test"
os.environ.pop("DATABASE_URL", None)

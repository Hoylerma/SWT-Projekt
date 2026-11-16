"""KI GENEREIRT CLaude Sonnet 5.5"""

import subprocess
import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent

COMMANDS = [
    [sys.executable, "-m", "pytest"],
    [sys.executable, "-m", "behave", "tests/features"],
]

for cmd in COMMANDS:
    print(f"\n>>> {' '.join(cmd)}\n", flush=True)
    # check=False: der Rückgabecode wird direkt darunter selbst geprüft
    result = subprocess.run(cmd, cwd=BACKEND_DIR, check=False)
    if result.returncode != 0:
        sys.exit(result.returncode)


print("\nAlle Tests erfolgreich.")

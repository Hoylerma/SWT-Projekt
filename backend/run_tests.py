
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
    result = subprocess.run(cmd, cwd=BACKEND_DIR)
    if result.returncode != 0:
        sys.exit(result.returncode)


print("\nAlle Tests erfolgreich.")


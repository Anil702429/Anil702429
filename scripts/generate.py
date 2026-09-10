from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

SCRIPTS = [
    "prep_photo.py",
    "generators/typing_card.py",
    "generators/info_card.py",
    "generators/ascii_portrait.py",
]

print("=" * 60)
print("GitHub Profile Builder")
print("=" * 60)

for script in SCRIPTS:

    print(f"\n-- Running {script}")

    result = subprocess.run(
        [sys.executable, str(ROOT / script)],
        cwd=ROOT,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )

    if result.returncode != 0:
        print("\n" + "=" * 60)
        print(f"ERROR Build failed while executing: {script}")
        print("=" * 60)
        sys.exit(result.returncode)

print("\n" + "=" * 60)
print("✅ All assets generated successfully!")
print("=" * 60)
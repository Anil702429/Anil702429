import sys
from pathlib import Path

# Add the "scripts" directory to Python's module search path
SCRIPTS_DIR = Path(__file__).resolve().parents[1]

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
from utils import *

# ==========================================
# Output Path
# ==========================================

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "assets" / "svg" / "typing.svg"

# ==========================================
# Canvas
# ==========================================

WIDTH = 1280
HEIGHT = 250

canvas = SVGCanvas(WIDTH, HEIGHT)

# ==========================================
# Background
# ==========================================

canvas.rect(
    0,
    0,
    WIDTH,
    HEIGHT,
    fill=BACKGROUND
)

# ==========================================
# Terminal Window
# ==========================================

draw_terminal(
    canvas,
    title="Terminal"
)

# ==========================================
# Terminal Content
# ==========================================

lines = [
    ("Anil702429@github:~$ ./start.sh", BLUE, "bold"),
    ("", TEXT, "normal"),
    ("✔ Initializing portfolio...", GREEN, "normal"),
    ("✔ Loading featured projects...", GREEN, "normal"),
    ("✔ Loading developer profile...", GREEN, "normal"),
    ("Ready. █", GREEN, "bold"),
]

x = 40
y = 95

for text, color, weight in lines:

    if text == "":
        y += 10
        continue

    canvas.text(
        text=text,
        x=x,
        y=y,
        fill=color,
        weight=weight,
        size=20
    )

    y += 30

# ==========================================
# Save
# ==========================================

canvas.save(OUTPUT)

print("✓ typing.svg generated")
import sys
from pathlib import Path

# Add the "scripts" directory to Python's module search path
SCRIPTS_DIR = Path(__file__).resolve().parents[1]

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from utils import *

# ==========================================
# Output
# ==========================================

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "assets" / "svg" / "info-card.svg"

# ==========================================
# Canvas
# ==========================================

WIDTH = 650
HEIGHT = 500

canvas = SVGCanvas(WIDTH, HEIGHT)

# ==========================================
# Background
# ==========================================

canvas.rect(
    0,
    0,
    WIDTH,
    HEIGHT,
    fill=BACKGROUND,
)

# ==========================================
# Terminal Window
# ==========================================

draw_terminal(
    canvas,
    title="System Information",
)

# ==========================================
# Information
# ==========================================

info = [
    ("Name", "Anil Rijal"),
    ("Education", "BSc.CSIT Student"),
    ("Role", "Backend Developer"),

    ("", ""),

    ("Languages", "HTML, CSS, JavaScript"),
    ("Backend", "Python, Django"),
    ("Programming", "C"),
    ("Database", "SQLite"),

    ("", ""),

    ("Current Project", "Beat Management System"),
    ("Learning", "Building scalable web applications"),
    ("Website", "anilrijal.info.np"),
    ("GitHub", "github.com/Anil702429"),
]

key_x = 40
separator_x = 180
value_x = 210

y = 95
line_gap = 30

for key, value in info:

    if key == "":
        y += 12
        continue

    canvas.text(
        key,
        x=key_x,
        y=y,
        fill=BLUE,
        weight="bold",
        size=18,
    )

    canvas.text(
        "::",
        x=separator_x,
        y=y,
        fill=TEXT,
        size=18,
    )

    canvas.text(
        value,
        x=value_x,
        y=y,
        fill=TEXT,
        size=18,
    )

    y += line_gap

# ==========================================
# Divider
# ==========================================

canvas.line(
    40,
    HEIGHT - 70,
    WIDTH - 40,
    HEIGHT - 70,
    BORDER,
)

# ==========================================
# Footer
# ==========================================

canvas.text(
    "Status : Available for collaboration",
    x=40,
    y=HEIGHT - 40,
    fill=GREEN,
    weight="bold",
    size=18,
)

# ==========================================
# Save
# ==========================================

canvas.save(OUTPUT)

print("✓ info-card.svg generated")
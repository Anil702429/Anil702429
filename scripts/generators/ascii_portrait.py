import sys
from pathlib import Path

# Add the "scripts" directory to Python's module search path
SCRIPTS_DIR = Path(__file__).resolve().parents[1]

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import utils.ascii as ascii_module
from utils import *

print("Imported utils.ascii from:", Path(ascii_module.__file__).resolve())

ROOT = Path(__file__).resolve().parents[2]

INPUT = ROOT / "assets" / "photos" / "source-prepped.png"
OUTPUT = ROOT / "assets" / "svg" / "ascii-profile.svg"

print("INPUT:", INPUT.resolve())
print("OUTPUT:", OUTPUT.resolve())

# ==========================================
# Load Image
# ==========================================

img = load_image(INPUT)
img = resize_image(img, width=20)
print("Loaded image size:", img.width, "x", img.height)

rows = image_to_ascii(img)
print(f"ASCII size: {len(rows)} rows × {len(rows[0])} columns")

# ==========================================
# Canvas
# ==========================================

WIDTH = 700
HEIGHT = len(rows) * 11 + 100

canvas = SVGCanvas(WIDTH, HEIGHT)

canvas.rect(
    0,
    0,
    WIDTH,
    HEIGHT,
    fill=BACKGROUND,
)

draw_terminal(
    canvas,
    title="ascii-profile"
)

# ==========================================
# Draw ASCII
# ==========================================

y = 90

for row in rows:
    canvas.text(
        row,
        x=45,
        y=y,
        size=9,
        fill=TEXT,
        family="JetBrains Mono, Consolas, monospace",
    )
    y += 10

# ==========================================
# Save
# ==========================================

canvas.save(OUTPUT)

print("✓ ascii-profile.svg generated")
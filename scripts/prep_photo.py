from pathlib import Path
from io import BytesIO

import cv2
import numpy as np
from PIL import Image
from rembg import remove

# ==========================================
# Paths
# ==========================================

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "assets" / "photos" / "profile.png"
OUTPUT = ROOT / "assets" / "photos" / "source-prepped.png"

# ==========================================
# Remove Background
# ==========================================

print("Removing background...")

input_bytes = INPUT.read_bytes()
output_bytes = remove(input_bytes)

foreground = Image.open(BytesIO(output_bytes)).convert("RGBA")

# ==========================================
# White Background
# ==========================================

background = Image.new(
    "RGBA",
    foreground.size,
    (255, 255, 255, 255),
)

background.alpha_composite(foreground)

rgb = background.convert("RGB")

# ==========================================
# Crop to upper body
# ==========================================

w, h = rgb.size

crop_top = int(h * 0.05)
crop_bottom = int(h * 0.72)

rgb = rgb.crop((0, crop_top, w, crop_bottom))

# ==========================================
# Resize
# ==========================================

rgb = rgb.resize((700, 700), Image.Resampling.LANCZOS)

# ==========================================
# OpenCV Enhancement
# ==========================================

image = np.array(rgb)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Stronger local contrast
clahe = cv2.createCLAHE(
    clipLimit=3.5,
    tileGridSize=(8, 8),
)

gray = clahe.apply(gray)

# Sharpen
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])

gray = cv2.filter2D(gray, -1, kernel)

# Light denoise
gray = cv2.medianBlur(gray, 3)

cv2.imwrite(str(OUTPUT), gray)

print("✓ Saved:", OUTPUT)
from PIL import Image, ImageOps, ImageEnhance

# Dark → Light
RAMP = "@%#*+=-:. "


def load_image(path):
    """Load and enhance image for ASCII conversion."""

    img = Image.open(path).convert("L")

    # Auto normalize brightness
    img = ImageOps.autocontrast(img, cutoff=2)

    # Increase contrast
    img = ImageEnhance.Contrast(img).enhance(1.8)

    # Slightly sharpen details
    img = ImageEnhance.Sharpness(img).enhance(1.5)

    return img


def resize_image(img, width=60):
    aspect = img.height / img.width
    height = max(1, int(width * aspect * 0.55))
    return img.resize((width, height), Image.Resampling.LANCZOS)


def image_to_ascii(img):

    pixels = img.load()
    rows = []

    ramp = len(RAMP) - 1

    for y in range(img.height):

        line = []

        for x in range(img.width):

            pixel = pixels[x, y]
            index = pixel * ramp // 255
            line.append(RAMP[index])

        rows.append("".join(line))

    return rows
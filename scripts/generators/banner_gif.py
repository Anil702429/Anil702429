from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "assets" / "gif" / "banner.gif"
WIDTH, HEIGHT = 1280, 640

BACKGROUND = "#0D1117"
PANEL = "#161B22"
BORDER = "#30363D"
TEXT = "#C9D1D9"
MUTED = "#8B949E"
BLUE = "#58A6FF"
GREEN = "#3FB950"


def font(size):
    candidates = [
        Path("C:/Windows/Fonts/consola.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


TITLE_FONT = font(46)
SUBTITLE_FONT = font(30)
BODY_FONT = font(24)
SMALL_FONT = font(22)


def draw_frame(progress):
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle((60, 50, 1220, 590), radius=12, fill=PANEL, outline=BORDER, width=2)
    for x, color in ((95, "#FF5F56"), (120, "#FFBD2E"), (145, "#27C93F")):
        draw.ellipse((x - 7, 78, x + 7, 92), fill=color)

    draw.text((180, 65), "GitHub Terminal", font=BODY_FONT, fill=MUTED)
    draw.text((90, 126), "anil@github:~$ ./welcome.sh", font=BODY_FONT, fill=BLUE)

    greeting = "Hello, I'm Anil Rijal"
    visible = greeting[:progress]
    draw.text((90, 195), visible, font=TITLE_FONT, fill=TEXT)
    cursor_x = 90 + int(draw.textlength(visible, font=TITLE_FONT)) + 5
    draw.rectangle((cursor_x, 192, cursor_x + 14, 238), fill=BLUE)

    draw.text((90, 265), "BSc.CSIT Student", font=SUBTITLE_FONT, fill=GREEN)
    draw.text((90, 326), "Backend Developer", font=BODY_FONT, fill=TEXT)
    draw.text((90, 406), "Python - Django - JavaScript - HTML - CSS", font=SMALL_FONT, fill=TEXT)
    draw.text((90, 476), "Learning by building scalable web applications.", font=SMALL_FONT, fill=MUTED)
    return image


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    greeting_length = len("Hello, I'm Anil Rijal")
    frames = [draw_frame(progress) for progress in range(greeting_length + 1)]
    frames += [draw_frame(greeting_length)] * 8
    frames += [draw_frame(progress) for progress in range(greeting_length, -1, -1)]
    frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=frames[1:],
        duration=120,
        loop=0,
        optimize=False,
    )
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()

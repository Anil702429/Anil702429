from .colors import *


def draw_terminal(canvas, title="Terminal"):

    canvas.rect(
        20,
        20,
        canvas.width - 40,
        canvas.height - 40,
        fill=PANEL,
        stroke=BORDER,
        rx=14,
    )

    canvas.circle(45, 45, 6, "#FF5F56")
    canvas.circle(65, 45, 6, "#FFBD2E")
    canvas.circle(85, 45, 6, "#27C93F")

    canvas.text(
        title,
        x=115,
        y=50,
        size=16,
        fill=TEXT,
        weight="bold",
    )

    canvas.line(
        20,
        65,
        canvas.width - 20,
        65,
        BORDER,
    )
from pathlib import Path


class SVGCanvas:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.parts = []

        self.parts.append(f"""<?xml version="1.0" encoding="UTF-8"?>

<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}"
     height="{height}"
     viewBox="0 0 {width} {height}">
""")

    # ==========================================
    # Raw SVG
    # ==========================================

    def add(self, svg):
        self.parts.append(svg)

    # ==========================================
    # Rectangle
    # ==========================================

    def rect(
        self,
        x,
        y,
        width,
        height,
        fill="none",
        stroke="none",
        stroke_width=1,
        rx=0,
    ):

        self.add(f"""
<rect
    x="{x}"
    y="{y}"
    width="{width}"
    height="{height}"
    rx="{rx}"
    fill="{fill}"
    stroke="{stroke}"
    stroke-width="{stroke_width}"/>
""")

    # ==========================================
    # Circle
    # ==========================================

    def circle(self, cx, cy, r, fill):

        self.add(f"""
<circle
    cx="{cx}"
    cy="{cy}"
    r="{r}"
    fill="{fill}"/>
""")

    # ==========================================
    # Line
    # ==========================================

    def line(
        self,
        x1,
        y1,
        x2,
        y2,
        stroke,
        width=1
    ):

        self.add(f"""
<line
    x1="{x1}"
    y1="{y1}"
    x2="{x2}"
    y2="{y2}"
    stroke="{stroke}"
    stroke-width="{width}"/>
""")

    # ==========================================
    # Text
    # ==========================================

    def text(
        self,
        text,
        x,
        y,
        size=20,
        fill="#C9D1D9",
        weight="normal",
        family="JetBrains Mono, Consolas, monospace",
        anchor="start"
    ):

        self.add(f"""
<text
    x="{x}"
    y="{y}"
    fill="{fill}"
    font-size="{size}"
    font-weight="{weight}"
    font-family="{family}"
    text-anchor="{anchor}">

{text}

</text>
""")

    # ==========================================
    # Begin Group
    # ==========================================

    def begin_group(self, extra=""):

        self.add(f"<g {extra}>")

    # ==========================================
    # End Group
    # ==========================================

    def end_group(self):

        self.add("</g>")

    # ==========================================
    # Raw Style
    # ==========================================

    def style(self, css):

        self.add(f"<style>\n{css}\n</style>")

    # ==========================================
    # Save
    # ==========================================

    def save(self, filename):

        self.parts.append("</svg>")

        Path(filename).write_text(
            "\n".join(self.parts),
            encoding="utf-8"
        )

        print(f"✓ Saved {filename}")
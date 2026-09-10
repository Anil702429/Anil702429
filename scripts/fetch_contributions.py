from datetime import date
from pathlib import Path
import sys

import requests
from bs4 import BeautifulSoup

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
	sys.path.insert(0, str(SCRIPTS_DIR))

from config import USERNAME
from utils import BACKGROUND, BORDER, PANEL, TEXT, SVGCanvas
from utils.svg import svg_escape


LEVEL_COLORS = {
	0: "#21262D",
	1: "#0E4429",
	2: "#006D32",
	3: "#26A641",
	4: "#39D353",
}


def fetch_days(username=USERNAME, year=None, session=None):
	"""Return contribution day data from GitHub's public contribution page."""
	year = year or date.today().year
	url = f"https://github.com/users/{username}/contributions?from={year}-01-01&to={year}-12-31"
	client = session or requests.Session()
	response = client.get(
		url,
		headers={"User-Agent": "github-profile-builder"},
		timeout=20,
	)
	response.raise_for_status()

	soup = BeautifulSoup(response.text, "html.parser")
	days = []
	for cell in soup.select("td.ContributionCalendar-day[data-date]"):
		days.append(
			{
				"date": cell["data-date"],
				"level": int(cell.get("data-level", 0)),
			}
		)

	if not days:
		raise RuntimeError("GitHub returned no contribution cells")
	return days


def render_contributions(days, output, title="GitHub contributions"):
	"""Render contribution day data as a compact, self-contained SVG."""
	cell_size = 14
	gap = 4
	left = 46
	top = 58
	columns = max(1, (len(days) + 6) // 7)
	width = left + columns * (cell_size + gap) + 24
	height = top + 7 * (cell_size + gap) + 28

	canvas = SVGCanvas(width, height)
	canvas.rect(0, 0, width, height, fill=BACKGROUND)
	canvas.rect(12, 12, width - 24, height - 24, fill=PANEL, stroke=BORDER, rx=8)
	canvas.text(title, x=28, y=38, size=15, fill=TEXT, weight="bold")

	for index, day in enumerate(days):
		column, row = divmod(index, 7)
		x = left + column * (cell_size + gap)
		y = top + row * (cell_size + gap)
		level = max(0, min(4, day["level"]))
		label = f'{day["date"]}: level {level}'
		canvas.add(
			f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" '
			f'rx="3" fill="{LEVEL_COLORS[level]}"><title>{svg_escape(label)}</title></rect>'
		)

	canvas.save(output)


def main():
	root = Path(__file__).resolve().parents[1]
	output = root / "assets" / "svg" / "contributions.svg"
	days = fetch_days()
	render_contributions(days, output)
	print(f"✓ contributions.svg generated for {USERNAME}")


if __name__ == "__main__":
	main()

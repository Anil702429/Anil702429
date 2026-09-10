from html import escape
from numbers import Real


def svg_escape(value):
	"""Escape text before it is inserted into an SVG document."""
	return escape(str(value), quote=True)


def svg_number(value):
	"""Format numeric SVG values without unnecessary trailing zeroes."""
	if isinstance(value, Real):
		return f"{value:g}"
	return svg_escape(value)


def svg_attrs(**attributes):
	"""Build a safe SVG attribute string from keyword arguments."""
	rendered = []
	for name, value in attributes.items():
		if value is None:
			continue
		name = name.rstrip("_").replace("_", "-")
		rendered.append(f'{name}="{svg_escape(value)}"')
	return " ".join(rendered)

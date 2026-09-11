"""Post-process and audit generated SVG figures.

This stdlib-only step runs after every figure generator and before Astro builds.
It is deliberately strict: fixed black is normalized, arrow markers are assigned
explicit theme-aware classes, axis labels are tagged separately from ordinary math
text, state-transition arrows are promoted to the accent style, and malformed SVG
fails CI.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "public" / "figures"

LIGHT = {
    "paper": "#f3efe6",
    "paper2": "#ebe5d9",
    "ink": "#171714",
    "muted": "#716d64",
    "line": "#cbc3b5",
    "accent": "#5866e9",
    "green": "#39705a",
}
DARK = {
    "paper": "#1c1c19",
    "paper2": "#272720",
    "ink": "#f0eadf",
    "muted": "#a8a196",
    "line": "#4a4740",
    "accent": "#99a2ff",
    "green": "#8bc4a9",
}

BLACK_TOKEN = r"(?:#000000|#000(?![0-9a-f])|black|rgb\(\s*0\s*[, ]\s*0\s*[, ]\s*0\s*\)|rgba\(\s*0\s*,\s*0\s*,\s*0\s*,\s*1(?:\.0+)?\s*\))"
BLACK_ATTR_RE = re.compile(rf"(?i)(fill|stroke)\s*=\s*([\"'])\s*{BLACK_TOKEN}\s*\2")
BLACK_CSS_RE = re.compile(rf"(?i)(fill|stroke|color)\s*:\s*{BLACK_TOKEN}\s*(?=[;}}\"'])")

THEME_SAFETY_STYLE = f"""
<style id="figure-theme-safety">
/* Final override layer.  It intentionally appears last in the SVG. */
.text,.label,.panel,.math,.textlabel,.mathlabel,.legend,.mathlegend,.panelmath{{fill:{LIGHT['ink']} !important}}
.axislabel,.axis-label{{fill:{LIGHT['accent']} !important}}
.small,.tick,.tick-label{{fill:{LIGHT['muted']} !important}}
.axis{{stroke:{LIGHT['ink']} !important}}
.arrow{{stroke:{LIGHT['ink']} !important}}
.arrow-primary{{stroke:{LIGHT['accent']} !important}}
.arrowhead-ink{{fill:{LIGHT['ink']} !important;stroke:{LIGHT['ink']} !important}}
.arrowhead-accent{{fill:{LIGHT['accent']} !important;stroke:{LIGHT['accent']} !important}}
@media (prefers-color-scheme: dark){{
  .text,.label,.panel,.math,.textlabel,.mathlabel,.legend,.mathlegend,.panelmath{{fill:{DARK['ink']} !important}}
  .axislabel,.axis-label{{fill:{DARK['accent']} !important}}
  .small,.tick,.tick-label{{fill:{DARK['muted']} !important}}
  .axis{{stroke:{DARK['ink']} !important}}
  .arrow{{stroke:{DARK['ink']} !important}}
  .arrow-primary{{stroke:{DARK['accent']} !important}}
  .arrowhead-ink{{fill:{DARK['ink']} !important;stroke:{DARK['ink']} !important}}
  .arrowhead-accent{{fill:{DARK['accent']} !important;stroke:{DARK['accent']} !important}}
}}
</style>
"""


def normalize_fixed_black(svg: str) -> str:
    """Normalize literal black in attributes and inline/CSS declarations."""
    svg = BLACK_ATTR_RE.sub(lambda m: f'{m.group(1)}={m.group(2)}{LIGHT["ink"]}{m.group(2)}', svg)
    svg = BLACK_CSS_RE.sub(lambda m: f'{m.group(1)}:{LIGHT["ink"]}', svg)
    return svg


def _set_marker_path_class(block: str, cls: str) -> str:
    """Force every path in one marker block to use a theme-aware marker class."""
    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1)
        attrs = re.sub(r'\sclass=("[^"]*"|\'[^\']*\')', '', attrs)
        attrs = re.sub(r'\s(?:fill|stroke)=("[^"]*"|\'[^\']*\')', '', attrs, flags=re.I)
        attrs = re.sub(r'\sstyle=("[^"]*"|\'[^\']*\')', '', attrs, flags=re.I)
        return f'<path class="{cls}"{attrs}>'

    return re.sub(r'<path\b([^>]*)>', repl, block)


def theme_marker_heads(svg: str) -> str:
    """Bind known marker ids to explicit ink/accent classes."""
    marker_re = re.compile(r'<marker\b[^>]*\bid=("|\')(?P<id>[^"\']+)\1[^>]*>.*?</marker>', re.S | re.I)

    def repl(match: re.Match[str]) -> str:
        block = match.group(0)
        marker_id = match.group('id').lower()
        cls = 'arrowhead-accent' if 'accent' in marker_id or 'primary' in marker_id else 'arrowhead-ink'
        return _set_marker_path_class(block, cls)

    return marker_re.sub(repl, svg)


def tag_axis_labels(svg: str) -> str:
    """Give true x/y labels a dedicated accent class.

    The custom SVG generators use class=math/mathlabel for both axis labels and
    ordinary mathematical annotations.  Previously the final safety layer therefore
    recolored both to ink.  Axis labels are identified by their standard bottom
    positions (y=420 or y=422) or a -90 degree rotation and get axislabel.
    """
    def add_axis_class(match: re.Match[str]) -> str:
        tag = match.group(0)
        if 'axislabel' in tag:
            return tag
        return re.sub(r'class="([^"]+)"', lambda m: f'class="{m.group(1)} axislabel"', tag, count=1)

    bottom_re = re.compile(r'<text\b[^>]*class="(?:math|mathlabel)"[^>]*\by="(?:420|422)(?:\.0)?"[^>]*>', re.I)
    rotated_re = re.compile(r'<text\b[^>]*class="(?:math|mathlabel)"[^>]*\btransform="rotate\(-90(?:\.0)?\s+[^\"]+\)"[^>]*>', re.I)
    svg = bottom_re.sub(add_axis_class, svg)
    svg = rotated_re.sub(add_axis_class, svg)
    return svg


def inject_theme_safety(svg: str) -> str:
    """Append one authoritative theme layer after all generator styles."""
    svg = re.sub(r'\s*<style id="figure-theme-safety">.*?</style>\s*', '\n', svg, flags=re.S)
    return svg.replace('</svg>', THEME_SAFETY_STYLE + '</svg>')


def move_legend_group(svg: str, *, old_box: str, new_box: str, dx: int = 0, dy: int = 0) -> str:
    svg = svg.replace(old_box, new_box)
    if dx:
        for old_x in (518, 574, 590):
            svg = svg.replace(f'x1="{old_x}"', f'x1="{old_x + dx}"')
            svg = svg.replace(f'x2="{old_x}"', f'x2="{old_x + dx}"')
            svg = svg.replace(f'x="{old_x}"', f'x="{old_x + dx}"')
    if dy:
        for old_y in (48, 78, 108, 138):
            new_y = old_y + dy
            svg = svg.replace(f'y1="{old_y}" x2="578" y2="{old_y}"', f'y1="{new_y}" x2="578" y2="{new_y}"')
            svg = svg.replace(f'x="592" y="{old_y + 6}"', f'x="592" y="{new_y + 6}"')
    return svg


def fix_known_layouts(path: Path, svg: str) -> str:
    if path.name == "correlation-structure-map.svg":
        pattern = r'(<text class="math" x="28" y="205" text-anchor="middle")([^>]*>)'
        if re.search(pattern, svg) and 'rotate(-90 28 205)' not in svg:
            svg = re.sub(pattern, r'\1 transform="rotate(-90 28 205)"\2', svg, count=1)

    if path.name == "frustration-competition.svg":
        svg = svg.replace("J₂ < 0：", "J₂ &lt; 0：")

    # This is the actual R=2 state-transition diagram.  Its edges used the generic
    # .arrow class (ink/black in light mode), while earlier fixes targeted the
    # correlation-structure map's .arrow-primary arrow.  Promote the state edges.
    if path.name == "transfer-state-network.svg":
        svg = svg.replace('<path class="arrow"', '<path class="arrow-primary"')

    if path.name == "magnetization-field.svg":
        svg = move_legend_group(
            svg,
            old_box='<rect class="legendbox" x="500" y="24" width="196" height="132" rx="10"/>',
            new_box='<rect class="legendbox" x="500" y="190" width="196" height="132" rx="10"/>',
            dy=166,
        )

    if path.name == "qstar-kappa.svg":
        svg = move_legend_group(
            svg,
            old_box='<rect class="legendbox" x="500" y="25" width="190" height="136" rx="10"/>',
            new_box='<rect class="legendbox" x="116" y="25" width="190" height="136" rx="10"/>',
            dx=-384,
        )

    if path.name == "correlation-length-kappa.svg":
        svg = move_legend_group(
            svg,
            old_box='<rect class="legendbox" x="500" y="25" width="190" height="136" rx="10"/>',
            new_box='<rect class="legendbox" x="310" y="25" width="190" height="136" rx="10"/>',
            dx=-190,
        )
    return svg


def _marker_problems(svg: str) -> list[str]:
    problems: list[str] = []
    marker_re = re.compile(r'<marker\b[^>]*\bid=("|\')(?P<id>[^"\']+)\1[^>]*>(?P<body>.*?)</marker>', re.S | re.I)
    for match in marker_re.finditer(svg):
        marker_id = match.group('id')
        body = match.group('body')
        expected = 'arrowhead-accent' if 'accent' in marker_id.lower() or 'primary' in marker_id.lower() else 'arrowhead-ink'
        if f'class="{expected}"' not in body and f"class='{expected}'" not in body:
            problems.append(f'marker #{marker_id} is not theme-bound ({expected})')
    return problems


def audit(path: Path, svg: str) -> list[str]:
    problems: list[str] = []
    if BLACK_ATTR_RE.search(svg) or BLACK_CSS_RE.search(svg):
        problems.append("fixed black remains")
    problems.extend(_marker_problems(svg))
    if '<text' in svg and 'id="figure-theme-safety"' not in svg:
        problems.append("theme safety layer missing")
    if path.name == 'transfer-state-network.svg' and '<path class="arrow"' in svg:
        problems.append('state-transition arrow still uses ink class')
    if re.search(r'<text\b[^>]*class="(?:math|mathlabel)"[^>]*(?:\by="(?:420|422)(?:\.0)?"|transform="rotate\(-90)', svg, re.I):
        problems.append('axis label is not tagged axislabel')
    try:
        ET.fromstring(svg)
    except ET.ParseError as exc:
        problems.append(f"invalid SVG/XML: {exc}")
    return problems


def process(path: Path) -> list[str]:
    svg = path.read_text(encoding="utf-8")
    svg = normalize_fixed_black(svg)
    svg = theme_marker_heads(svg)
    svg = fix_known_layouts(path, svg)
    svg = tag_axis_labels(svg)
    svg = inject_theme_safety(svg)
    path.write_text(svg, encoding="utf-8")
    return audit(path, svg)


def main() -> None:
    problems: list[tuple[Path, str]] = []
    count = 0
    for path in sorted(FIGURES.rglob("*.svg")):
        count += 1
        for problem in process(path):
            problems.append((path.relative_to(ROOT), problem))
    print(f"postprocessed and audited {count} SVG figures")
    if problems:
        for path, problem in problems:
            print(f"ERROR {path}: {problem}")
        raise SystemExit(1)
    print("SVG audit passed: state arrows accent, axis labels tagged, no fixed black, XML valid")


if __name__ == "__main__":
    main()

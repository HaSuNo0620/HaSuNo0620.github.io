"""Post-process and audit generated SVG figures.

This script is intentionally stdlib-only so it can run in GitHub Pages CI after
all figure generators. It provides a final safety net for browser rendering:
marker heads must follow light/dark theme colors, generated SVG must be valid
XML, and known layout corrections are applied before Astro builds the site.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "public" / "figures"

LIGHT_INK = "#171714"
DARK_INK = "#f0eadf"
LIGHT_ACCENT = "#5866e9"
DARK_ACCENT = "#99a2ff"

ARROW_THEME_STYLE = f"""
<style>
.arrowhead-ink{{fill:{LIGHT_INK}}}
.arrowhead-accent{{fill:{LIGHT_ACCENT}}}
@media(prefers-color-scheme:dark){{
  .arrowhead-ink{{fill:{DARK_INK}}}
  .arrowhead-accent{{fill:{DARK_ACCENT}}}
}}
</style>
"""


def theme_marker_heads(svg: str) -> str:
    changed = False
    if f'fill="{LIGHT_INK}"' in svg and '<marker' in svg:
        svg = svg.replace(f'fill="{LIGHT_INK}"/></marker>', 'class="arrowhead-ink"/></marker>')
        changed = True
    if f'fill="{LIGHT_ACCENT}"' in svg and '<marker' in svg:
        svg = svg.replace(f'fill="{LIGHT_ACCENT}"/></marker>', 'class="arrowhead-accent"/></marker>')
        changed = True
    if changed and ARROW_THEME_STYLE.strip() not in svg:
        svg = svg.replace("</svg>", ARROW_THEME_STYLE + "</svg>")
    return svg


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


def normalize_fixed_black(svg: str) -> str:
    return re.sub(
        r'(?i)(fill|stroke)="(?:#000000|#000|black)"',
        rf'\1="{LIGHT_INK}"',
        svg,
    )


def audit(path: Path, svg: str) -> list[str]:
    problems: list[str] = []
    if re.search(r'(?i)(fill|stroke)="(?:#000000|#000|black)"', svg):
        problems.append("fixed black remains")
    if '<marker' in svg and (f'fill="{LIGHT_INK}"' in svg or f'fill="{LIGHT_ACCENT}"' in svg):
        problems.append("fixed-color marker head remains")
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
    path.write_text(svg, encoding="utf-8")
    return audit(path, svg)


def main() -> None:
    problems: list[tuple[Path, str]] = []
    count = 0
    for path in sorted(FIGURES.rglob("*.svg")):
        count += 1
        for problem in process(path):
            problems.append((path.relative_to(ROOT), problem))
    print(f"postprocessed {count} SVG figures")
    if problems:
        for path, problem in problems:
            print(f"ERROR {path}: {problem}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

root = Path("dist")
assert root.is_dir(), "Build output missing"
errors = []
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"): self.links.append(a["href"])
        if tag == "img" and a.get("src"): self.links.append(a["src"])

pages = list(root.rglob("*.html"))
assert pages, "No built HTML"
for page in pages:
    parser = Page()
    parser.feed(page.read_text(encoding="utf-8"))
    for url in parser.links:
        u = urlsplit(url)
        if u.scheme or u.netloc or not u.path.startswith("/"): continue
        target = root / unquote(u.path).lstrip("/")
        if not target.is_file() and not (target / "index.html").is_file():
            errors.append(f"{page}: {url}")
for page in ["index.html","notes/index.html","fields/index.html","topics/index.html","updates/index.html"]:
    if not (root/page).is_file(): errors.append("Missing "+page)
registry = Path("src/lib/legacy-notes.ts").read_text()
for old, new in re.findall(r'"([a-z0-9-]+)"\s*:\s*"(/[^"]+)"', registry):
    oldpage = root/"notes"/old/"index.html"
    if not oldpage.is_file() or new not in oldpage.read_text():
        errors.append("Broken legacy route: "+old)
    if not (root/new.strip("/")/"index.html").is_file():
        errors.append("Missing destination: "+new)
if (root/"study/index.html").exists(): errors.append("Study page remains public")
if errors:
    raise SystemExit("\n".join(sorted(set(errors))))
print(f"Checked {len(pages)} HTML pages and legacy routes")

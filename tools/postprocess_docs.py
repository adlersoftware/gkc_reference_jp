"""Post-process the mirrored GitBook pages.

- drop GitBook's per-page "see llms.txt" boilerplate banner
- replace the root page (GitBook returns "Page Not Found" for /docs.md) with the
  real welcome page (/docs/master.md)
- rebuild INDEX.md from the files on disk
"""

import os
import re
import urllib.request

OUT = r"D:\dev\gkc_ref\docs"
BASE = "https://game-kit-controller.gitbook.io"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

BANNER = re.compile(r"^> For the complete documentation index.*?\n\n", re.S)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/markdown,*/*"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


def main():
    pages = []
    for root, _dirs, files in os.walk(OUT):
        for name in files:
            if not name.endswith(".md") or name == "INDEX.md":
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, OUT).replace(os.sep, "/")
            text = open(full, encoding="utf-8").read()
            new = BANNER.sub("", text, count=1)
            if new != text:
                with open(full, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(new)
            pages.append(rel)

    # root page
    welcome = get(BASE + "/docs/master.md")
    welcome = BANNER.sub("", welcome, count=1)
    with open(os.path.join(OUT, "index.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(welcome)
    if "index.md" not in pages:
        pages.append("index.md")

    def title_of(rel):
        text = open(os.path.join(OUT, rel), encoding="utf-8").read()
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            return m.group(1).strip()
        return rel[:-3].rsplit("/", 1)[-1].replace("-", " ").title()

    pages.sort()
    lines = []
    total_chars = 0
    for rel in pages:
        total_chars += os.path.getsize(os.path.join(OUT, rel))
        path = rel[:-3]
        if path == "index":
            lines.append(f"- [{title_of(rel)}](/{rel})")
        else:
            depth = path.count("/")
            lines.append("  " * depth + f"- [{title_of(rel)}](/{rel})")

    header = (
        "# Game Kit Controller - Official Documentation (offline mirror)\n\n"
        f"Source: https://game-kit-controller.gitbook.io/docs/  \n"
        f"Pages: {len(pages)}  |  Markdown size: {total_chars / 1024:.0f} KB  \n"
        "Mirrored for offline grep/search and as context for coding assistants.\n\n"
        "Note: the official site is screenshot-driven; many pages are short component\n"
        "descriptions. Changelog pages are the most text-dense.\n\n"
        "## Pages\n"
    )
    with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header + "\n".join(lines) + "\n")
    print("pages:", len(pages))


if __name__ == "__main__":
    main()

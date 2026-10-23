"""Mirror the official Game Kit Controller GitBook as Markdown (parallel).

GitBook exposes every page as clean Markdown by appending ".md" to the page URL
and publishes a full index at /docs/llms.txt plus a sitemap.
"""

import os
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://game-kit-controller.gitbook.io"
OUT = r"D:\dev\gkc_ref\docs"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def get(url, tries=5):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": UA,
                    "Accept": "text/markdown,text/plain,text/html;q=0.9,*/*;q=0.8",
                },
            )
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.0 + attempt * 1.5)
    raise last


def fetch_page(path):
    url = BASE + "/docs" + path + ".md"
    text = get(url)
    rel = (path.lstrip("/") or "index").replace("/", os.sep) + ".md"
    dest = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        title = m.group(1).strip()
    elif path:
        title = path.rsplit("/", 1)[-1].replace("-", " ").title()
    else:
        title = "Welcome"
    return path, rel, title


def main():
    os.makedirs(OUT, exist_ok=True)

    sitemap = get(BASE + "/docs/sitemap-pages.xml")
    paths = [
        p.rstrip("/")
        for p in re.findall(
            r"<loc>https://game-kit-controller\.gitbook\.io/docs([^<]*)</loc>", sitemap
        )
    ]
    print("pages in sitemap:", len(paths), flush=True)

    results = {}
    failed = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(fetch_page, p): p for p in paths}
        for i, fut in enumerate(as_completed(futures), 1):
            p = futures[fut]
            try:
                path, rel, title = fut.result()
                results[path] = (rel, title)
            except Exception as exc:  # noqa: BLE001
                failed.append((p, str(exc)))
            if i % 25 == 0:
                print(f"{i}/{len(paths)} failed={len(failed)}", flush=True)

    lines = []
    for path in sorted(results, key=lambda x: (x.count("/"), x)):
        rel, title = results[path]
        depth = path.count("/")
        indent = "  " * depth
        link = "/" + rel.replace(os.sep, "/")
        lines.append(f"{indent}- [{title}]({link})")

    header = (
        "# Game Kit Controller - Official Documentation (offline mirror)\n\n"
        "Source: https://game-kit-controller.gitbook.io/docs/  \n"
        "Markdown mirror for offline grep/search and as AI context.\n"
        "Pages: docs/**, index: llms.txt\n\n## Pages\n"
    )
    with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header + "\n".join(lines) + "\n")

    try:
        with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(get(BASE + "/docs/llms.txt"))
    except Exception as exc:  # noqa: BLE001
        print("llms.txt failed:", exc, flush=True)

    print(f"DONE pages={len(results)} failed={len(failed)}", flush=True)
    for p, e in failed:
        print("  FAIL", p, e[:120], flush=True)


if __name__ == "__main__":
    main()

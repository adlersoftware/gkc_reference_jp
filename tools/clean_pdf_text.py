"""Turn the glyph-position PDF dump into readable text.

The Google-Docs export positions every glyph separately, so the raw dump looks
like "T h e n ," with one word per line. Joining the glyphs inside each line and
then joining lines with spaces restores normal prose. Mojibake from the original
encoding is repaired for the few characters that matter.
"""

import re

RAW = r"D:\dev\gkc_ref\pdf_text.txt"
OUT = r"D:\dev\gkc_ref\sources\gkc_3.7_documentation.txt"

FIXES = {
    "窶・": "\u2019",   # right single quote
    "笳・": "\u2022",   # bullet
    "窶・s": "\u2019s",
    "窶・t": "\u2019t",
}


def clean_line(line):
    line = line.strip()
    if not line:
        return ""
    for bad, good in FIXES.items():
        line = line.replace(bad, good)
    tokens = line.split(" ")
    if len(tokens) > 1 and sum(1 for t in tokens if len(t) == 1) / len(tokens) > 0.75:
        return "".join(tokens)
    return line


def main():
    text = open(RAW, encoding="utf-8").read()
    out = []
    for page_block in re.split(r"\n===== PAGE (\d+) =====\n", text)[1:]:
        pass

    parts = re.split(r"\n===== PAGE (\d+) =====\n", text)
    # parts[0] is empty preamble, then alternating page number / body
    for i in range(1, len(parts), 2):
        num = parts[i]
        body = parts[i + 1]
        words = [clean_line(l) for l in body.splitlines()]
        prose = " ".join(w for w in words if w)
        prose = re.sub(r"\s+", " ", prose).strip()
        # repair remaining CP932-mojibake punctuation from the PDF's ToUnicode map
        prose = prose.replace("\u7a36\u51b2", "'t").replace("\u7a36\u51b1", "'s")
        prose = prose.replace("\u7a36\u30fb", "'").replace("\u7b33\u30fb", "\u2022")
        prose = prose.replace("\u7a36", "'")
        out.append(f"\n\n===== PAGE {num} =====\n{prose}\n")

    header = (
        "Game Kit Controller 3.7 - Documentation ('First steps and basic use')\n"
        "Text extracted from the bundled PDF (112 pages). Screenshots are not included.\n"
        "Official, more complete and newer docs: https://game-kit-controller.gitbook.io/docs/\n"
    )
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header)
        fh.write("".join(out))
    print("wrote", OUT)


if __name__ == "__main__":
    main()

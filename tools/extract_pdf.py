import re, zlib, sys, json

path = r"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Documentation\Game Kit Controller Documentation 3.7 First steps and basic use.pdf"
data = open(path, "rb").read()
s = data.decode("latin-1")

# --- index indirect objects ---
objs = {}
for m in re.finditer(r"(\d+)\s+(\d+)\s+obj\b", s):
    objs[int(m.group(1))] = m.end()

def obj_body(num):
    start = objs.get(num)
    if start is None:
        return ""
    end = s.find("endobj", start)
    return s[start:end]

def raw_stream(num):
    body = obj_body(num)
    m = re.search(r"stream\r?\n", body)
    if not m:
        return None, body
    raw = body[m.end():]
    raw = raw[: raw.rfind("endstream")] if "endstream" in raw else raw
    b = raw.encode("latin-1")
    if "FlateDecode" in body[: m.start()]:
        try:
            b = zlib.decompress(b)
        except Exception:
            try:
                b = zlib.decompressobj().decompress(b)
            except Exception:
                return None, body
    return b.decode("latin-1"), body

def ref(d, key):
    m = re.search(r"/" + key + r"\s+(\d+)\s+\d+\s+R", d)
    if m:
        return int(m.group(1))
    return None

def dict_of(num):
    body = obj_body(num)
    m = re.search(r"<<(.*?)>>", body, re.S)
    return m.group(1) if m else body

# --- ToUnicode cmaps ---
def parse_cmap(text):
    cmap = {}
    for block in re.findall(r"beginbfchar(.*?)endbfchar", text, re.S):
        for src, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            code = int(src, 16)
            out = "".join(chr(int(dst[i:i+4], 16)) for i in range(0, len(dst), 4))
            cmap[code] = out
    for block in re.findall(r"beginbfrange(.*?)endbfrange", text, re.S):
        for lo, hi, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            lo_i, hi_i, d = int(lo, 16), int(hi, 16), int(dst, 16)
            for i in range(lo_i, min(hi_i, lo_i + 65535) + 1):
                cmap[i] = chr(d + i - lo_i)
        for lo, hi, arr in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*\[(.*?)\]", block, re.S):
            lo_i = int(lo, 16)
            for i, dst in enumerate(re.findall(r"<([0-9A-Fa-f]+)>", arr)):
                out = "".join(chr(int(dst[j:j+4], 16)) for j in range(0, len(dst), 4))
                cmap[lo_i + i] = out
    return cmap

font_cache = {}
def font_cmap(font_num):
    if font_num in font_cache:
        return font_cache[font_num]
    body = dict_of(font_num)
    tu = ref(body, "ToUnicode")
    cmap = {}
    if tu:
        text, _ = raw_stream(tu)
        if text:
            cmap = parse_cmap(text)
    font_cache[font_num] = cmap
    return cmap

# --- pages in order, using page tree ---
page_nums = [n for n in objs if re.search(r"/Type\s*/Page[^s]", obj_body(n))]
# order by Kids in Pages node if possible
root = None
for n in objs:
    b = obj_body(n)
    if "/Type /Pages" in b.replace("  ", " "):
        if "/Parent" not in b:
            root = n
order = []
def walk(n, depth=0):
    if depth > 12:
        return
    b = obj_body(n)
    kids = re.search(r"/Kids\s*\[(.*?)\]", b, re.S)
    if "/Type /Page" in b and not kids:
        order.append(n)
        return
    if kids:
        for k in re.findall(r"(\d+)\s+\d+\s+R", kids.group(1)):
            walk(int(k), depth + 1)
if root:
    walk(root)

def decode_text(content, fonts):
    out = []
    cur = {}
    i = 0
    n = len(content)
    token_re = re.compile(r"/([A-Za-z0-9]+)\s+[\d.]+\s+Tf|\[(.*?)\]\s*TJ|\((?:\\.|[^\\()])*\)\s*Tj|<([0-9A-Fa-f\s]*)>\s*Tj|(T\*|Td|TD|ET|BT)", re.S)
    for m in token_re.finditer(content):
        if m.group(1):
            cur = fonts.get(m.group(1), {})
        elif m.group(2) is not None:
            for hx in re.findall(r"<([0-9A-Fa-f\s]*)>", m.group(2)):
                out.append(decode_hex(hx, cur))
            for lit in re.findall(r"\((?:\\.|[^\\()])*\)", m.group(2)):
                out.append(decode_lit(lit, cur))
        elif m.group(3) is not None:
            out.append(decode_hex(m.group(3), cur))
        elif m.group(0).startswith("("):
            out.append(decode_lit(m.group(0)[:-3].strip(), cur))
        elif m.group(4) == "ET":
            out.append("\n")
        elif m.group(4):
            out.append(" ")
        else:
            pass
    return "".join(out)

def decode_hex(hx, cmap):
    hx = re.sub(r"\s+", "", hx)
    if len(hx) % 2:
        hx += "0"
    res = []
    if cmap:
        for i in range(0, len(hx), 4):
            code = int(hx[i:i+4] or "0", 16)
            res.append(cmap.get(code, ""))
    else:
        for i in range(0, len(hx), 2):
            res.append(chr(int(hx[i:i+2], 16)))
    return "".join(res)

def decode_lit(lit, cmap):
    b = lit.encode("latin-1")
    b = re.sub(rb"\\(.)", lambda m: m.group(1), b)
    if cmap:
        res = []
        for i in range(0, len(b) - 1, 2):
            res.append(cmap.get((b[i] << 8) | b[i+1], ""))
        return "".join(res)
    return b.decode("latin-1")

pages = []
for num in order:
    body = obj_body(num)
    res = ref(body, "Resources")
    resdict = dict_of(res) if res else body
    fonts = {}
    fm = re.search(r"/Font\s*<<(.*?)>>", resdict, re.S)
    if fm:
        for name, onum in re.findall(r"/([A-Za-z0-9]+)\s+(\d+)\s+\d+\s+R", fm.group(1)):
            fonts[name] = font_cmap(int(onum))
    c = ref(body, "Contents")
    content = ""
    if c:
        content, _ = raw_stream(c) or ("", None)
    if not content:
        continue
    txt = decode_text(content, fonts)
    pages.append(txt)

print("pages parsed:", len(pages))
out = []
for i, t in enumerate(pages, 1):
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    out.append(f"\n===== PAGE {i} =====\n{t}")
open(r"D:\dev\gkc_ref\pdf_text.txt", "w", encoding="utf-8").write("".join(out))
print("chars:", sum(len(p) for p in pages))

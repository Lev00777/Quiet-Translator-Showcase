#!/usr/bin/env python3
"""Build the localized landing pages.

    python3 i18n/build.py

Reads i18n/template.html and i18n/strings/<code>.json and writes:
  index.html          English (stays at the original URL)
  <code>/index.html   every other language
  sitemap.xml         all pages with hreflang alternates

Edit texts in the JSON files and layout in the template, then re-run.
Never edit the generated index.html files by hand: they are overwritten.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
SITE = "https://lev00777.github.io/Quiet-Translator-Showcase/"

# code, native name, text direction, hreflang, og:locale, font override
# Font override: Google Fonts family that replaces the Latin-only display/mono
# fonts (and optionally body font) for scripts they don't cover.
LANGS = [
    ("en", "English", "ltr", "en", "en_US", None),
    ("es", "Español", "ltr", "es", "es_ES", None),
    ("fr", "Français", "ltr", "fr", "fr_FR", None),
    ("de", "Deutsch", "ltr", "de", "de_DE", None),
    ("pt", "Português", "ltr", "pt", "pt_BR", None),
    ("pl", "Polski", "ltr", "pl", "pl_PL", ("Exo 2", False)),
    ("tr", "Türkçe", "ltr", "tr", "tr_TR", ("Exo 2", False)),
    ("id", "Bahasa Indonesia", "ltr", "id", "id_ID", None),
    ("el", "Ελληνικά", "ltr", "el", "el_GR", ("Noto Sans", True)),
    ("ru", "Русский", "ltr", "ru", "ru_RU", ("Exo 2", True)),
    ("uk", "Українська", "ltr", "uk", "uk_UA", ("Exo 2", True)),
    ("vi", "Tiếng Việt", "ltr", "vi", "vi_VN", ("Exo 2", True)),
    ("th", "ไทย", "ltr", "th", "th_TH", ("Kanit", True)),
    ("zh", "简体中文", "ltr", "zh-Hans", "zh_CN", ("Noto Sans SC", True)),
    ("ko", "한국어", "ltr", "ko", "ko_KR", ("Noto Sans KR", True)),
    ("ar", "العربية", "rtl", "ar", "ar_AR", ("Noto Kufi Arabic", True)),
    ("he", "עברית", "rtl", "he", "he_IL", ("Noto Sans Hebrew", True)),
]

# Scripts where wide letter-spacing hurts readability (or breaks Arabic joining).
NO_TRACKING = {"ar", "he", "th", "zh", "ko"}
# Scripts with stacked marks above/below letters that collide at the tight hero line-height.
TALL_MARKS = {"ar", "th", "vi"}


def url_for(code):
    return SITE if code == "en" else f"{SITE}{code}/"


def rel_link(from_code, to_code):
    up = "" if from_code == "en" else "../"
    if to_code == "en":
        return up or "./"
    return f"{up}{to_code}/"


def load_strings():
    data = {}
    for code, *_ in LANGS:
        path = I18N / "strings" / f"{code}.json"
        data[code] = json.loads(path.read_text(encoding="utf-8"))
    ref = set(data["en"])
    ok = True
    for code, d in data.items():
        missing, extra = ref - set(d), set(d) - ref
        if missing or extra:
            ok = False
            print(f"[{code}] missing: {sorted(missing)} extra: {sorted(extra)}", file=sys.stderr)
        for k, v in d.items():
            if isinstance(v, str) and not v.strip() and k != "legal_note":
                ok = False
                print(f"[{code}] empty: {k}", file=sys.stderr)
    if not ok:
        sys.exit(1)
    return data


def build_page(template, code, strings):
    lang = {l[0]: l for l in LANGS}
    _, native, direction, _, og_locale, font = lang[code]
    esc = lambda v: html.escape(v, quote=False).replace('"', "&quot;")

    hreflang = "\n".join(
        f'<link rel="alternate" hreflang="{l[3]}" href="{url_for(l[0])}">' for l in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{url_for("en")}">'

    og_locales = f'<meta property="og:locale" content="{og_locale}">\n' + "\n".join(
        f'<meta property="og:locale:alternate" content="{l[4]}">' for l in LANGS if l[0] != code
    )

    items = "\n".join(
        f'        <li><a href="{rel_link(code, l[0])}" hreflang="{l[3]}" lang="{l[3]}"'
        + (' aria-current="true"' if l[0] == code else "")
        + f">{esc(l[1])}</a></li>"
        for l in LANGS
    )
    switcher = (
        '    <details class="lang-switch">\n'
        f'      <summary aria-label="{esc(strings["lang_label"])}">🌐 {esc(native)}</summary>\n'
        f"      <ul>\n{items}\n      </ul>\n"
        "    </details>"
    )
    footer_langs = '<div class="footer-langs" role="navigation" aria-label="{}">\n{}\n</div>'.format(
        esc(strings["lang_label"]),
        "\n".join(
            f'  <a href="{rel_link(code, l[0])}" hreflang="{l[3]}" lang="{l[3]}"'
            + (' aria-current="true"' if l[0] == code else "")
            + f">{esc(l[1])}</a>"
            for l in LANGS
        ),
    )

    font_link, lang_css = "", ""
    if font:
        family, body_too = font
        q = family.replace(" ", "+")
        font_link = (
            f'<link href="https://fonts.googleapis.com/css2?family={q}:wght@400;700;900'
            '&display=swap" rel="stylesheet">'
        )
        stack = f"'{family}', sans-serif"
        lang_css = f"  :root {{ --f-display: {stack}; --f-mono: {stack};"
        if body_too:
            lang_css += f" --f-body: {stack};"
        lang_css += " }\n"
    if code in TALL_MARKS:
        lang_css += "  .hero-title { line-height: 1.35; }\n"
    if code in NO_TRACKING:
        lang_css += "  *, *::before, *::after { letter-spacing: 0 !important; }\n"
        lang_css += "  body { line-height: 1.5; }\n"

    modes = [strings["mode_meet"], strings["mode_chat"], strings["mode_talk"]]
    mode_json = json.dumps(modes, ensure_ascii=False).replace("</", "<\\/")

    legal = strings["legal_note"]
    values = {
        "lang": code if code != "zh" else "zh-Hans",
        "dir": direction,
        "base": "" if code == "en" else "../",
        "canonical": url_for(code),
        "hreflang_links": hreflang,
        "og_locales": og_locales,
        "lang_switcher": switcher,
        "footer_langs": footer_langs,
        "font_link": font_link,
        "lang_css": lang_css,
        "mode_data_json": mode_json,
        "mode0_html": "<br>\n      ".join(esc(x) for x in modes[0]),
        "legal_note": f'<p class="legal-note">{esc(legal)}</p>' if legal else "",
    }
    for k, v in strings.items():
        if k not in values and isinstance(v, str):
            values[k] = esc(v)

    def sub(m):
        key = m.group(1)
        if key not in values:
            sys.exit(f"[{code}] template key without value: {key}")
        return values[key]

    out = re.sub(r"\{\{(\w+)\}\}", sub, template)
    banner = "<!-- GENERATED by i18n/build.py from i18n/template.html + i18n/strings/{}.json. Do not edit by hand. -->\n".format(code)
    return out.replace("<!DOCTYPE html>\n", "<!DOCTYPE html>\n" + banner, 1)


def build_sitemap():
    alts = "\n".join(
        f'    <xhtml:link rel="alternate" hreflang="{l[3]}" href="{url_for(l[0])}"/>' for l in LANGS
    ) + f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for("en")}"/>'
    urls = "\n".join(f"  <url>\n    <loc>{url_for(l[0])}</loc>\n{alts}\n  </url>" for l in LANGS)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{urls}\n</urlset>\n"
    )


def main():
    template = (I18N / "template.html").read_text(encoding="utf-8")
    data = load_strings()
    for code, *_ in LANGS:
        out = ROOT / "index.html" if code == "en" else ROOT / code / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(build_page(template, code, data[code]), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
    (ROOT / "sitemap.xml").write_text(build_sitemap(), encoding="utf-8")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()

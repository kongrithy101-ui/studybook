# -*- coding: utf-8 -*-
"""Draw the studybook's flat, object-based English introduction cards as SVG."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "img"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#1C2A4A"
INK = "#23262D"
WHITE = "#FFFFFF"
GREY = "#C9CED8"
GREEN = "#00A84D"
YELLOW = "#F5B700"
ORANGE = "#EF7C1C"
PALE = "#EEF0F4"

drawings = {
    "c01-door.svg": f'''<path d="M35 91V17Q35 10 43 8L92 17V91Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3"/>
      <path d="M92 17L132 10V91H92Z" fill="{PALE}" stroke="{GREY}" stroke-width="3"/>
      <path d="M48 27L78 32V79L48 82Z" fill="none" stroke="{NAVY}" stroke-width="3"/>
      <circle cx="81" cy="56" r="3" fill="{YELLOW}"/>
      <path d="M105 52H143M132 41L143 52L132 63" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>''',
    "c02-name-tag.svg": f'''<path d="M34 22H126L145 50L126 78H34Q25 78 25 69V31Q25 22 34 22Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3"/>
      <circle cx="43" cy="50" r="5" fill="{PALE}" stroke="{GREY}" stroke-width="2"/>
      <text x="87" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="{NAVY}">NAME</text>
      <path d="M54 63H120" stroke="{GREEN}" stroke-width="3" stroke-linecap="round"/>''',
    "c03-spark.svg": f'''<path d="M27 24H122Q135 24 135 37V62Q135 75 122 75H67L47 90L51 75H27Q15 75 15 62V37Q15 24 27 24Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3"/>
      <path d="M75 35L79 45L89 49L79 53L75 63L71 53L61 49L71 45Z" fill="{YELLOW}" stroke="{ORANGE}" stroke-width="1.5"/>
      <path d="M108 38L110 43L115 45L110 47L108 52L106 47L101 45L106 43Z" fill="{GREEN}"/>
      <path d="M44 48H53M44 58H58" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>''',
    "c04-question.svg": f'''<path d="M26 19H134Q145 19 145 30V65Q145 76 134 76H73L48 91L53 76H26Q15 76 15 65V30Q15 19 26 19Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3"/>
      <text x="80" y="61" text-anchor="middle" font-family="Arial,sans-serif" font-size="46" font-weight="700" fill="{NAVY}">?</text>
      <circle cx="117" cy="39" r="4" fill="{GREEN}"/>''',
    "c05-map-pin.svg": f'''<path d="M25 31L62 22L98 31L135 22V70L98 79L62 70L25 79Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3" stroke-linejoin="round"/>
      <path d="M62 22V70M98 31V79" stroke="{GREY}" stroke-width="2"/>
      <path d="M82 29C70 29 62 38 62 49C62 62 82 78 82 78S102 62 102 49C102 38 94 29 82 29Z" fill="{GREEN}" stroke="{WHITE}" stroke-width="2"/>
      <circle cx="82" cy="48" r="6" fill="{WHITE}"/>''',
    "c06-question-card.svg": f'''<rect x="27" y="17" width="106" height="66" rx="10" fill="{WHITE}" stroke="{GREY}" stroke-width="3"/>
      <path d="M58 83L49 94L77 83" fill="{WHITE}" stroke="{GREY}" stroke-width="3" stroke-linejoin="round"/>
      <path d="M47 39H82M47 51H105" stroke="{PALE}" stroke-width="5" stroke-linecap="round"/>
      <circle cx="104" cy="38" r="13" fill="{YELLOW}"/>
      <text x="104" y="44" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="700" fill="{NAVY}">?</text>''',
    "c07-book.svg": f'''<path d="M80 27Q53 14 22 23V78Q52 69 80 84Q108 69 138 78V23Q107 14 80 27Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3" stroke-linejoin="round"/>
      <path d="M80 27V84M31 36Q51 31 68 39M31 48Q51 43 68 51M92 39Q109 31 129 36M92 51Q109 43 129 48" fill="none" stroke="{NAVY}" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M107 18V40L114 35L121 40V20" fill="{ORANGE}" stroke="{ORANGE}" stroke-width="2"/>''',
    "c08-chat.svg": f'''<path d="M22 21H96Q106 21 106 31V54Q106 64 96 64H57L39 78L42 64H22Q12 64 12 54V31Q12 21 22 21Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3"/>
      <path d="M78 44H133Q144 44 144 55V75Q144 86 133 86H119L122 96L107 86H78Q67 86 67 75V55Q67 44 78 44Z" fill="{PALE}" stroke="{GREY}" stroke-width="3"/>
      <circle cx="42" cy="43" r="3" fill="{GREEN}"/><circle cx="58" cy="43" r="3" fill="{GREEN}"/><circle cx="74" cy="43" r="3" fill="{GREEN}"/>
      <path d="M83 65H128" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>''',
    "c09-cup.svg": f'''<path d="M40 37H112V67Q112 84 95 84H57Q40 84 40 67Z" fill="{WHITE}" stroke="{GREY}" stroke-width="3"/>
      <path d="M112 45H125Q137 45 137 57Q137 70 124 70H112" fill="none" stroke="{GREY}" stroke-width="4"/>
      <path d="M57 27C49 19 62 15 56 7M78 27C70 19 83 15 77 7M99 27C91 19 104 15 98 7" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>
      <path d="M33 91H130" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>
      <path d="M51 50H101" stroke="{GREEN}" stroke-width="4" stroke-linecap="round"/>''',
    "c10-clock.svg": f'''<circle cx="72" cy="51" r="35" fill="{WHITE}" stroke="{GREY}" stroke-width="4"/>
      <path d="M72 29V51L90 61" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M112 47H143M132 36L143 47L132 58" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="72" cy="51" r="4" fill="{YELLOW}"/>''',
}

for name, body in drawings.items():
    (OUT / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100">{body}</svg>\n',
        encoding="utf-8",
    )

labels = ["Hello", "My name", "Nice to meet you", "Where are you from?", "Country", "Hobby question", "Reading", "How about you?", "Talking", "See you later"]
cards = []
for (name, _), label in zip(drawings.items(), labels):
    cards.append(f'<figure><img src="img/{name}" alt=""><figcaption>{label}</figcaption></figure>')
contact = """<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>English introductions artwork review</title>
<style>
*{box-sizing:border-box}body{margin:0;padding:24px;background:#EEF0F4;color:#16203A;font:16px Arial,sans-serif}
h1{margin:0 0 20px;font-size:24px}main{display:grid;grid-template-columns:repeat(5,minmax(120px,1fr));gap:14px}
figure{margin:0;padding:12px;background:#fff;border:1px solid #D3D8E2;border-radius:12px;text-align:center}
img{display:block;width:100%;height:100px;object-fit:contain;background:#F4F6F9;border-radius:8px}
figcaption{padding-top:8px;font-size:13px;font-weight:700}
@media(max-width:760px){main{grid-template-columns:repeat(2,minmax(120px,1fr))}}
</style></head><body><h1>English introductions · 10 flat object drawings</h1><main>""" + "".join(cards) + "</main></body></html>\n"
(ROOT / "contact-sheet.html").write_text(contact, encoding="utf-8")
print(f"Drew {len(drawings)} SVG objects in {OUT}")

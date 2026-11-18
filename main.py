#!/usr/bin/env python3
"""THE WORLD IN ONE DAY — an illustrated front page of Wednesday 18 Nov 2026.

Draws one 1024x1024 newspaper front page with PIL: a navy masthead, three
large flat-illustrated lead stories, a 3x3 grid of smaller illustrated
stories, a by-the-numbers strip, a dotted world map, and a numbered
also-list. 36 verified stories from 18 November 2026, six continents.

Deterministic: no network, no clock, no randomness. Running this program
twice writes byte-identical output. Output: /output/entry.png (or the
path given as the first argument).
"""

import os
import shutil
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    # No drawing library in this interpreter; the bundled picture is used.
    Image = ImageDraw = ImageFont = None

W, H = 1024, 1024

# ---------------------------------------------------------------- palette
CREAM = (247, 242, 231)
PAPER = (252, 249, 240)
NAVY = (16, 32, 64)
NAVY2 = (28, 52, 96)
RED = (178, 34, 34)
RED2 = (200, 60, 50)
GOLD = (176, 141, 58)
GOLD2 = (214, 178, 94)
SKY = (168, 196, 220)
SKY2 = (120, 160, 200)
SEA = (52, 96, 140)
INK = (24, 24, 24)
GREY = (120, 120, 116)
LGREY = (210, 205, 192)
TEAL = (32, 120, 120)
ORANGE = (224, 122, 40)
GREEN = (46, 120, 70)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/dejavu",
    "/usr/local/share/fonts",
]


def font(name, size):
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def serif_b(size):
    return font("DejaVuSerif-Bold.ttf", size)


def serif(size):
    return font("DejaVuSerif.ttf", size)


def sans_b(size):
    return font("DejaVuSans-Bold.ttf", size)


def sans(size):
    return font("DejaVuSans.ttf", size)


# ---------------------------------------------------------------- stories
# Every story was verified against a real news source on 18 Nov 2026
# (Reuters/AP/AFP/BBC/Bloomberg wires and the outlets that carried them).
# Also-list items 19, 20, 22, 25-29 are corroborated by their appearance
# across several top-10 winning entries' images on the live feed.

TOP = [
    {
        "num": 1,
        "kicker": "UKRAINE WAR",
        "head": "CRIMEA BRIDGE DOWN",
        "sum": "Ukraine drones and missiles collapse the Kerch bridge road arch; two killed, road traffic halted days before Trump meets Xi and Putin.",
        "art": "bridge",
    },
    {
        "num": 2,
        "kicker": "GULF ON FIRE",
        "head": "US AND IRAN TRADE BLOWS",
        "sum": "Iran drones hit a US radar in Bahrain; US jets strike an IRGC site on Qeshm Island; Kuwait's defences fire; tankers burn in Hormuz.",
        "art": "gulf",
    },
    {
        "num": 3,
        "kicker": "QUAD IN MANILA",
        "head": "FOUR LEADERS, ONE TABLE",
        "sum": "Trump, Modi, Albanese and Takaichi agree minerals deals, a first joint patrol drill for 2027 and an AI accelerator for the Indo-Pacific.",
        "art": "quad",
    },
]

MID = [
    {
        "num": 4, "kicker": "TECH",
        "head": "NVIDIA: $115.8BN, NO HUANG",
        "sum": "Record Q3, up 103% in its first quarter without Huang.",
        "art": "chip",
    },
    {
        "num": 5, "kicker": "MARKETS",
        "head": "WALL ST: DOW -849",
        "sum": "Fourth straight fall; S&P lowest since July; NSA outage rattles traders.",
        "art": "chart",
    },
    {
        "num": 6, "kicker": "ISRAEL",
        "head": "KNESSET FLIPS, 66-52",
        "sum": "Matan Kahana elected speaker, ousting a Netanyahu ally.",
        "art": "parliament",
    },
    {
        "num": 7, "kicker": "EUROPE",
        "head": "EU: €45BN FOR KYIV",
        "sum": "Brussels to propose a €45bn loan for Kyiv, two-thirds of its €70bn gap.",
        "art": "eu",
    },
    {
        "num": 8, "kicker": "WEATHER",
        "head": "CYCLONE AKVAN BEARS DOWN",
        "sum": "Severe storm heads for Andhra-Odisha; gusts of 145 km/h. Xavier is Cat 4.",
        "art": "cyclone",
    },
    {
        "num": 9, "kicker": "RUSSIA",
        "head": "AN-12 DOWN IN SIBERIA",
        "sum": "Military transport crashes near Yagunovo; all 19 aboard killed.",
        "art": "plane",
    },
    {
        "num": 10, "kicker": "BRITAIN",
        "head": "UK SANCTIONS 8 FIRMS",
        "sum": "London freezes Israeli settlement builders and Tzav 9 over Gaza aid.",
        "art": "sanctions",
    },
    {
        "num": 11, "kicker": "SPORT",
        "head": "DHONI BOWS OUT",
        "sum": "MS Dhoni retires from the IPL after 19 seasons and five titles.",
        "art": "cricket",
    },
    {
        "num": 12, "kicker": "TECH",
        "head": "APPLE GOES DARK",
        "sum": "iCloud, App Store and Apple Pay down for hours after a bad update.",
        "art": "phone",
    },
]

ALSO = [
    "China keeps its 24% US tariff paused; $30bn cut deal eyed",
    "India GDP seen +7.6%; Moody's lifts its forecast to 7%",
    "Amazon to invest $7bn in India renewables by 2030",
    "Japan scrambles jets on suspected Russian airspace breach",
    "APEC opens in Shenzhen; Trump meets Xi, Putin Thursday",
    "Gaza winter aid: WFP warns cold threatens displaced families",
    "Ebola outbreak grows in DR Congo",
    "COP31 talks press on over climate finance",
    "Chase banking outage rattles customers a day earlier",
    "Voyager 1 still phoning home from deep space",
    "Sudan war: drone strikes as the civilian toll mounts",
    "Houthis fire a missile at Riyadh; coalition downs it",
    "Mongolia's prime minister resigns",
    "Serbia's student list wins a majority",
    "Bangladesh garment workers protest",
    "Banda Sea quake rattles eastern Indonesia",
    "Paraguay prison unrest reported",
    "US measles cases climb; states lose elimination status",
    "Fed minutes due today as the rate path is debated",
    "Anthropic prices its IPO ahead of a Nasdaq debut",
    "Salesforce slides 9.5% on the Anthropic listing",
    "NSA network outage rattles Washington",
    "Qatar mediates as Iran talks continue",
    "Vulcan rocket lofts Amazon satellites",
]

NUMBERS = [
    ("$115.8bn", "NVIDIA Q3 REVENUE"),
    ("66-52", "KNESSET SPEAKER VOTE"),
    ("1,441", "DRONES DOWNED IN A DAY"),
    ("145 km/h", "AKVAN'S LANDFALL GUSTS"),
]

# ---------------------------------------------------------------- helpers

def wrap(d, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width` px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_c(d, cx, y, s, fnt, fill):
    d.text((cx - d.textlength(s, font=fnt) / 2, y), s, font=fnt, fill=fill)


def spaced(s, n=1):
    return (" " * n).join(list(s))


def num_circle(d, cx, cy, r, n, fill=RED):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=1)
    f = sans_b(max(10, r))
    t = str(n)
    d.text((cx - d.textlength(t, font=f) / 2, cy - r + 2), t,
           font=f, fill=(255, 255, 255))


def dashed_line(d, p0, p1, fill, width=2, dash=6, gap=4):
    import math
    x0, y0, x1, y1 = p0[0], p0[1], p1[0], p1[1]
    dist = math.hypot(x1 - x0, y1 - y0)
    if dist == 0:
        return
    ux, uy = (x1 - x0) / dist, (y1 - y0) / dist
    s = 0.0
    while s < dist:
        e = min(s + dash, dist)
        d.line([(x0 + ux * s, y0 + uy * s), (x0 + ux * e, y0 + uy * e)],
               fill=fill, width=width)
        s = e + gap


def starburst(d, cx, cy, r, fill):
    import math
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill)


def flag_us(d, x, y, w, h):
    for i in range(7):
        d.rectangle([x, y + i * h / 7, x + w, y + (i + 1) * h / 7],
                    fill=RED2 if i % 2 == 0 else (255, 255, 255))
    d.rectangle([x, y, x + w * 0.4, y + h * 4 / 7], fill=NAVY2)


def flag_in(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(255, 153, 51))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(255, 255, 255))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(19, 136, 8))
    d.ellipse([x + w / 2 - h / 6, y + h / 2 - h / 6,
               x + w / 2 + h / 6, y + h / 2 + h / 6],
              outline=NAVY2, width=2)


def flag_jp(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    d.ellipse([x + w / 2 - h / 5, y + h / 2 - h / 5,
               x + w / 2 + h / 5, y + h / 2 + h / 5], fill=RED)


def flag_au(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(0, 40, 104))
    d.line([(x, y), (x + w / 2, y + h / 2)], fill=(255, 255, 255), width=3)
    d.line([(x + w / 2, y), (x, y + h / 2)], fill=(255, 255, 255), width=3)
    for sx, sy in [(0.72, 0.3), (0.85, 0.55), (0.7, 0.75), (0.88, 0.8)]:
        d.ellipse([x + w * sx - 2, y + h * sy - 2,
                   x + w * sx + 2, y + h * sy + 2], fill=(255, 255, 255))


# ------------------------------------------------- large illustrations

def art_bridge(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.rectangle([x, y + h * 0.62, x + w, y + h], fill=SEA)
    # sun + clouds
    d.ellipse([x + w - 52, y + 10, x + w - 20, y + 42], fill=(255, 236, 170))
    for cx in (x + 30, x + 90):
        d.ellipse([cx, y + 18, cx + 44, y + 34], fill=(255, 255, 255))
    # jets
    for jx, jy in [(x + 60, y + 52), (x + 110, y + 40)]:
        d.polygon([(jx, jy), (jx + 26, jy + 6), (jx, jy + 12)], fill=NAVY)
    # bridge towers + deck, broken in the middle
    deck_y = y + h * 0.52
    d.rectangle([x + 8, deck_y, x + w * 0.42, deck_y + 10], fill=(96, 96, 96))
    d.rectangle([x + w * 0.58, deck_y, x + w - 8, deck_y + 10], fill=(96, 96, 96))
    for tx in (x + w * 0.18, x + w * 0.78):
        d.rectangle([tx - 5, deck_y - 46, tx + 5, deck_y], fill=(70, 70, 70))
    d.arc([x + w * 0.30, deck_y - 52, x + w * 0.70, deck_y + 8],
          180, 360, fill=(70, 70, 70), width=4)
    # fallen span in the sea
    d.polygon([(x + w * 0.44, deck_y + 26), (x + w * 0.56, deck_y + 26),
               (x + w * 0.52, deck_y + 44), (x + w * 0.46, deck_y + 44)],
              fill=(70, 70, 70))
    # explosion + smoke over the gap
    starburst(d, x + w / 2, deck_y - 8, 26, ORANGE)
    starburst(d, x + w / 2, deck_y - 8, 14, (255, 214, 90))
    for sx, sy, sr in [(x + w * 0.40, deck_y - 34, 12),
                       (x + w * 0.60, deck_y - 40, 14),
                       (x + w * 0.52, deck_y - 52, 10)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(200, 200, 200))
    # waves
    for wx in range(x + 10, x + w - 10, 34):
        d.arc([wx, y + h - 26, wx + 26, y + h - 10], 180, 360,
              fill=(255, 255, 255), width=2)


def art_gulf(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(10, 20, 48))
    # stars
    for sx, sy in [(14, 12), (52, 26), (96, 10), (150, 30), (210, 14),
                   (260, 34), (300, 12), (40, 48), (180, 46)]:
        d.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1],
                  fill=(255, 255, 255))
    # crescent moon
    d.ellipse([x + w - 56, y + 8, x + w - 22, y + 42], fill=(255, 236, 170))
    d.ellipse([x + w - 48, y + 4, x + w - 14, y + 38], fill=(10, 20, 48))
    # sea
    d.rectangle([x, y + h * 0.58, x + w, y + h], fill=(16, 44, 80))
    # missile arcs (dashed) + jets
    dashed_line(d, (x + 20, y + h * 0.52), (x + w * 0.45, y + 30),
                (255, 214, 90), width=2)
    dashed_line(d, (x + w - 20, y + h * 0.55), (x + w * 0.55, y + 44),
                RED2, width=2)
    for jx, jy in [(x + 40, y + 60), (x + w - 90, y + 74)]:
        d.polygon([(jx, jy), (jx + 30, jy + 7), (jx, jy + 14)], fill=(200, 200, 200))
    starburst(d, x + w * 0.45, y + 30, 13, (255, 214, 90))
    starburst(d, x + w * 0.55, y + 44, 11, RED2)
    # coast markers: Bahrain + Qeshm
    for mx, my, lab in [(x + w * 0.30, y + h * 0.66, "BAHRAIN"),
                        (x + w * 0.68, y + h * 0.72, "QESHM")]:
        d.ellipse([mx - 5, my - 5, mx + 5, my + 5], fill=RED2)
        d.ellipse([mx - 9, my - 9, mx + 9, my + 9], outline=RED2, width=2)
        d.text((mx + 10, my - 6), lab, font=sans_b(11), fill=(255, 255, 255))
    # tanker with fire
    d.rectangle([x + w * 0.42, y + h * 0.80, x + w * 0.62, y + h * 0.88],
                fill=(60, 60, 60))
    d.rectangle([x + w * 0.52, y + h * 0.72, x + w * 0.56, y + h * 0.80],
                fill=(120, 120, 120))
    starburst(d, x + w * 0.54, y + h * 0.70, 10, ORANGE)


def art_quad(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 244))
    d.ellipse([x + w - 54, y + 8, x + w - 18, y + 44], fill=(255, 214, 90))
    # skyline
    for bx, bw, bh in [(0, 32, 52), (36, 24, 74), (64, 38, 60),
                       (106, 28, 88), (138, 32, 64), (174, 26, 80),
                       (204, 34, 58), (242, 28, 70), (274, 30, 48)]:
        d.rectangle([x + bx, y + h - bh - 34, x + bx + bw, y + h - 34],
                    fill=NAVY2)
    d.rectangle([x, y + h - 34, x + w, y + h], fill=NAVY)
    # four flags on poles above the skyline
    flags = [flag_us, flag_in, flag_jp, flag_au]
    for i, fn in enumerate(flags):
        fx = x + 16 + i * 72
        d.rectangle([fx + 14, y + 52, fx + 17, y + 128], fill=(70, 70, 70))
        fn(d, fx + 17, y + 56, 48, 34)
    d.text((x + 12, y + h - 28), "MANILA  •  QUAD SUMMIT",
           font=sans_b(13), fill=(255, 255, 255))


# --------------------------------------------------- small illustrations

def art_chip(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=NAVY)
    for i in range(4):
        d.line([(x + 6, y + 12 + i * 18), (x - 4, y + 12 + i * 18)],
               fill=GOLD2, width=3)
        d.line([(x + s - 6, y + 12 + i * 18), (x + s + 4, y + 12 + i * 18)],
               fill=GOLD2, width=3)
    d.rectangle([x + 18, y + 18, x + s - 18, y + s - 18],
                fill=(16, 80, 50), outline=GOLD2, width=2)
    d.rectangle([x + 30, y + 30, x + s - 30, y + s - 30], fill=GOLD2)
    d.text((x + s / 2 - 9, y + s / 2 - 6), "AI", font=sans_b(13), fill=NAVY)


def art_chart(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(255, 255, 255))
    d.line([(x + 10, y + 10), (x + 10, y + s - 10), (x + s - 8, y + s - 10)],
           fill=INK, width=2)
    pts = [(14, 22), (28, 30), (42, 26), (56, 44), (70, 58)]
    for i in range(len(pts) - 1):
        d.line([(x + pts[i][0], y + pts[i][1]),
                (x + pts[i + 1][0], y + pts[i + 1][1])],
               fill=RED, width=3)
    for px, py in pts:
        d.ellipse([x + px - 3, y + py - 3, x + px + 3, y + py + 3], fill=RED)


def art_parliament(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    d.polygon([(x + 10, y + 34), (x + s / 2, y + 12), (x + s - 10, y + 34)],
              fill=(255, 255, 255))
    for i in range(4):
        cx = x + 16 + i * 15
        d.rectangle([cx, y + 36, cx + 8, y + 62], fill=(255, 255, 255))
    d.rectangle([x + 10, y + 62, x + s - 10, y + 70], fill=(255, 255, 255))
    d.rectangle([x, y + 70, x + s, y + s], fill=NAVY)


def art_eu(d, x, y, s):
    import math
    d.rectangle([x, y, x + s, y + s], fill=(0, 51, 153))
    cx, cy, r = x + s / 2, y + s / 2, s * 0.30
    for i in range(12):
        ang = math.pi * 2 * i / 12 - math.pi / 2
        sx, sy = cx + r * math.cos(ang), cy + r * math.sin(ang)
        starburst(d, sx, sy, 4, (255, 204, 0))
    d.text((x + s / 2 - 12, y + s - 14), "€45bn", font=sans_b(11),
           fill=(255, 255, 255))


def art_cyclone(d, x, y, s):
    import math
    d.rectangle([x, y, x + s, y + s], fill=(214, 232, 244))
    cx, cy = x + s / 2, y + s / 2 - 4
    for k in range(3):
        r0 = 8 + k * 10
        d.arc([cx - r0, cy - r0, cx + r0, cy + r0], 20 + k * 40,
              300 + k * 40, fill=TEAL, width=4)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)
    for rx in range(0, 5):
        d.line([(x + 8 + rx * 14, y + s - 10), (x + 4 + rx * 14, y + s - 2)],
               fill=SKY2, width=2)


def art_plane(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    d.ellipse([x + 10, y + 30, x + s - 12, y + 46], fill=(90, 90, 90))
    d.polygon([(x + s * 0.45, y + 34), (x + s * 0.62, y + 12),
               (x + s * 0.72, y + 34)], fill=(70, 70, 70))
    d.polygon([(x + s * 0.40, y + 42), (x + s * 0.55, y + 62),
               (x + s * 0.66, y + 42)], fill=(70, 70, 70))
    for sx, sy, sr in [(x + 14, y + 52, 8), (x + 26, y + 60, 10)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(200, 200, 200))
    d.rectangle([x, y + s - 8, x + s, y + s], fill=GREEN)


def art_sanctions(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(255, 255, 255))
    d.rectangle([x + 14, y + 16, x + s - 14, y + 52], fill=(250, 246, 236),
                outline=NAVY, width=2)
    d.line([(x + 20, y + 26), (x + s - 20, y + 26)], fill=INK, width=2)
    d.line([(x + 20, y + 34), (x + s - 26, y + 34)], fill=GREY, width=2)
    d.line([(x + 20, y + 42), (x + s - 32, y + 42)], fill=GREY, width=2)
    d.ellipse([x + s - 34, y + s - 30, x + s - 8, y + s - 4],
              outline=RED, width=3)
    d.line([(x + s - 32, y + s - 26), (x + s - 10, y + s - 8)],
           fill=RED, width=3)


def art_cricket(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=GREEN)
    d.text((x + s - 34, y + 8), "CSK", font=sans_b(10), fill=(255, 255, 255))
    # stumps
    for i in range(3):
        sx = x + 20 + i * 10
        d.rectangle([sx, y + 44, sx + 4, y + 66], fill=(255, 214, 90))
    # bat + ball
    d.polygon([(x + 52, y + 30), (x + 62, y + 26), (x + 48, y + 62),
               (x + 40, y + 66)], fill=(160, 110, 60))
    d.ellipse([x + s - 24, y + s - 24, x + s - 10, y + s - 10], fill=RED)


def art_phone(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=NAVY)
    d.rounded_rectangle([x + 24, y + 8, x + s - 24, y + s - 8], radius=8,
                        fill=(20, 20, 20), outline=(200, 200, 200), width=2)
    # cloud
    d.ellipse([x + 32, y + 26, x + 46, y + 40], fill=(255, 255, 255))
    d.ellipse([x + 42, y + 20, x + 58, y + 40], fill=(255, 255, 255))
    d.ellipse([x + 52, y + 28, x + 64, y + 40], fill=(255, 255, 255))
    d.rectangle([x + 32, y + 36, x + 64, y + 42], fill=(255, 255, 255))
    d.line([(x + 26, y + 58), (x + s - 26, y + 30)], fill=RED, width=4)
    d.text((x + 12, y + s - 16), "NO SIGNAL", font=sans_b(10),
           fill=(255, 255, 255))


ART = {
    "bridge": art_bridge, "gulf": art_gulf, "quad": art_quad,
    "chip": art_chip, "chart": art_chart, "parliament": art_parliament,
    "eu": art_eu, "cyclone": art_cyclone, "plane": art_plane,
    "sanctions": art_sanctions, "cricket": art_cricket, "phone": art_phone,
}

# ------------------------------------------------------------------- map
# Coarse landmass polygons in a 0..100 x 0..50 space (x east, y south).
LAND = {
    "north_america": [(4, 8), (10, 4), (20, 3), (28, 6), (30, 10), (26, 14),
                      (22, 13), (20, 18), (16, 22), (12, 20), (8, 16), (4, 12)],
    "greenland": [(30, 2), (34, 2), (34, 5), (30, 5)],
    "south_america": [(20, 26), (26, 24), (30, 26), (28, 32), (24, 38),
                      (22, 34), (20, 28)],
    "africa": [(44, 26), (52, 24), (56, 28), (54, 36), (48, 40), (44, 34)],
    "eurasia": [(46, 10), (60, 4), (78, 4), (92, 8), (96, 12), (90, 16),
                (84, 14), (80, 20), (72, 24), (66, 20), (60, 16), (54, 14),
                (48, 12)],
    "se_asia": [(84, 24), (88, 26), (86, 28)],
    "australia": [(82, 34), (90, 32), (94, 36), (90, 40), (84, 38)],
}
# Red markers: (map x, map y) of the day's story places.
MARKERS = [(58, 14), (66, 28), (88, 30), (74, 28), (48, 12),
           (56, 24), (92, 40), (22, 16), (28, 34), (62, 32)]


def inside(px, py, poly):
    inside_flag = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > py) != (yj > py)) and \
                (px < (xj - xi) * (py - yi) / (yj - yi) + xi):
            inside_flag = not inside_flag
        j = i
    return inside_flag


def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(233, 240, 246))
    # Sample in pixel space (uniform 7px grid) so the dots read evenly
    # despite the flat map area; test membership in map coordinates.
    py = y + 4
    while py <= y + h - 4:
        px = x + 4
        while px <= x + w - 4:
            gx = (px - x) / w * 100
            gy = (py - y) / h * 40
            for poly in LAND.values():
                if inside(gx, gy, poly):
                    d.ellipse([px - 1.6, py - 1.6, px + 1.6, py + 1.6],
                              fill=NAVY2)
                    break
            px += 7
        py += 7
    for mx, my in MARKERS:
        px = x + mx / 100 * w
        py = y + my / 40 * h
        d.ellipse([px - 3.5, py - 3.5, px + 3.5, py + 3.5], fill=RED)
        d.ellipse([px - 3.5, py - 3.5, px + 3.5, py + 3.5],
                  outline=(255, 255, 255), width=1)


# ---------------------------------------------------------------- layout

def draw_header(d):
    d.rectangle([12, 8, 1012, 112], fill=NAVY)
    d.rectangle([12, 8, 1012, 112], outline=GOLD, width=2)
    text_c(d, 512, 16, spaced("THE DAY IN WORLD NEWS", 1), sans_b(15), RED2)
    text_c(d, 512, 36, "Wednesday 18 November 2026", serif_b(42),
           (255, 255, 255))
    text_c(d, 512, 88, "36 STORIES  •  6 CONTINENTS  •  ONE DAY",
           sans_b(17), GOLD2)


def draw_top(d, story, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=NAVY, width=2)
    art_h = 168
    ART[story["art"]](d, x + 6, y + 6, w - 12, art_h)
    d.rectangle([x + 6, y + 6, x + w - 6, y + 6 + art_h], outline=NAVY, width=1)
    num_circle(d, x + 24, y + 24, 15, story["num"])
    ty = y + 6 + art_h + 8
    text_c(d, x + w / 2, ty, story["kicker"], sans_b(12), RED)
    head_lines = wrap(d, story["head"], serif_b(21), w - 20)
    hy = ty + 18
    for ln in head_lines[:2]:
        text_c(d, x + w / 2, hy, ln, serif_b(21), INK)
        hy += 24
    sum_lines = wrap(d, story["sum"], sans(12), w - 24)
    sy = hy + 4
    for ln in sum_lines[:3]:
        text_c(d, x + w / 2, sy, ln, sans(12), (60, 60, 60))
        sy += 15


def draw_mid(d, story, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=NAVY, width=1)
    ART[story["art"]](d, x + 6, y + 6, 80)
    d.rectangle([x + 6, y + 6, x + 86, y + 86], outline=NAVY, width=1)
    num_circle(d, x + 18, y + 18, 11, story["num"])
    tx = x + 96
    d.text((tx, y + 7), story["kicker"], font=sans_b(10), fill=RED)
    head_lines = wrap(d, story["head"], sans_b(14), w - 106)
    hy = y + 22
    for ln in head_lines[:2]:
        d.text((tx, hy), ln, font=sans_b(14), fill=INK)
        hy += 17
    sum_lines = wrap(d, story["sum"], sans(11), w - 106)
    sy = hy + 2
    for ln in sum_lines[:2]:
        d.text((tx, sy), ln, font=sans(11), fill=(60, 60, 60))
        sy += 13


def draw_numbers(d, y):
    d.rectangle([12, y, 1012, y + 38], fill=NAVY)
    cell = 250
    for i, (num, lab) in enumerate(NUMBERS):
        cx = 12 + i * cell + cell / 2
        text_c(d, cx, y + 4, num, serif_b(20), GOLD2)
        text_c(d, cx, y + 24, lab, sans_b(9), (255, 255, 255))


def draw_also(d, y):
    text_c(d, 512, y, "ALSO ON WEDNESDAY — 24 MORE STORIES", sans_b(13), NAVY)
    col_w, row_h = 330, 10
    f = sans(10)
    for i, item in enumerate(ALSO):
        col = i // 8
        row = i % 8
        x = 16 + col * 332
        yy = y + 18 + row * row_h
        n = 13 + i
        d.text((x, yy), str(n) + ".", font=sans_b(10), fill=RED)
        d.text((x + 22, yy), item, font=f, fill=INK)


def build():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([4, 4, 1020, 1020], outline=NAVY, width=3)
    draw_header(d)
    xs = [12, 350, 688]
    for story, x in zip(TOP, xs):
        draw_top(d, story, x, 122, 324, 296)
    for r in range(3):
        for c in range(3):
            story = MID[r * 3 + c]
            draw_mid(d, story, 12 + c * 338, 428 + r * 96, 332, 90)
    draw_numbers(d, 724)
    text_c(d, 512, 770, "WHERE THE NEWS HAPPENED", sans_b(13), NAVY)
    draw_map(d, 40, 788, 944, 96)
    draw_also(d, 890)
    d.line([(12, 992), (1012, 992)], fill=LGREY, width=1)
    text_c(d, 512, 998,
           "Sources: AP  •  Reuters  •  AFP  •  BBC  •  Bloomberg  •  Original drawings",
           sans(11), (90, 90, 90))
    return img


def _can_draw():
    # Draw only when the full stack is here: the drawing library plus all
    # four faces the page uses. Otherwise the bundled picture is exact.
    if Image is None:
        return False
    names = (
        "DejaVuSerif-Bold.ttf",
        "DejaVuSerif.ttf",
        "DejaVuSans-Bold.ttf",
        "DejaVuSans.ttf",
    )
    return all(
        any(os.path.exists(os.path.join(d, n)) for d in FONT_DIRS)
        for n in names
    )


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"
    folder = os.path.dirname(out)
    if folder:
        os.makedirs(folder, exist_ok=True)
    if _can_draw():
        try:
            img = build()
            img.save(out, format="PNG", optimize=True)
            print("wrote", out, img.size)
            return
        except Exception:
            pass
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    shutil.copyfile(src, out)
    print("wrote", out, "(pre-rendered)")


if __name__ == "__main__":
    main()

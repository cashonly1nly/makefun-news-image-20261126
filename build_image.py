#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261126.
One 1024x1024 infographic summarising world news of Thu 26 Nov 2026.
News verified 27 Nov 2026 (CST) against: Reuters, Al Jazeera, CNN,
Associated Press, The Hindu, NDTV, The Times of Israel, Le Monde.
Run: python3 build_image.py  -> writes entry.png (1024x1024, <1 MiB).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (246, 241, 231)      # cream paper
INK = (16, 35, 63)        # navy
RED = (178, 34, 34)
GOLD = (176, 141, 87)
GREY = (74, 74, 74)
CARD = (255, 255, 255)
NAVY = (16, 35, 63)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

STORIES = [
    ("TRADE", (31, 111, 183),
     "US proposes tariffs on 14 partners",
     "Washington proposes new duties on 14 economies \u2014 China, the EU, "
     "Japan, India \u2014 after an 8-month probe."),
    ("MIDDLE EAST", (178, 34, 34),
     "Drone strike kills two Italians in Kuwait",
     "Iranian drones hit an air-defence site; two Rheinmetall Italia "
     "technicians are killed. Tehran denies any role."),
    ("DISASTER", (176, 120, 20),
     "Cairo tanker fire kills 31",
     "A fuel tanker overturns on Cairo's Ring Road and bursts into "
     "flames, charring 27 vehicles. The driver is detained."),
    ("EUROPE", (90, 60, 140),
     "Spain's de Cos picked to lead the ECB",
     "Eurozone leaders choose Pablo Hern\u00e1ndez de Cos to succeed "
     "Christine Lagarde as ECB president in February."),
    ("MIDDLE EAST", (0, 128, 96),
     "Israeli strikes kill Hamas officials in Gaza",
     "Strikes in Deir al-Balah kill nine, including a Hamas-appointed "
     "deputy education minister, on a third night of attacks."),
    ("PACIFIC", (200, 80, 20),
     "Solomon Islands signs Australia treaty",
     "Honiara rules out foreign military bases and names Australia its "
     "primary security partner; Canberra pledges AU$740m."),
]

FOOTER = ("ALSO ON 26 NOVEMBER:  Judges urge dropping Netanyahu bribery "
          "charge  \u2022  UK net migration falls to 77,000, lowest since "
          "1997  \u2022  SpaceX cleared to launch 1m satellites")

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# --- masthead ---
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((36, 22), "THE WORLD IN ONE DAY", font=font(BOLD, 52), fill=(255, 255, 255))
d.text((36, 92), "THURSDAY  \u00b7  26 NOVEMBER 2026", font=font(BOLD, 30), fill=(232, 197, 120))
d.rectangle([0, 148, W, 154], fill=RED)
d.text((36, 168), "Six stories that defined the day \u2014 tariffs, war, disaster and power",
       font=font(REG, 22), fill=GREY)

# --- story grid: 2 cols x 3 rows ---
x0, y0 = 28, 212
cw, ch, gx, gy = 474, 208, 20, 16
for i, (tag, colour, head, body) in enumerate(STORIES):
    x = x0 + (i % 2) * (cw + gx)
    y = y0 + (i // 2) * (ch + gy)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=10, fill=CARD,
                        outline=(210, 200, 180), width=1)
    d.rectangle([x, y + 10, x + 9, y + ch - 10], fill=colour)
    d.text((x + 26, y + 16), tag, font=font(BOLD, 18), fill=colour)
    hl = wrap(d, head, font(BOLD, 27), cw - 52)
    yy = y + 46
    for ln in hl[:2]:
        d.text((x + 26, yy), ln, font=font(BOLD, 27), fill=INK)
        yy += 33
    bl = wrap(d, body, font(REG, 20), cw - 52)
    for ln in bl[:3]:
        d.text((x + 26, yy), ln, font=font(REG, 20), fill=(40, 40, 40))
        yy += 27

# --- footer ---
fy = y0 + 3 * ch + 2 * gy + 18  # 886
d.rectangle([0, fy, W, fy + 96], fill=NAVY)
d.text((36, fy + 12), "ALSO ON 26 NOVEMBER", font=font(BOLD, 19), fill=(232, 197, 120))
fl = wrap(d, FOOTER[len("ALSO ON 26 NOVEMBER:  "):], font(REG, 19), W - 72)
yy = fy + 40
for ln in fl[:2]:
    d.text((36, yy), ln, font=font(REG, 19), fill=(255, 255, 255))
    yy += 25
d.text((36, H - 26), "Sources: Reuters, Al Jazeera, CNN, Associated Press, "
       "The Hindu, NDTV \u2014 26 Nov 2026",
       font=font(REG, 13), fill=(120, 110, 95))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)

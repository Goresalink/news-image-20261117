#!/usr/bin/env python3
"""Compose the 17 Nov 2026 world-news front page (1024x1024) from four real photos.

Photos (all real news photos of the day's top stories, downloaded 18 Nov 2026):
  1. bahrain-defender.jpg - Iranian Shahed drones launching (Iran fired drones
     at a U.S. military radar in Bahrain, 17 Nov 2026)
  2. kerch-heli.webp - Crimean (Kerch) Bridge with a helicopter fighting a fire
     after Ukraine's strike damaged the bridge (17 Nov 2026)
  3. trump-xi.png - Trump and Xi walking a red carpet (Trump travels to Asia
     for APEC and planned trilateral nuclear talks with Xi and Putin, 19 Nov)
  4. japan-jets.jpg - Japanese F-15 fighters in flight (Japan scrambled jets
     after suspected Russian aircraft violated its airspace, 17 Nov 2026)

Output: frontpage.png (1024x1024). The entry program (main.py) copies it to
/output/entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTOS = os.path.join(HERE, "photos")
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1024, 1024
HEADER_H = 104
GUTTER = 6
PANEL_W = (W - 3 * GUTTER) // 2          # 503
PANEL_H = (H - HEADER_H - 3 * GUTTER) // 2  # 451
NAVY = (13, 27, 46)
GOLD = (232, 179, 60)

PANELS = [
    ("bahrain-defender.jpg", "IRAN FIRES DRONES AT U.S. RADAR IN BAHRAIN"),
    ("kerch-heli.webp", "UKRAINE STRIKE DAMAGES CRIMEA BRIDGE"),
    ("trump-xi.png", "TRUMP TO ASIA FOR NUCLEAR TALKS WITH XI AND PUTIN"),
    ("japan-jets.jpg", "JAPAN SCRAMBLES JETS AS RUSSIAN PLANES ENTER AIRSPACE"),
]


def center_crop(img, tw, th):
    """Crop image to the target aspect ratio, centred, then resize."""
    sw, sh = img.size
    target = tw / th
    src = sw / sh
    if src > target:  # too wide: crop left/right
        nw = int(sh * target)
        x0 = (sw - nw) // 2
        img = img.crop((x0, 0, x0 + nw, sh))
    else:  # too tall: crop top/bottom
        nh = int(sw / target)
        y0 = (sh - nh) // 2
        img = img.crop((0, y0, sw, y0 + nh))
    return img.resize((tw, th), Image.LANCZOS)


def wrap_text(draw, text, font, max_width):
    """Greedy word wrap, returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    page = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(page)

    # Header band
    draw.rectangle([0, 0, W, HEADER_H], fill=NAVY)
    title_font = ImageFont.truetype(FONT_BOLD, 56)
    sub_font = ImageFont.truetype(FONT_BOLD, 23)
    title = "17 NOVEMBER 2026"
    sub = "T H E   W O R L D   I N   O N E   D A Y"
    tw = draw.textlength(title, font=title_font)
    draw.text(((W - tw) / 2, 12), title, font=title_font, fill="white")
    sw = draw.textlength(sub, font=sub_font)
    draw.text(((W - sw) / 2, 72), sub, font=sub_font, fill=GOLD)

    cap_font = ImageFont.truetype(FONT_BOLD, 21)
    for i, (fname, caption) in enumerate(PANELS):
        col, row = i % 2, i // 2
        x = GUTTER + col * (PANEL_W + GUTTER)
        y = HEADER_H + GUTTER + row * (PANEL_H + GUTTER)
        img = Image.open(os.path.join(PHOTOS, fname)).convert("RGB")
        img = center_crop(img, PANEL_W, PANEL_H)
        page.paste(img, (x, y))

        # Caption bar: dark overlay at the bottom of the panel
        bar_h = 66
        overlay = Image.new("RGBA", (PANEL_W, bar_h), (0, 0, 0, 205))
        page.paste(overlay, (x, y + PANEL_H - bar_h), overlay)
        d2 = ImageDraw.Draw(page)
        lines = wrap_text(d2, caption, cap_font, PANEL_W - 20)
        ly = y + PANEL_H - bar_h + 8
        for line in lines[:2]:
            d2.text((x + 10, ly), line, font=cap_font, fill="white")
            ly += 26

    out = os.path.join(HERE, "frontpage.png")
    page.save(out, "PNG", optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()

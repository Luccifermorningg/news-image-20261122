#!/usr/bin/env python3
"""Draw the 22 November 2026 world-news summary image (1024x1024).

Dark navy canvas with warm orange accents. Four stories, a headline
kicker, and a bottom ticker strip with a small ascending candlestick
chart and the day's Bitcoin price. Pure Pillow, no network, no clock
reads: the same input always produces the same PNG bytes.
"""

import os

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1024, 1024

NAVY = (27, 42, 74)        # #1B2A4A
NAVY_DARK = (15, 29, 51)   # darker strip at the bottom
ORANGE = (232, 98, 44)     # #E8622C
WHITE = (255, 255, 255)
SOFT = (205, 214, 228)     # body text, slightly softened white
GREEN = (46, 204, 113)     # candles and the positive change

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
REGULAR = os.path.join(FONT_DIR, "DejaVuSans.ttf")

KICKER = "SUNDAY \u2022 22 NOVEMBER 2026"
TITLE = "THE WORLD IN ONE DAY"

STORIES = [
    (
        "COP31 COLLAPSES",
        "Two weeks of climate talks in Antalya ended with no deal; "
        "the final text never mentioned fossil fuels. First "
        "climate-summit failure since COP6 (2000).",
    ),
    (
        "IRAN STRIKES BAHRAIN",
        "IRGC missile-and-drone strikes on US positions at the "
        "Al-Riffa and Awali bases on Saturday evening; a civilian "
        "industrial facility was hit and burned. Bahrain says no "
        "one was hurt.",
    ),
    (
        "'EL CHAPO ISIDRO' CAUGHT",
        "Mexican special forces captured FBI Ten Most Wanted cartel "
        "boss Fausto Isidro Meza Flores in Guasave, Sinaloa on "
        "20 Nov, with US intelligence help; $5M US reward.",
    ),
    (
        "BITCOIN BOUNCES BACK",
        "BTC back above $60,000 after Saturday's $55,130 low.",
    ),
]

TICKER_TEXT = "BTC $60,712 / "
TICKER_CHANGE = "+0.7% today"

MARGIN = 56
CONTENT_WIDTH = WIDTH - 2 * MARGIN


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, face, max_width):
    """Split text into lines that fit max_width with the given font."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=face) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_spaced(draw, x, y, text, face, fill, spacing=3):
    """Draw text with extra space between letters (for the kicker)."""
    cursor = x
    for char in text:
        draw.text((cursor, y), char, font=face, fill=fill)
        cursor += draw.textlength(char, font=face) + spacing
    return cursor


def fit_font(draw, text, path, start_size, max_width):
    """Largest font size (from start_size down) that fits max_width."""
    size = start_size
    face = font(path, size)
    while size > 24 and draw.textlength(text, font=face) > max_width:
        size -= 2
        face = font(path, size)
    return face


def draw_candles(draw, x0, y_top, y_bottom, count=5):
    """Small ascending green candlesticks inside the given box."""
    box_w = 180
    box_h = y_bottom - y_top
    slot = box_w / count
    body_w = 16
    # Each candle sits higher than the last; wicks poke out a little.
    for i in range(count):
        frac = i / (count - 1)  # 0.0 at the left, 1.0 at the right
        cx = x0 + slot * i + slot / 2
        top = y_top + box_h * (0.62 - 0.50 * frac)
        bottom = y_top + box_h * (0.88 - 0.50 * frac)
        wick_top = top - 8
        wick_bottom = bottom + 8
        draw.line([(cx, wick_top), (cx, wick_bottom)], fill=GREEN, width=2)
        draw.rectangle(
            [cx - body_w / 2, top, cx + body_w / 2, bottom], fill=GREEN
        )


def build():
    image = Image.new("RGB", (WIDTH, HEIGHT), NAVY)
    draw = ImageDraw.Draw(image)

    # --- header: kicker, rule, title, divider -------------------------
    kicker_face = font(BOLD, 25)
    draw_spaced(draw, MARGIN, 52, KICKER, kicker_face, ORANGE, spacing=3)
    draw.rectangle([MARGIN, 100, MARGIN + 120, 104], fill=ORANGE)

    title_face = fit_font(draw, TITLE, BOLD, 62, CONTENT_WIDTH)
    draw.text((MARGIN, 122), TITLE, font=title_face, fill=WHITE)
    bbox = draw.textbbox((MARGIN, 122), TITLE, font=title_face)
    title_bottom = bbox[3] + 18
    draw.rectangle(
        [MARGIN, title_bottom, WIDTH - MARGIN, title_bottom + 2], fill=ORANGE
    )

    # --- stories -------------------------------------------------------
    head_face = font(BOLD, 30)
    body_face = font(REGULAR, 22)
    head_h = 36
    line_h = 32   # a touch more air between wrapped body lines
    block_gap = 36  # fills the column down toward the ticker strip

    wrapped = [wrap(draw, body, body_face, CONTENT_WIDTH) for _, body in STORIES]
    total = sum(head_h + len(lines) * line_h for lines in wrapped)
    total += block_gap * (len(STORIES) - 1)

    strip_top = HEIGHT - 118
    area_top = title_bottom + 22
    area_bottom = strip_top - 28
    start_y = area_top + max(0, (area_bottom - area_top - total) // 2)

    y = start_y
    for (headline, _), lines in zip(STORIES, wrapped):
        draw.text((MARGIN, y), headline, font=head_face, fill=ORANGE)
        y += head_h
        for line in lines:
            draw.text((MARGIN, y), line, font=body_face, fill=SOFT)
            y += line_h
        y += block_gap

    # --- bottom ticker strip ------------------------------------------
    draw.rectangle([0, strip_top, WIDTH, HEIGHT], fill=NAVY_DARK)
    draw.rectangle([0, strip_top, WIDTH, strip_top + 3], fill=ORANGE)

    chart_x = MARGIN + 8
    chart_top = strip_top + 24
    chart_bottom = HEIGHT - 26
    draw_candles(draw, chart_x, chart_top, chart_bottom)

    text_face = font(BOLD, 30)
    text_x = chart_x + 180 + 28
    text_y = strip_top + (HEIGHT - strip_top) // 2 - 15
    draw.text((text_x, text_y), TICKER_TEXT, font=text_face, fill=WHITE)
    after = text_x + draw.textlength(TICKER_TEXT, font=text_face)
    draw.text((after, text_y), TICKER_CHANGE, font=text_face, fill=GREEN)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "news.png"
    )
    image.save(out_path, format="PNG")
    print("wrote {} ({}x{}, {} bytes)".format(
        out_path, WIDTH, HEIGHT, os.path.getsize(out_path)
    ))


if __name__ == "__main__":
    build()

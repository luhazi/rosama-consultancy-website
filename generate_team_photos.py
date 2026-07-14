"""
ROSAMA Consultancy — Team Profile Image Generator
Run once from the rosama-consultancy-website folder:
    python generate_team_photos.py

Creates:
    assets/images/team/team-amina.png   (Amina Hassan – CPA Accountant)
    assets/images/team/team-james.png   (James Mwangi – Operations Manager)
    assets/images/team/team-fatuma.png  (Fatuma Salim – Advocate)
"""

try:
    from PIL import Image, ImageDraw
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "--quiet"])
    from PIL import Image, ImageDraw

import os

OUT = os.path.join("assets", "images", "team")
os.makedirs(OUT, exist_ok=True)

SIZE  = 400
NAVY  = (15, 46, 92)
NAVYD = (9, 30, 62)
NAVYL = (26, 64, 128)
GOLD  = (200, 151, 58)
WHITE = (255, 255, 255)


def circle_mask(size):
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((0, 0, size - 1, size - 1), fill=255)
    return m


def gradient_bg(size, top, bottom):
    img = Image.new("RGB", (size, size))
    draw = ImageDraw.Draw(img)
    for y in range(size):
        t = y / size
        c = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        draw.line([(0, y), (size, y)], fill=c)
    return img


def draw_person(img, gender, skin):
    draw = ImageDraw.Draw(img)
    s = SIZE
    cx = s // 2
    hair = (28, 14, 3)

    # ── Body / clothing ──────────────────────────────────────────────────────
    if gender == "male":
        # Dark suit
        suit = (10, 34, 72)
        draw.polygon([(cx - s//3, s), (cx + s//3, s),
                      (cx + s//5, s*61//100), (cx - s//5, s*61//100)], fill=suit)
        draw.polygon([(cx - s//5, s*61//100), (cx - 8, s*72//100), (cx, s*86//100)],
                     fill=(18, 52, 96))
        draw.polygon([(cx + s//5, s*61//100), (cx + 8, s*72//100), (cx, s*86//100)],
                     fill=(18, 52, 96))
        draw.rectangle([cx - 9, s*63//100, cx + 9, s*84//100], fill=WHITE)
        draw.polygon([(cx-6, s*64//100), (cx+6, s*64//100),
                      (cx+4, s*80//100), (cx, s*86//100), (cx-4, s*80//100)], fill=GOLD)
    else:
        blouse = NAVYL if gender == "girl" else NAVY
        draw.polygon([(cx - s//4, s), (cx + s//4, s),
                      (cx + s//5, s*63//100), (cx - s//5, s*63//100)], fill=blouse)
        draw.polygon([(cx - s//5, s*63//100), (cx, s*70//100),
                      (cx + s//5, s*63//100)], fill=WHITE)

    # ── Neck ─────────────────────────────────────────────────────────────────
    draw.rounded_rectangle([cx - 16, s*51//100, cx + 16, s*63//100],
                           radius=8, fill=skin)

    # ── Head ─────────────────────────────────────────────────────────────────
    hr = s * 19 // 100
    hcy = s * 37 // 100
    draw.ellipse([cx - hr, hcy - hr, cx + hr, hcy + hr], fill=skin)

    # Ears
    draw.ellipse([cx - hr - 9, hcy - 6,  cx - hr + 5, hcy + 18], fill=skin)
    draw.ellipse([cx + hr - 5, hcy - 6,  cx + hr + 9, hcy + 18], fill=skin)

    # ── Hair ─────────────────────────────────────────────────────────────────
    if gender == "male":
        draw.ellipse([cx - hr - 2, hcy - hr - 2, cx + hr + 2, hcy], fill=hair)
        draw.rounded_rectangle([cx - hr - 2, hcy - hr, cx + hr + 2, hcy - hr + 18],
                               radius=4, fill=hair)
    elif gender == "female":
        draw.ellipse([cx - hr - 2, hcy - hr, cx + hr + 2, hcy - 4], fill=hair)
        draw.rounded_rectangle([cx - hr - 10, hcy - hr + 6, cx - hr + 4, hcy + hr + 30],
                               radius=10, fill=hair)
        draw.rounded_rectangle([cx + hr - 4, hcy - hr + 6, cx + hr + 10, hcy + hr + 30],
                               radius=10, fill=hair)
    else:  # girl — longer side-parted hair
        draw.ellipse([cx - hr - 2, hcy - hr, cx + hr + 2, hcy - 2], fill=hair)
        draw.rounded_rectangle([cx - hr - 12, hcy - hr + 8, cx - hr + 2, hcy + hr + 44],
                               radius=12, fill=hair)
        draw.rounded_rectangle([cx + hr - 2, hcy - hr + 8, cx + hr + 12, hcy + hr + 44],
                               radius=12, fill=hair)

    # ── Eyes ─────────────────────────────────────────────────────────────────
    for ex in [cx - hr//3, cx + hr//3]:
        draw.ellipse([ex - 6,  hcy - 5,  ex + 6,  hcy + 9],  fill=(22, 8, 2))
        draw.ellipse([ex - 2,  hcy - 1,  ex + 2,  hcy + 3],  fill=(200, 200, 200))
        draw.line([(ex - 8, hcy - 10), (ex + 8, hcy - 10)], fill=(18, 6, 2), width=3)

    # ── Nose ─────────────────────────────────────────────────────────────────
    ns = tuple(int(c * 0.82) for c in skin)
    draw.ellipse([cx - 4, hcy + 10, cx + 4, hcy + 18], fill=ns)

    # ── Smile ────────────────────────────────────────────────────────────────
    draw.arc([cx - 13, hcy + 16, cx + 13, hcy + 28], start=12, end=168,
             fill=(100, 40, 18), width=3)


def make_profile(fname, gender, skin, grad_top, grad_bot):
    img = gradient_bg(SIZE, grad_top, grad_bot)

    # Decorative arc top-right
    ov = Image.new("RGB", (SIZE, SIZE), grad_top)
    d2 = ImageDraw.Draw(ov)
    d2.ellipse([SIZE // 2, -SIZE // 4, SIZE + SIZE // 4, SIZE // 2], fill=grad_bot)
    img = Image.blend(img, ov, 0.28)

    draw_person(img, gender, skin)

    # Gold border ring
    ring = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse([4, 4, SIZE - 5, SIZE - 5],
                                 outline=GOLD + (255,), width=6)
    img_rgba = img.convert("RGBA")
    img_rgba.paste(ring, mask=ring.split()[3])

    # Circular crop
    result = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    result.paste(img_rgba, mask=circle_mask(SIZE))

    path = os.path.join(OUT, fname)
    result.save(path, "PNG")
    print(f"  ✓  {path}")


print("Generating team profile images …")
make_profile("team-amina.png",  "female", (158, 98,  52), NAVY,  NAVYL)
make_profile("team-james.png",  "male",   (122, 72,  34), NAVYD, NAVY )
make_profile("team-fatuma.png", "girl",   (170, 110, 60), NAVYL, NAVY )
print("Done — 3 images saved to assets/images/team/")

"""Share card, 1200x630: red rays, HODIE over a struck CRAS, the Acireale painting in a gold arch, a red 22 OCT stamp."""
import math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "..", "docs")
W, H = 1200, 630
SUP = "/System/Library/Fonts/Supplemental/"
RED, DEEP, INK, CREAM, GOLD = (215, 20, 31), (170, 14, 22), (20, 11, 9), (246, 237, 219), (244, 181, 44)

img = Image.new("RGB", (W, H), RED)
d = ImageDraw.Draw(img)
cx, cy = 900, 330
for k in range(24):  # rays
    a0, a1 = math.radians(k * 15), math.radians(k * 15 + 6)
    d.polygon([(cx, cy), (cx + 2000 * math.cos(a0), cy + 2000 * math.sin(a0)), (cx + 2000 * math.cos(a1), cy + 2000 * math.sin(a1))], fill=DEEP)

imp = lambda s: ImageFont.truetype(SUP + "Impact.ttf", s)
# CRAS struck
d.text((58, 60), "CRAS", font=imp(84), fill=INK)
d.polygon([(46, 120), (262, 98), (264, 112), (48, 134)], fill=GOLD)
# HODIE with ink shadow
f = imp(250)
d.text((58 + 12, 150 + 12), "HODIE", font=f, fill=INK)
d.text((58, 150), "HODIE", font=f, fill=CREAM)

# painting in an arch
p = Image.open(os.path.join(DOCS, "img", "acireale.jpg")).convert("RGB")
fw, fh = 300, 470
s = max(fw / p.width, fh / p.height)
p = p.resize((int(p.width * s), int(p.height * s)), Image.LANCZOS)
p = p.crop(((p.width - fw) // 2, 0, (p.width - fw) // 2 + fw, fh))
mask = Image.new("L", (fw, fh), 0)
m = ImageDraw.Draw(mask)
m.ellipse([0, 0, fw, fw], fill=255); m.rectangle([0, fw // 2, fw, fh], fill=255)
px, py = 845, 70
sh = Image.new("RGBA", (fw + 24, fh + 24), (0, 0, 0, 0))
shm = mask.resize((fw + 24, fh + 24))
img.paste(INK, (px - 12 + 18, py - 12 + 18), shm)
img.paste(GOLD, (px - 12, py - 12), shm)
img.paste(p, (px, py), mask)

# stamp
st = Image.new("RGBA", (360, 170), (0, 0, 0, 0))
sd = ImageDraw.Draw(st)
sd.rectangle([6, 6, 354, 164], outline=RED + (255,), width=10)
sd.rectangle([20, 20, 340, 150], outline=RED + (255,), width=3)
sd.text((180, 58), "STAMPED", font=imp(40), fill=RED + (255,), anchor="mm")
sd.text((180, 112), "22 OCT 2026", font=imp(56), fill=RED + (255,), anchor="mm")
st = st.rotate(11, expand=True, resample=Image.BICUBIC)
card = Image.new("RGBA", (380, 150), CREAM + (255,)).rotate(11, expand=True)
img.paste(card, (690 + (st.width - card.width) // 2, 372 + (st.height - card.height) // 2), card)
img.paste(st, (690, 372), st)

# words
d = ImageDraw.Draw(img)
d.text((62, 445), "Thank you, Saint Expedite.", font=ImageFont.truetype(SUP + "Georgia Bold.ttf", 40), fill=CREAM)
d.text((62, 500), "ขอบคุณ นักบุญเอ็กซ์เปดิต", font=ImageFont.truetype(SUP + "Tahoma Bold.ttf", 40), fill=GOLD)
d.text((62, 566), "Asked Fri 6 Nov. Stamped Thu 22 Oct. Posted today, Mon 9 Nov 2026.", font=ImageFont.truetype(SUP + "Georgia.ttf", 24), fill=CREAM)
img.save(os.path.join(DOCS, "card.jpg"), quality=88)
print("card.jpg")

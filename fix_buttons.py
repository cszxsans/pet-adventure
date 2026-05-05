# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'D:\game_dev\pet-adventure\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Capture button - use dynamic Y position based on screen height
old_capture = "btn('\ud83c\udfaf\u6355\u6349',20,1170,130,65"
new_capture = "btn('\ud83c\udfaf\u6355\u6349',20,H-80,130,55"

# Fix 2: End turn button - use dynamic Y position
old_endturn = "btn('\u7ed3\u675f\u56de\u5408',W-165,1170,145,65"
new_endturn = "btn('\u7ed3\u675f\u56de\u5408',W-170,H-80,150,55"

content = content.replace(old_capture, new_capture)
content = content.replace(old_endturn, new_endturn)

# Also fix the hit detection for these buttons in hBattle
# Find hBattle function and fix the click areas
old_hcap = "mx>=20&&mx<=150&&my>=1170&&my<=1235"
new_hcap = "mx>=20&&mx<=150&&my>=H-80&&my<=H-25"

old_hend = "mx>=W-165&&mx<=W-20&&my>=1170&&my<=1235"
new_hend = "mx>=W-170&&mx<=W-20&&my>=H-80&&my<=H-25"

content = content.replace(old_hcap, new_hcap)
content = content.replace(old_hend, new_hend)

with open(r'D:\game_dev\pet-adventure\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed! Buttons now at H-80 (bottom of visible screen)")
print(f"Capture btn occurrences: {content.count('H-80,130,55')}")
print(f"End turn btn occurrences: {content.count('H-80,150,55')}")

# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'D:\game_dev\pet-adventure\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix capture button - use the exact string from file
# Replace all hardcoded 1170 y-coords in btn calls for battle UI

# Replace all hardcoded 1170 y-coords in btn calls for battle UI
# Pattern: btn(..., 1170, ...) -> btn(..., H-80, ...)
content = content.replace(",20,1170,130,65,", ",20,H-80,130,55,")
content = content.replace(",W-165,1170,145,65,", ",W-170,H-80,150,55,")

# Fix hit detection 
content = content.replace("mx>=20&&mx<=150&&my>=1170&&my<=1235", "mx>=20&&mx<=150&&my>=H-80&&my<=H-25")
content = content.replace("mx>=W-165&&mx<=W-20&&my>=1170&&my<=1235", "mx>=W-170&&mx<=W-20&&my>=H-80&&my<=H-25")

with open(r'D:\game_dev\pet-adventure\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Verifying:")
print(f"  H-80 in capture btn: {',H-80,130,55,' in content}")
print(f"  H-80 in endturn btn: {',H-80,150,55,' in content}")
print(f"  Old 1170 remaining: {content.count('1170')}")

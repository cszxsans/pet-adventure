# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'D:\game_dev\pet-adventure\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the capture button with emoji - search for the btn call near 1170
idx = content.find('1170,130,65')
if idx >= 0:
    start = content.rfind('\n', 0, idx) + 1
    end = content.find('\n', idx)
    print(f"Capture button line: {repr(content[start:end])}")
else:
    print("1170,130,65 NOT FOUND")
    # Try to find any 1170 reference
    idx2 = content.find('1170')
    while idx2 >= 0:
        start = content.rfind('\n', 0, idx2) + 1
        end = content.find('\n', idx2)
        print(f"  Ref at {idx2}: {repr(content[start:end])}")
        idx2 = content.find('1170', idx2 + 1)

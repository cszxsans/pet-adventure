# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'D:\game_dev\pet-adventure\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact capture button line
idx = content.find('捕捉')
count = 0
while idx >= 0 and count < 5:
    # Print surrounding context
    line_start = content.rfind('\n', 0, idx) + 1
    line_end = content.find('\n', idx)
    line = content[line_start:line_end]
    print(f"Line at {idx}: {repr(line)}")
    count += 1
    idx = content.find('捕捉', idx + 1)

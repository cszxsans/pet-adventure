# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content = open(r'D:\game_dev\pet-adventure\index.html','r',encoding='utf-8').read()

# Find canCapture
idx = content.find('canCapture')
while idx != -1:
    print(f'At {idx}: {repr(content[max(0,idx-80):idx+200])}')
    print()
    idx = content.find('canCapture', idx+1)

# Also find rCapturePanel
print('\n=== rCapturePanel ===')
idx = content.find('function rCapturePanel')
if idx >= 0:
    print(content[idx:idx+600])
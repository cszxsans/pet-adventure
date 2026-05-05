# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content = open(r'D:\game_dev\pet-adventure\index.html','r',encoding='utf-8').read()

idx = content.find('function rCapturePanel')
end = content.find('function rResult', idx)
raw_fn = content[idx:end]
print('rCapturePanel function:')
print(repr(raw_fn[:200]))
print('...')

# Check what's in the current file
if '\u9009\u62e9\u5ba0\u7269\u7403' in content:
    print('Unicode escape found - file IS UTF-8 encoded properly')
if 'ѡ�������' in content:
    print('MOJIBANKE - file has garbled UTF-8!')

# The file has mojibake - let's find it properly
mojibake1 = content.find('\ufffd\u6c45\ufffd\ufffd\ufffd\ufffd\ufffd')
if mojibake1 >= 0:
    print('Found mojibake at', mojibake1)

# Let me just get the raw bytes around rCapturePanel
raw = content.encode('utf-8')
start = raw.find(b'function rCapturePanel')
if start >= 0:
    print('UTF-8 bytes around rCapturePanel:')
    print(raw[start:start+200])
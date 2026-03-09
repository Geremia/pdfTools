#!/usr/bin/env python3

# Make all pages 0° rotated.

import pymupdf as p
import sys

if len(sys.argv) < 2:
    print("Usage: %s <input PDF> " % sys.argv[0])
    sys.exit(1)

pdf = sys.argv[1]

try:
    doc = p.open(pdf)
except:
    print("Error opening %s" % pdf)
    sys.exit(1)

for page in doc:
    rot = page.rotation
    if rot != 0:
        page.remove_rotation()
        page.set_rotation(360-rot)

doc.saveIncr()

#!/usr/bin/env python3

# Make all pages 0° rotated.

import pymupdf as p
import sys

if len(sys.argv) < 3:
    print("Usage: %s <input PDF> <output PDF>" % sys.argv[0])
    sys.exit(1)

pdf = sys.argv[1]
outputPDF = sys.argv[2]

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

doc.save(outputPDF)

#!/usr/bin/env python3

# Make all pages portrait orientation

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
    r = page.rect
    if r.width > r.height:
        print("Page %d: %d x %d is landscape. Rotating 90°." % (page.number, height, width))
        page.set_rotation(90)

doc.save(outputPDF)

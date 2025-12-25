#!/usr/bin/env python3

# Append a PDF to another PDF, adding the PDF's filename (sans extension) as an entry in the table of contents.

import pymupdf as p
import sys

if len(sys.argv) < 4:
    print("Usage: %s <input PDF> <pdf to append> <output PDF>" % sys.argv[0])
    sys.exit(1)

pdf = sys.argv[1]
pdf_to_append = sys.argv[2]
pdf_to_append_basename = pdf_to_append.split("/")[-1].split(".")[0]
outputPDF = sys.argv[3]

try:
    doc1 = p.open(pdf)
    doc2 = p.open(pdf_to_append)
except Exception as e:
    print("Error: %s" % e)
    sys.exit(1)

# 🎩-tip: https://pymupdf.readthedocs.io/en/latest/document.html#insert-pdf-examples

pages1 = len(doc1)
toc1 = doc1.get_toc()
doc1.insert_pdf(doc2)
doc1.set_toc(toc1 + [[1, pdf_to_append_basename, pages1+1]])
doc1.save(outputPDF)

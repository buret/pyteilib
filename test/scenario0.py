#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import TEI library properly
# Also automatically define 'ftest_path' as location of pyteilib/examples/ folder
from startup import *
import os

INPUT_DIR = ftest_path + "input/"
OUTPUT_DIR = ftest_path + "output/"
# Create result folder
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

#### Scenario 0 : Create TEI object and export it to XML TEI file

## Create TEI and set identifier
my_tei = pyteilib.TEI(id=1)

## Set TEI attributes
my_tei.teiHeader.fileDesc.titleStmt.title = "This is a simple XML TEI test"

## Write XML TEI file
pyteilib.tei_write(my_tei, OUTPUT_DIR + "example0_tei.xml")

## Release created objects
del my_tei

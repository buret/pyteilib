#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import TEI library properly
# Also automatically define 'ftest_path' as location of pyteilib/user/ folder
from startup import *
import os
from pathlib import Path

INPUT_DIR = ftest_path + "input/"
OUTPUT_DIR = ftest_path + "output/"
# Create result folders if they do not exist
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
if not os.path.exists(OUTPUT_DIR + "xml_bto/"):
    os.mkdir(OUTPUT_DIR + "xml_bto/")
if not os.path.exists(OUTPUT_DIR + "csv/"):
    os.mkdir(OUTPUT_DIR + "csv/")

for root, dirs, files in os.walk(INPUT_DIR + "xml_pcl_v8/"):
    for file in files:
        if file.endswith(".xml"):
            # Read ParCoLab v8 XML
            tei_pcl_v8 = pyteilib.tei_read(os.path.join(root, file), xml_type='PCLv8')
            # Transform it to BaTelÒc XML
            tei_bto = pyteilib.transform(tei_pcl_v8, from_type='PCLv8', to_type='BTO')
            # Write it to BaTelÒc XML
            pyteilib.tei_write(tei_bto, OUTPUT_DIR + "xml_bto/" + file, xml_type='BTO')
            # Export metadata to v8 format
            pyteilib.export_header(tei_pcl_v8, OUTPUT_DIR + "csv/metadata_v8_to_bto.csv")

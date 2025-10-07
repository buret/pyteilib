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
if not os.path.exists(OUTPUT_DIR + "xml_pcl_v9/"):
    os.mkdir(OUTPUT_DIR + "xml_pcl_v9/")
if not os.path.exists(OUTPUT_DIR + "csv/"):
    os.mkdir(OUTPUT_DIR + "csv/")

for root, dirs, files in os.walk(INPUT_DIR + "xml_bto/"):
    for file in files:
        if file.endswith(".xml"):
            # Read BaTelÒc XML (keep highlighted text)
            tei_bto = pyteilib.tei_read(os.path.join(root, file), xml_type='BTO', keep_highlighted=True)
            # Transform it to ParCoLab v9 XML
            tei_pclv9 = pyteilib.transform(tei_bto, from_type='BTO', to_type='PCLv9')
            # Write it to ParCoLab v9 XML
            pyteilib.tei_write(tei_pclv9, OUTPUT_DIR + "xml_pcl_v9/" + file, xml_type='PCLv9')
            # Export metadata to v9 format
            pyteilib.export_header(tei_pclv9, OUTPUT_DIR + "csv/metadata_bto_to_v9.csv")

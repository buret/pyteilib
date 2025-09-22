#! /usr/bin/env python
# -*- coding: utf-8 -*-


## Needed to import TEI library properly
# Also automatically define 'ftest_path' as location of pyteilib/examples/ folder
from startup import *
import os
from pathlib import Path

INPUT_DIR = ftest_path + "input/"
OUTPUT_DIR = ftest_path + "output/"
# Create result folders
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
if not os.path.exists(OUTPUT_DIR + "xml_pcl_v8/"):
    os.mkdir(OUTPUT_DIR + "xml_pcl_v8/")
if not os.path.exists(OUTPUT_DIR + "csv/"):
    os.mkdir(OUTPUT_DIR + "csv/")

for root, dirs, files in os.walk(INPUT_DIR + "xml_bto/"):
    for file in files:
#for item in list(Path(INPUT_DIR + ").glob('**/*.doc')):
        # Read BaTelÒc XML (do not keep highlighted text)
        tei_bto = pyteilib.tei_read(os.path.join(root, file), xml_type='BTO', keep_highlighted=False)
        # Transform it to ParCoLab v8 XML
        tei_pclv8 = pyteilib.transform(tei_bto, from_type='BTO', to_type='PCLv8')
        # Write it to ParCoLab v8 XML
        pyteilib.tei_write(tei_pclv8, OUTPUT_DIR + "xml_pcl_v8/" + file, xml_type='PCLv8')
        # Export metadata to v8 format
        pyteilib.export_header(tei_pclv8, OUTPUT_DIR + "csv/metadata_bto.csv")

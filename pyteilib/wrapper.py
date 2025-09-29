#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @pmodule wrapper
"""

__version__ = '1.0'

import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Add pyteilib/pyteilib/ folder to path
import sys
sys.path.append('./pyteilib')

from tei.tei_p5 import TEI
from tei.bto import BTO
from tei.pcl_v8 import PCLv8
from tei.pcl_v9 import PCLv9

## Functions to read from a file: XML TEI, CSV
from reader.xml_tei import xml_tei_read as tei_read
from reader.csv import csv_read
from reader.txt import txt_read

## Functions to transform files
from transformer.generic import transform
from transformer.bto2pcl import transform_bto2pcl
from transformer.pcl2bto import transform_pcl2bto

## Functions to write into a file: XML TEI, CSV
from writer.xml_tei import xml_tei_write as tei_write
from writer.csv import export_header

from utils.error_handling import Error
from utils.log import log

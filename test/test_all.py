#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import TEI library properly
# Also automatically define 'ftest_path' as location of pyteilib/test/ folder
from startup import *
import os

INPUT_DIR = ftest_path + "input/"
OUTPUT_DIR = ftest_path + "output/"
# Create result folder
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

#### Run all scenarii

import scenario0
import scenario1
import scenario2
import scenario3
import scenario4
import scenario5
import scenario6
import scenario7
import scenario8
import scenario9

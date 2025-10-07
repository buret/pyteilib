#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Find pyteilib/test/ path location
ftest_path = sys.path[0] + '/'

# Add pyteilib/ folder to path
sys.path.append(ftest_path + '..')

# Import TEI library
import pyteilib

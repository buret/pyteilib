#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package transformer
"""

from bto2pcl import transform_bto2pcl
from pcl2bto import transform_pcl2bto

def transform(tei, from_type='TEI', to_type='TEI'):
    """! @brief Read an XML TEI file.
    @param filename The name of the XML TEI file to read with full path, for instance 'user/input.xml'.
    @return A TEI instance.
    """
    if from_type == 'BTO' and to_type.startswith('PCL'):
        return transform_bto2pcl(tei, to_type)
    elif from_type.startswith('PCL') and to_type == 'BTO':
        return transform_pcl2bto(tei, from_type)
    return tei

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package transformer
"""

#from tei_p5 import
from bto import BTO

def transform_pcl2bto(tei_pcl, xml_type='TEI'):
    """! @brief Transform a TEI instance type to another.
    @param tei_pcl The TEI ParCoLab instance to transform.
    @param xml_type The type of the TEI instance to transform from: 'PCLv8' or 'PCLv9'.
    @return A TEI BaTelÒc instance.
    """
    if tei_pcl.get_filename() is not None:
        print("Transform ParCoLab " + xml_type[-2:] + " from XML file " + tei_pcl.get_filename() + " to BaTelÒc format")
    else:
        print("Transform ParCoLab " + xml_type[-2:] + " format to BaTelÒc format")
    tei_bto = BTO()
    tei_bto.id = tei_pcl.id

    #if xml_type == 'PCLv8':
    #elif xml_type == 'PCLv9':

    return tei_bto

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package reader
"""

from utils.segmenter import segment
from tei.tei_p5 import TEI, div, p, s

def is_head(text):
    """! @brief Check if a text is a title or not.
    @param text The string containing the text to check.
    @return Boolean."""
    import re
    titles = ["Chapitre", "Chapter", "Capitol", "Capítol", "Capítulo", "Tratado", "Prologue", "Prològue", "Prólogo", "Note", "Nòta", "Glava", "Poglavlje"]
    for title in titles:
        if text.startswith(title) or text.startswith(title.upper()):
            return True
    # Check if the string starts with a numerotation
    if re.match("^[IVXLCM0-9]+", text.split()[0]):
        return True
    return False

def txt_read(filename, tei=None):
    """! @brief Read a text file.
    @param filename The name of the text file to read with full path, for instance 'user/input.txt'.
    @param tei If given, use this TEI instance; otherwise create one.    
    @return A TEI instance.
    """
    print("Read TEI body from text file " + filename)
    if tei is None:
        tei = TEI()

    ## Read file
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]
    # Remove empty lines
    lines.remove('')

    ## Segment each paragraph into sentences
    current_div = None
    for line in lines:
        if line != '':
            if current_div is None or is_head(line):
                if current_div is not None:
                    # Append previous division to TEI text body
                    tei.text.body.div.append(current_div)
                # Create a new division
                current_div = div()
                # Add division head if any
                if is_head(line):
                    current_div.head.seg = line
                    continue
            # Create a new paragraph
            current_p = p()
            sentences = segment(line)
            for sentence in sentences:
                # Create a new sentence and append it to the current paragraph
                current_p.s.append(s(text=sentence))
            # Append the new paragraph to the current division
            current_div.p.append(current_p)
    # Append current division to TEI text body
    tei.text.body.div.append(current_div)

    return tei

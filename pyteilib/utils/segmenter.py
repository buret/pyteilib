#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package transformer
"""

import nltk

def segment(paragraph):
    """! @brief Segment a paragraph into sentences.
    @param paragraph The string containing the text to segment.
    @return A list of strings containing sentences."""
    sentences = []
    nltk_sentences = []
    if paragraph is not None and len(paragraph) > 0:
        lines = paragraph.replace("...", "...\n").splitlines()
        for line in lines:
            line = line.strip()
            nltk_sentences += nltk.tokenize.sent_tokenize(line, language='french')
    # Handle incorrect segmentation
    index = 0
    for sentence in nltk_sentences:
        if index == 0:
            sentences.append(sentence)
            index += 1
        else:
            # Check if each sentence starts with a capital letter
            if sentence[0].islower():
                # If it starts with a lower case, join with previous sentence
                sentences[index-1] += ' ' + sentence
            elif sentence[0].isupper() and sentence[1] == '.' and len(sentence) == 2:
                # If it starts with an upper case but is an abbreviation, join with previous sentence
                sentences[index-1] += ' ' + sentence
            else:
                sentences.append(sentence)
                index += 1
    return sentences

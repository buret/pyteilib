#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package transformer
"""

from utils.segmenter import segment
from tei_p5 import TEI, catDesc, term, div, p, s
from pcl_v8 import PCLv8
from pcl_v9 import PCLv9

# Map genre from BaTelÒc to ParCoLab
genre_mapping = {
    'roman'  : 'novel',
    'conte literari' : 'tale',
    'memòris e cronicas' : 'memoirs',
    'novèlas' : 'short story',
    'ensag' : 'essay',
    'poesia' : 'poem',
    'teatre' : 'theater',
    'cançon' : 'song',
    'correspondéncia' : 'letter',
    'discors' : 'speech',
    'tractat' : 'convention',
    'conte de tradicion orala' : 'fairy tale',
    'article scientific' : 'scientific paper',
    'article de premsa' : 'newspaper article',
    'tèxte oral' : 'spoken',
    '' : '',
    None : None
}

def count_words(text):
    """! @brief Count words in a text.
    @param text The string containing the text.
    @return Number of words."""
    import re
    return len(re.findall(r'\w+', text))

def create_sub_divisions(body_div_pcl, sub_div_bto):
    """! @brief For each sub-division in BaTelÒc text body, create a division in ParCoLab text body.
    @param body_div_pcl The TEI BaTelÒc instance to transform. The list of TEI ParCoLab text body divisions.
    @param sub_div_bto The list of TEI BaTelÒc text body sub-divisions.
    @return None.
    """
    for divn in sub_div_bto:
        if divn.text is not None or divn.head.text is not None or len(divn.p) > 0 or len(divn.div) > 0:
            sub_div_pcl = div(text=divn.text)
            sub_div_pcl.head.seg = divn.head.text
            for divn_p in divn.p:
                sub_div_pcl_p = p(text=divn_p.text)
                for divn_p_s in divn_p.s:
                    sub_div_pcl_p.s.append(s(text=divn_p_s.text))
                sub_div_pcl.p.append(sub_div_pcl_p)
            body_div_pcl.append(sub_div_pcl)
            create_sub_divisions(body_div_pcl, divn.div)

def transform_bto2pcl(tei_bto, xml_type='TEI'):
    """! @brief Transform a TEI instance type to another.
    @param tei_bto The TEI BaTelÒc instance to transform.
    @param xml_type The type of the TEI instance to transform to: 'PCLv8' or 'PCLv9'.
    @return A TEI ParCoLab instance.
    """
    if tei_bto.get_filename() is not None:
        print("Transform BaTelÒc format from XML file " + tei_bto.get_filename() + " to ParCoLab " + xml_type[-2:] + " format")
    else:
        print("Transform BaTelÒc format to ParCoLab " + xml_type[-2:] + " format")
    if xml_type == 'PCLv8':
        tei_pcl = PCLv8()
    elif xml_type == 'PCLv9':
        tei_pcl = PCLv9()
    tei_pcl.id = tei_bto.id

    #### TEI header

    ### fileDesc

    ## titleStmt
    for item in tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title:
        if item.type == None:
            # Set title
            tei_pcl.teiHeader.fileDesc.titleStmt.title = item.text
        elif item.type == "parallel":
            # Set subtitle
            tei_pcl.teiHeader.fileDesc.titleStmt.subtitle = item.text
    for item in tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author:
        if item.id == "auteurOriginal":
            # Set author
            tei_pcl.teiHeader.fileDesc.titleStmt.author[0].name.forename = item.forename
            tei_pcl.teiHeader.fileDesc.titleStmt.author[0].name.surname = item.surname
            if xml_type == 'PCLv9':
                tei_pcl.teiHeader.fileDesc.titleStmt.author[0].birth = item.datebirth
                tei_pcl.teiHeader.fileDesc.titleStmt.author[0].death = item.datedead
        elif item.id == "traducteur":
            # Set translator
            tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename = item.forename
            tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname = item.surname
            if xml_type == 'PCLv9':
                tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[0].birth = item.datebirth
                tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[0].death = item.datedead
    if xml_type == 'PCLv9':
        for item in tei_bto.teiHeader.fileDesc.titleStmt.respStmt:
            if item.resp.startswith("balhaire"):
                # Set publisher provider
                tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[4].name = item.name
            elif item.resp.startswith("portaire"):
                # Set project provider
                tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[5].name = item.name
            elif item.resp.startswith("donadas"):
                # Set TEI header creator
                tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[6].name = item.name
            elif item.resp.startswith("pretractament"):
                # Set TEI body creator
                tei_pcl.teiHeader.fileDesc.titleStmt.respStmt[7].name = item.name
    # Hard-code collection
    tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.collection = "BaTelÒc"
    # Split principal's name to set responsible's forename and surname
    list_of_names = tei_bto.teiHeader.fileDesc.titleStmt.principal.split()
    if len(list_of_names) == 1:
        tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname = list_of_names[0]
    else:
        tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename = ' '.join(list_of_names[:-1])
        tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname = list_of_names[-1]

    ## editionStmt
    # Compute edition
    series = tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.series
    for item in tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno:
        if item.type == "numero edition":
            idno = item.text
        elif item.type == "ISBN" and xml_type == 'PCLv9':
            # Set ISBN
            tei_pcl.teiHeader.fileDesc.publicationStmt.idno.text = item.text

    # Set edition
    if series is None:
        tei_pcl.teiHeader.fileDesc.editionStmt.edition.text = idno
    elif idno is None:
        tei_pcl.teiHeader.fileDesc.editionStmt.edition.text = series
    else:
        tei_pcl.teiHeader.fileDesc.editionStmt.edition.text = series + idno.text

    ## publicationStmt
    # Set publisher
    tei_pcl.teiHeader.fileDesc.publicationStmt.publisher = tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.publisher
    # Set pubPlace
    tei_pcl.teiHeader.fileDesc.publicationStmt.pubPlace = tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.pubplace
    # Set date
    tei_pcl.teiHeader.fileDesc.publicationStmt.date = tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.date
    # Set availability and licence
    tei_pcl.teiHeader.fileDesc.publicationStmt.availability.licence.text = tei_bto.teiHeader.fileDesc.publicationStmt.availability.status
    tei_pcl.teiHeader.fileDesc.publicationStmt.availability.licence.p = p(tei_bto.teiHeader.fileDesc.publicationStmt.availability.p.text)

    ## Hard-code sourceDesc
    tei_pcl.teiHeader.fileDesc.sourceDesc.text = "Imported from BaTelÒc"

    ### encodingDesc
    tei_pcl.teiHeader.encodingDesc.projectDesc = tei_bto.teiHeader.encodingDesc.projectDesc

    ### profileDesc

    ## langUsage
    # Set language
    tei_pcl.teiHeader.profileDesc.langUsage.language.ident = tei_bto.teiHeader.profileDesc.langUsage.language.ident
    tei_pcl.teiHeader.profileDesc.langUsage.language.langOri = tei_bto.teiHeader.profileDesc.langUsage.language.ident

    ## category
    for item in tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category:
        if item.type == "dialecte":
            if xml_type == 'PCLv8':
                # Clone catDesc
                for cat_desc in item.catDesc:
                    tei_pcl.teiHeader.profileDesc.category.catDesc.append(catDesc(text=cat_desc.text))
            elif xml_type == 'PCLv9':
                # Set language
                tei_pcl.teiHeader.profileDesc.langUsage.language.variant = item.catDesc[0].text
                tei_pcl.teiHeader.profileDesc.langUsage.language.variantOri = item.catDesc[0].text
        elif item.type == "graphie" and xml_type == 'PCLv9':
            # Set language
            tei_pcl.teiHeader.profileDesc.langUsage.language.script = item.catDesc[0].text
            tei_pcl.teiHeader.profileDesc.langUsage.language.scriptOri = item.catDesc[0].text

    ## creation
    # Set date
    tei_pcl.teiHeader.profileDesc.creation.date =  tei_bto.teiHeader.profileDesc.creation.date

    ## textDesc
    # Hard-code derivation
    tei_pcl.teiHeader.profileDesc.textDesc.derivation.type = "original"
    # Hard-code domain
    tei_pcl.teiHeader.profileDesc.textDesc.domain[0].type = "literature"
    # Map genre
    for item in tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category:
        if item.type == "genre":
            for cat_desc in item.catDesc:
                if cat_desc.text in genre_mapping:
                    genre_pcl = genre_mapping[cat_desc.text]
                else:
                    genre_pcl = "other"
                if cat_desc.type == "principal":
                    if genre_pcl is not None and len(genre_pcl) > 0:
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[0].lang = "en"
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[0].type = genre_pcl
                    if cat_desc.text is not None and len(cat_desc.text) > 0:
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[1].lang = "oc"
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[1].type = cat_desc.text
                elif cat_desc.type == "sub":
                    if genre_pcl is not None and len(genre_pcl) > 0:
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[2].lang = "en"
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[2].type = genre_pcl
                    if cat_desc.text is not None and len(cat_desc.text) > 0:
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[3].lang = "oc"
                        tei_pcl.teiHeader.profileDesc.textDesc.genre[3].type = cat_desc.text

        ## textClass
        elif item.type == "corpus" and xml_type == 'PCLv9':
            for cat_desc in item.catDesc:
                tei_pcl.teiHeader.profileDesc.textClass.keywords.term.append(term(cat_desc.text))

    # Hard-code textForm
    tei_pcl.teiHeader.profileDesc.textDesc.textForm.type = "prose"

    ### revisionDesc
    # Hard-coded in PCLv9 constructor

    #### TEI text

    ## Get prologue if any
    if tei_bto.text.front is not None and (tei_bto.text.front.prologue.text is not None or len(tei_bto.text.front.prologue.p) > 0):
        # Create a new text body division
        div_pro = div(text=tei_bto.text.front.prologue.text)
        for prologue_p in tei_bto.text.front.prologue.p:
            div_pro.p.append(p(text=prologue_p.text))
        tei_pcl.text.body.div.append(div_pro)

    ## Clone body divisions and sub-divisions
    for div_bto in tei_bto.text.body.div:
        if (div_bto.text is not None and div_bto.text != '') or div_bto.head.text is not None or len(div_bto.p) > 0 or len(div_bto.div) > 0:
            div_pcl = div(text=div_bto.text)
            div_pcl.head.seg = div_bto.head.text
            for div_bto_p in div_bto.p:
                div_pcl_p = p(text=div_bto_p.text)
                for div_bto_p_s in div_bto_p.s:
                    div_pcl_p.s.append(s(text=div_bto_p_s.text))
                div_pcl.p.append(div_pcl_p)
            tei_pcl.text.body.div.append(div_pcl)
            create_sub_divisions(tei_pcl.text.body.div, div_bto.div)

    ## Get epilogue if any
    if tei_bto.text.back is not None:
        # Clone epilogue divisions and sub-divisions
        for div_epi in tei_bto.text.back.epilogue.div:
            if (div_epi.text is not None and div_epi.text != '') or div_epi.head.text is not None or len(div_epi.p) > 0 or len(div_epi.div) > 0:
                div_pcl = div(text=div_epi.text)
                div_pcl.head.seg = div_epi.head.text
                for div_epi_p in div_epi.p:
                    div_pcl_p = p(text=div_epi_p.text)
                    for div_epi_p_s in div_epi_p.s:
                        div_pcl_p.s.append(s(text=div_epi_p_s.text))
                    div_pcl.p.append(div_pcl_p)
                tei_pcl.text.body.div.append(div_pcl)
                create_sub_divisions(tei_pcl.text.body.div, div_epi.div)

    ## Now, compute TEI header fileDesc extent
    for div_bdy in tei_pcl.text.body.div:
        tei_pcl.text.body.add_text(div_bdy.text, new_line=True)
        tei_pcl.text.body.add_text(div_bdy.head.seg, new_line=True)
        for p_bdy in div_bdy.p:
            tei_pcl.text.body.add_text(p_bdy.text, new_line=True)
            for s_bdy in p_bdy.s:
                tei_pcl.text.body.add_text(s_bdy.text)
        assert len(div_bdy.div) == 0, len(div_bdy.div)
    tei_pcl.teiHeader.fileDesc.extent.measure.quantity = count_words(tei_pcl.text.body.get_text())

    ## Segment paragraphs into sentences
    # For each division
    for div_bdy in tei_pcl.text.body.div:
        # Handle divison text if any
        div_bdy_seg = segment(div_bdy.text)
        if len(div_bdy_seg) > 0:
            # Insert a paragraph at the beginning of the division
            p0 = p()
            for div_bdy_s in div_bdy_seg:
                p0.s.append(s(div_bdy_s))
            div_bdy.p.insert(0, p0)
        div_bdy.text = None
        # For each paragraph, create needed sentences
        for p_bdy in div_bdy.p:
            p_bdy_seg = segment(p_bdy.text)
            index_s = 0
            for p_bdy_s in p_bdy_seg:
                p_bdy.s.insert(index_s, s(p_bdy_s))
                index_s += 1
            p_bdy.text = None
            for s_bdy in p_bdy.s:
                if s_bdy.text is None:
                    p_bdy.s.remove(s_bdy)

    return tei_pcl

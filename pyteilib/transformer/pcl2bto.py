#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package transformer
"""

from tei_p5 import projectDesc, catDesc, div, p
from bto import BTO

# Map genre from ParCoLab to BaTelÒc
genre_mapping = {
    'novel'  : 'roman',
    'tale' : 'conte literari',
    'memoirs' : 'memòris e cronicas',
    'short story' : 'novèlas',
    'essay' : 'ensag',
    'poem' : 'poesia',
    'theater' : 'teatre',
    'song' : 'cançon',
    'letter' : 'correspondéncia',
    'speech' : 'discors',
    'convention' : 'tractat',
    'fairy tale' : 'conte de tradicion orala',
    'scientific paper' : 'article scientific',
    'newspaper article' : 'article de premsa',
    'spoken' : 'tèxte oral',
    '' : '',
    None : None
}

def concatenate_name(name1, name2, separator=' '):
    """! @brief Concatenate name1 and name2.
    @param name1 A string containing a name, might be None.
    @param name2 A string containing a name, might be None.
    @param separator A character to insert between both names, default is space.
    @return A string containing the full name 'name1 name2', might be None.
    """
    name = name1
    if name2 is not None and name2 != '':
        if name is None or name == '':
            name = name2
        else:
            name = name + separator + name2
    return name

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
    if tei_pcl.__class__.__name__ == "teiCorpus":
        tei_pcl = tei_pcl.TEI
    tei_bto.id = tei_pcl.id

    #### TEI header

    ### fileDesc

    ## titleStmt

    # Set title in 2 different places
    tei_bto.teiHeader.fileDesc.titleStmt.title = tei_pcl.teiHeader.fileDesc.titleStmt.title
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].text = tei_pcl.teiHeader.fileDesc.titleStmt.title
    # Set subtitle
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].text = tei_pcl.teiHeader.fileDesc.titleStmt.subtitle
    # Set author in 2 different places
    if len(tei_pcl.teiHeader.fileDesc.titleStmt.author) > 0:
        tei_bto.teiHeader.fileDesc.titleStmt.author = concatenate_name(tei_pcl.teiHeader.fileDesc.titleStmt.author[0].name.surname, tei_pcl.teiHeader.fileDesc.titleStmt.author[0].name.forename)
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].surname = tei_pcl.teiHeader.fileDesc.titleStmt.author[0].name.surname
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].forename = tei_pcl.teiHeader.fileDesc.titleStmt.author[0].name.forename
    if xml_type == 'PCLv9':
        tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datebirth = tei_pcl.teiHeader.fileDesc.titleStmt.author[0].birth
        tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datedead = tei_pcl.teiHeader.fileDesc.titleStmt.author[0].death
    # Leave editor empty
    # Compute principal
    if len(tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt) > 0 and tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name is not None:
        tei_bto.teiHeader.fileDesc.titleStmt.principal = concatenate_name(tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename, tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname)
    # Set 5 respStmt
    set_translator = True
    for item in tei_pcl.teiHeader.fileDesc.titleStmt.respStmt:
        # Set 'balhaire fichièr sorga'
        if item.resp == "publisher_provider":
            tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].name = item.name
        # Set 'portaire fichièr sorga'
        elif item.resp == "project_provider":
            tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].name = item.name
        # Set 'donadas pel header'
        elif item.resp == "teihdr_creator":
            tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].name = item.name
        # Set 'pretractament e balisatge del tèxte segon la TEI P5'
        elif item.resp == "teibdy_creator":
            tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].name = item.name
        # Set first translator
        elif item.resp == "translator" and set_translator:
            tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].surname = item.name.surname
            tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].forename = item.name.forename
            tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datebirth = item.birth
            tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datedead = item.death
            set_translator = False

    ## editionStmt
    if xml_type == 'PCLv9':
        # Set edition date as last change
        if len(tei_pcl.teiHeader.revisionDesc.listChange.change) > 0:
            tei_bto.teiHeader.fileDesc.editionStmt.edition.date = tei_pcl.teiHeader.revisionDesc.listChange.change[0].when

    ## extent
    if tei_pcl.teiHeader.fileDesc.extent is not None:
        tei_bto.teiHeader.fileDesc.extent = tei_pcl.teiHeader.fileDesc.extent.measure.quantity + ' ' + tei_pcl.teiHeader.fileDesc.extent.measure.unit

    ## publicationStmt

    # Compute distributor's name
    if len(tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt) > 1:
        tei_bto.teiHeader.fileDesc.publicationStmt.distributor.name = concatenate_name(tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.surname, tei_pcl.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.forename, separator='-')
    # Set availability
    tei_bto.teiHeader.fileDesc.publicationStmt.availability.status = tei_pcl.teiHeader.fileDesc.publicationStmt.availability.licence.text
    tei_bto.teiHeader.fileDesc.publicationStmt.availability.p = tei_pcl.teiHeader.fileDesc.publicationStmt.availability.licence.p

    ## sourceDesc

    # Hard-code bibliography structure lang
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.lang = "fr"
    # Set bibliography structure monography
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.date = tei_pcl.teiHeader.fileDesc.publicationStmt.date
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.publisher = tei_pcl.teiHeader.fileDesc.publicationStmt.publisher
    # Split edition into series and idno
    if tei_pcl.teiHeader.fileDesc.editionStmt.edition.text is not None:
        edition_list = tei_pcl.teiHeader.fileDesc.editionStmt.edition.text.split()
        if len(edition_list) > 1:
            tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.series = edition_list[0]
            tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].text = edition_list[1]
        elif len(edition_list) == 1:
            try:
                # If this a an integer, set idno
                tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].text = int(edition_list[0])
            except ValueError:
                # If this is a string, set series statement
                tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.seriesStmt = edition_list[0]
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.pubplace = tei_pcl.teiHeader.fileDesc.publicationStmt.pubPlace
    tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].text = tei_pcl.teiHeader.fileDesc.publicationStmt.idno

    ### encodingDesc

    ## projectDesc
    if tei_pcl.teiHeader.encodingDesc.projectDesc is not None:
        tei_bto.teiHeader.encodingDesc.projectDesc = projectDesc()
        for item in tei_pcl.teiHeader.encodingDesc.projectDesc.p:
            tei_bto.teiHeader.encodingDesc.projectDesc.p.append(p(text=item.text))

    ## classDecl
    # Hard-code taxonomy bibliography
    tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.bibl = "Frantext"
    # Set dialect
    if xml_type == 'PCLv8':
        if tei_pcl.teiHeader.profileDesc.category.type == "dialecte" and len(tei_pcl.teiHeader.profileDesc.category.catDesc) > 0:
            tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].catDesc[0].text = tei_pcl.teiHeader.profileDesc.category.catDesc[0].text
    elif xml_type == 'PCLv9':
        tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].catDesc[0].text = tei_pcl.teiHeader.profileDesc.langUsage.language.variant
    if xml_type == 'PCLv9':
        # Set script
        tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].catDesc[0].text = tei_pcl.teiHeader.profileDesc.langUsage.language.script
    # Map genre
    genre_bto = None
    index = 0
    for item in tei_pcl.teiHeader.profileDesc.textDesc.genre:
        if item.lang == "en":
            if item.type in genre_mapping:
                genre_bto = genre_mapping[item.type]
            else:
                genre_bto = "autre"
            if len(tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc) > index :
                tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[index].text = genre_bto
                index += 1
    if xml_type == 'PCLv9':
        # Set corpus
        for item in tei_pcl.teiHeader.profileDesc.textClass.keywords.term:
            tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].catDesc.append(catDesc(text=item.text))

    ### profileDesc

    ## creation
    # Set date
    tei_bto.teiHeader.profileDesc.creation.date = tei_pcl.teiHeader.profileDesc.creation.date

    ## langUsage
    # Set language
    tei_bto.teiHeader.profileDesc.langUsage.language.ident = tei_pcl.teiHeader.profileDesc.langUsage.language.ident
    if tei_pcl.teiHeader.profileDesc.langUsage.language.ident == "oc":
        tei_bto.teiHeader.profileDesc.langUsage.language.text = "Occitan"

    #### TEI text

    ## Clone body divisions and sub-divisions
    for div_pcl in tei_pcl.text.body.div:
        if (div_pcl.text is not None and div_pcl.text != '') or (div_pcl.head.seg is not None and div_pcl.head.seg != '') or len(div_pcl.p) > 0:
            div_bto = div(text=div_pcl.text)
            div_bto.head.text = div_pcl.head.seg
            for p_pcl in div_pcl.p:
                p_bto = p(text=p_pcl.text)
                for s_pcl in p_pcl.s:
                    if s_pcl.text is not None and s_pcl.text != '':
                        if p_bto.text is None or p_bto.text == '':
                            p_bto.text = s_pcl.text
                        else:
                            p_bto.text += ' ' + s_pcl.text
                div_bto.p.append(p_bto)
            tei_bto.text.body.div.append(div_bto)

    return tei_bto

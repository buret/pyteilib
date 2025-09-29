#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package reader
"""

import pandas
from tei.pcl_v8 import PCLv8
from tei.pcl_v9 import PCLv9
from tei.tei_p5 import note, p, term

def csv_read(filename):
    """! @brief Read a CSV file.
    @param filename The name of the CSV file to read with full path, for instance 'user/input/metadata.csv'.
    @return A list of TEI instances.
    """
    print("Read TEI header from CSV file " + filename)
    tei_instances = []
    dataframe = pandas.read_csv(filename, delimiter="\t", encoding="utf-8")
    dataframe = dataframe.fillna('')
    # Get ParCoLab metadata version: v8 or v9
    version = 'v9'
    try:
        dataframe["author-birth1"]
    except KeyError:
        version = 'v8'
    for index, row in dataframe.iterrows():
        tei = None
        if version == 'v8':
            tei = PCLv8(id=int(row["id"]))
        else: # v9
            tei = PCLv9(id=int(row["id"]))
        tei.set_filename(row["file"])
        # Fill in TEI header from CSV columns
        tei.teiHeader.fileDesc.titleStmt.title = row["title"]
        tei.teiHeader.fileDesc.titleStmt.subtitle = row["subtitle"]
        tei.teiHeader.fileDesc.titleStmt.author[0].name.forename = row["author-firstname1"]
        tei.teiHeader.fileDesc.titleStmt.author[0].name.surname = row["author-lastname1"]
        tei.teiHeader.fileDesc.titleStmt.author[1].name.forename = row["author-firstname2"]
        tei.teiHeader.fileDesc.titleStmt.author[1].name.surname = row["author-lastname2"]
        tei.teiHeader.fileDesc.titleStmt.author[2].name.forename = row["author-firstname3"]
        tei.teiHeader.fileDesc.titleStmt.author[2].name.surname = row["author-lastname3"]
        if version == 'v9':
            tei.teiHeader.fileDesc.titleStmt.author[0].birth = str(row["author-birth1"])
            tei.teiHeader.fileDesc.titleStmt.author[0].death = str(row["author-death1"])
            tei.teiHeader.fileDesc.titleStmt.author[0].placeName = row["author-place1"]
            tei.teiHeader.fileDesc.titleStmt.author[1].birth = str(row["author-birth2"])
            tei.teiHeader.fileDesc.titleStmt.author[1].death = str(row["author-death2"])
            tei.teiHeader.fileDesc.titleStmt.author[1].placeName = row["author-place2"]
            tei.teiHeader.fileDesc.titleStmt.author[2].birth = str(row["author-birth3"])
            tei.teiHeader.fileDesc.titleStmt.author[2].death = str(row["author-death3"])
            tei.teiHeader.fileDesc.titleStmt.author[2].placeName = row["author-place3"]
        tei.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename = row["translator-firstname1"]
        tei.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname = row["translator-lastname1"]
        tei.teiHeader.fileDesc.titleStmt.respStmt[1].name.forename = row["translator-firstname2"]
        tei.teiHeader.fileDesc.titleStmt.respStmt[1].name.surname = row["translator-lastname2"]
        tei.teiHeader.fileDesc.titleStmt.respStmt[2].name.forename = row["translator-firstname3"]
        tei.teiHeader.fileDesc.titleStmt.respStmt[2].name.surname = row["translator-lastname3"]
        if version == 'v9':
            tei.teiHeader.fileDesc.titleStmt.respStmt[0].birth = str(row["translator-birth1"])
            tei.teiHeader.fileDesc.titleStmt.respStmt[0].death = str(row["translator-death1"])
            tei.teiHeader.fileDesc.titleStmt.respStmt[1].birth = str(row["translator-birth2"])
            tei.teiHeader.fileDesc.titleStmt.respStmt[1].death = str(row["translator-death2"])
            tei.teiHeader.fileDesc.titleStmt.respStmt[2].birth = str(row["translator-birth3"])
            tei.teiHeader.fileDesc.titleStmt.respStmt[2].death = str(row["translator-death3"])
        tei.teiHeader.fileDesc.titleStmt.respStmt[3].name.forename = row["transcriber-firstname1"]
        tei.teiHeader.fileDesc.titleStmt.respStmt[3].name.surname = row["transcriber-lastname1"]
        if version == 'v9':
            tei.teiHeader.fileDesc.titleStmt.respStmt[4].name = row["publisher_provider-name"]
            tei.teiHeader.fileDesc.titleStmt.respStmt[4].date = str(row["publisher_provider-date"])
            tei.teiHeader.fileDesc.titleStmt.respStmt[5].name = row["project_provider-name"]
            tei.teiHeader.fileDesc.titleStmt.respStmt[6].name = row["teihdr_creator-name"]
            tei.teiHeader.fileDesc.titleStmt.respStmt[6].date = str(row["teihdr_creator-date"])
            tei.teiHeader.fileDesc.titleStmt.respStmt[7].name = row["teibdy_creator-name"]
            tei.teiHeader.fileDesc.titleStmt.respStmt[7].date = str(row["teibdy_creator-date"])
        tei.teiHeader.fileDesc.titleStmt.collectionStmt.collection = row["collection"]
        tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename = row["resp_collection-firstname1"]
        tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname = row["resp_collection-lastname1"]
        tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.forename = row["resp_collection-firstname2"]
        tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.surname = row["resp_collection-lastname2"]
        tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.forename = row["resp_collection-firstname3"]
        tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.surname = row["resp_collection-lastname3"]
        tei.teiHeader.fileDesc.extent.measure.quantity = int(row["words"])
        tei.teiHeader.fileDesc.publicationStmt.publisher = row["publisher"]
        tei.teiHeader.fileDesc.publicationStmt.pubPlace = row["pubPlace"]
        tei.teiHeader.fileDesc.publicationStmt.date = str(row["date"])
        if version == 'v9':
            tei.teiHeader.fileDesc.publicationStmt.idno.text = row["isbn"]
        tei.teiHeader.fileDesc.publicationStmt.availability.licence.text = row["licence"]
        tei.teiHeader.fileDesc.notesStmt.note.append(note(text=row["note"]))
        tei.teiHeader.fileDesc.editionStmt.edition.text = row["edition"]
        tei.teiHeader.fileDesc.sourceDesc.text = row["sourceDesc"]
        tei.teiHeader.encodingDesc.projectDesc.p.append(p(text=row["projectDesc"]))
        tei.teiHeader.profileDesc.langUsage.language.ident = row["language"]
        tei.teiHeader.profileDesc.langUsage.language.langOri = row["language_ori"]
        if version == 'v8':
            tei.teiHeader.profileDesc.category.catDesc = row["dialect"]
        else: # v9
            tei.teiHeader.profileDesc.langUsage.language.variant = row["dialect"]
            tei.teiHeader.profileDesc.langUsage.language.variantOri = row["dialect_ori"]
            tei.teiHeader.profileDesc.langUsage.language.script = row["script"]
            tei.teiHeader.profileDesc.langUsage.language.scriptOri = row["script_ori"]
        tei.teiHeader.profileDesc.creation.date = str(row["creationDate"])
        tei.teiHeader.profileDesc.textDesc.derivation.type = row["derivation"]
        tei.teiHeader.profileDesc.textDesc.domain[0].type = row["domain1"]
        tei.teiHeader.profileDesc.textDesc.domain[1].type = row["domain2"]
        tei.teiHeader.profileDesc.textDesc.domain[2].type = row["domain3"]
        tei.teiHeader.profileDesc.textDesc.genre[0].type = row["genre1"]
        tei.teiHeader.profileDesc.textDesc.genre[1].type = row["genre2"]
        tei.teiHeader.profileDesc.textDesc.genre[2].type = row["genre3"]
        tei.teiHeader.profileDesc.textDesc.textForm.type = row["textForm"]
        if version == 'v9':
            for corpus in row["predefined_corpora"].split(';'):
                tei.teiHeader.profileDesc.textClass.keywords.term.append(term(corpus.rstrip().lstrip()))
            tei.teiHeader.revisionDesc.listChange.change[0].when = str(row["contributor-date1"])
            tei.teiHeader.revisionDesc.listChange.change[0].who = row["contributor-name1"]
        tei_instances.append(tei)
    return tei_instances

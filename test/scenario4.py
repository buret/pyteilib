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

#### Scenario 4 : Read ParCoLab v9 XML and transform it to BaTelÒc XML

## Read ParCoLab v9 XML
tei_pclv9 = pyteilib.tei_read(INPUT_DIR + "example4_pcl_v9.xml", xml_type='PCLv9')
assert tei_pclv9.get_filename() == INPUT_DIR + "example4_pcl_v9.xml", tei_corpusv8.get_filename()
assert tei_pclv9.__class__.__name__ == "PCLv9", tei_pclv9.__class__.__name__
assert tei_pclv9.id == "12345", tei_pclv9.id

# Test teiHeader
assert tei_pclv9.teiHeader.fileDesc.titleStmt.title == "Title", tei_pclv9.teiHeader.fileDesc.titleStmt.title
assert tei_pclv9.teiHeader.fileDesc.titleStmt.subtitle == "Subtitle", tei_pclv9.teiHeader.fileDesc.titleStmt.subtitle
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.forename == "Firstname1", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.surname == "Lastname1", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].birth == "1901", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].death == "2001", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].placeName == "Paris", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].placeName
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].name.forename == "Firstname2", tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].name.surname == "Lastname2", tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].birth == "1902", tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].death == "2002", tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].placeName == "Toulouse", tei_pclv9.teiHeader.fileDesc.titleStmt.author[1].placeName
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].name.forename == "Firstname3", tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].name.surname == "Lastname3", tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].birth == "1903", tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].death == "2003", tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].placeName == "Bordeaux", tei_pclv9.teiHeader.fileDesc.titleStmt.author[2].placeName
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].resp == "translator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename == "Prénom1", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname == "Nom1", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].birth == "1951", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].death == "-", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].resp == "translator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].name.forename == "Prénom2", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].name.surname == "Nom2", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].birth == "1952", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].death == "-", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].resp == "translator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].name.forename == "Prénom3", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].name.surname == "Nom3", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].birth == "1953", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].death == "-", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].resp == "transcriber", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].name.forename == "Firstname", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].name.surname == "Lastname", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].resp == "publisher_provider", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].name.text == "Monsieur X", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].name.text
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].date == "01/10/01", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].resp == "project_provider", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].name.text == "Myriam Bras", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].name.text
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].resp == "teihdr_creator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].name.text == "Céline Buret", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].name.text
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].date == "01/05/25", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].resp == "teibdy_creator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].name.text == "Céline Buret", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].name.text
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].date == "02/05/25", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.collection == "DIVITAL", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.collection
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp == None, tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name == None, tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name
assert tei_pclv9.teiHeader.fileDesc.editionStmt.edition.text == "Edition", tei_pclv9.teiHeader.fileDesc.editionStmt.edition.text
assert tei_pclv9.teiHeader.fileDesc.extent.measure.unit == "words", tei_pclv9.teiHeader.fileDesc.extent.measure.unit
assert tei_pclv9.teiHeader.fileDesc.extent.measure.quantity == "54321", tei_pclv9.teiHeader.fileDesc.extent.measure.quantity
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.publisher == "Publisher", tei_pclv9.teiHeader.fileDesc.publicationStmt.publisher
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.pubPlace == "Place", tei_pclv9.teiHeader.fileDesc.publicationStmt.pubPlace
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.date == "2001", tei_pclv9.teiHeader.fileDesc.publicationStmt.date
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.type == "ISBN", tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.type
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.text == "978-1-906964-22-1", tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.text
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.text == "Unknown", tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.text
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.p == None, tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.p
assert tei_pclv9.teiHeader.fileDesc.notesStmt.note[0].text == "No remarks", tei_pclv9.teiHeader.fileDesc.notesStmt.note[0].text
assert tei_pclv9.teiHeader.fileDesc.sourceDesc.p.text == "Provided by the editor", tei_pclv9.teiHeader.fileDesc.sourceDesc.p.text
assert tei_pclv9.teiHeader.encodingDesc.projectDesc.p[0].text == "DIVITAL", tei_pclv9.teiHeader.encodingDesc.projectDesc.p[0].text
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.ident == "en", tei_pclv9.teiHeader.profileDesc.langUsage.language.ident
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.langOri == "oc", tei_pclv9.teiHeader.profileDesc.langUsage.language.langOri
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.variant == "dialect", tei_pclv9.teiHeader.profileDesc.langUsage.language.variant
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.script == "latine", tei_pclv9.teiHeader.profileDesc.langUsage.language.script
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.variantOri == "gascon", tei_pclv9.teiHeader.profileDesc.langUsage.language.variantOri
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.scriptOri == "classique", tei_pclv9.teiHeader.profileDesc.langUsage.language.scriptOri
assert tei_pclv9.teiHeader.profileDesc.creation.date == "2000", tei_pclv9.teiHeader.profileDesc.creation.date
assert tei_pclv9.teiHeader.profileDesc.textDesc.derivation.type == "translation", tei_pclv9.teiHeader.profileDesc.derivation.type
assert tei_pclv9.teiHeader.profileDesc.textDesc.domain[0].type == "literature", tei_pclv9.teiHeader.profileDesc.textDesc.domain[0].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.domain[1].type == "linguistics", tei_pclv9.teiHeader.profileDesc.textDesc.domain[1].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.domain[2].type == "music", tei_pclv9.teiHeader.profileDesc.textDesc.domain[2].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].lang == "en", tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].lang
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].type == "novel", tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].lang == "en", tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].lang
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].type == "nursery rhyme", tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[2].lang == "en", tei_pclv9.teiHeader.profileDesc.textDesc.genre[2].lang
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[2].type == "fairy tale", tei_pclv9.teiHeader.profileDesc.textDesc.genre[2].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.textForm.type == "prose", tei_pclv9.teiHeader.profileDesc.textDesc.textForm.type
assert tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[0].text == "descobèrta", tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[0].text
assert tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[1].text == "roergue", tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[1].text
#assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].who == "Céline Buret", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].who
#assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].when == "13/05/25", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].when
assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].text == "File creation", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].text

# Test text body

## Simply export it to ParCoLab v9 XML
pyteilib.tei_write(tei_pclv9, OUTPUT_DIR + "example4_pcl_v9.xml", xml_type='PCLv9')
assert tei_pclv9.get_filename() == OUTPUT_DIR + "example4_pcl_v9.xml", tei_pclv9.get_filename()

## Export metadata to v9 format
pyteilib.export_header(tei_pclv9, OUTPUT_DIR + "example4_metadata_v9.csv")

## Transform it to BaTelÒc XML
tei_bto = pyteilib.transform(tei_pclv9, from_type='PCLv9', to_type='BTO')
assert tei_bto.__class__.__name__ == "BTO", tei_bto.__class__.__name__
assert tei_bto.id == "12345", tei_bto.id

# Test teiHeader

# Test text body

## Simply export it to BaTelÒc XML
pyteilib.tei_write(tei_bto, OUTPUT_DIR + "example4_bto.xml", xml_type='BTO')
assert tei_bto.get_filename() == OUTPUT_DIR + "example4_bto.xml", tei_bto.get_filename()

## Release created objects
del tei_pclv9, tei_bto

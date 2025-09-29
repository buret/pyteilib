#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import TEI library properly
# Also automatically define 'ftest_path' as location of pyteilib/examples/ folder
from startup import *
import os
from datetime import datetime

INPUT_DIR = ftest_path + "input/"
OUTPUT_DIR = ftest_path + "output/"
# Create result folder
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

#### Scenario 6 : Read metadata and text, then transform them to ParCoLab v8/v9 XML

## Read CSV file containing PCLv9 metadata
tei_pclv9 = pyteilib.csv_read(INPUT_DIR + "example6_metadata_v9.csv")[0]
assert tei_pclv9.__class__.__name__ == "PCLv9", tei.__class__.__name__
assert tei_pclv9.get_filename() == "example6_pcl_v9.xml", tei.get_filename()
assert tei_pclv9.id == 12345, tei_pclv9.id

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
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].name == "Monsieur X", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].date == "01/10/01", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].resp == "project_provider", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].name == "Myriam Bras", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].resp == "teihdr_creator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].name == "Céline Buret", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].date == "01/05/25", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].resp == "teibdy_creator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].name == "Céline Buret", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].date == "02/05/25", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.collection == "DIVITAL", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.collection
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp == "resp_collection", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename == "RespFirstname1", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname == "RespLastname1", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp == "resp_collection", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.forename == "RespFirstname2", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.surname == "RespLastname2", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].resp == "resp_collection", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.forename == "RespFirstname3", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.surname == "RespLastname3", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.surname
assert tei_pclv9.teiHeader.fileDesc.extent.measure.unit == "words", tei_pclv9.teiHeader.fileDesc.extent.measure.unit
assert tei_pclv9.teiHeader.fileDesc.extent.measure.quantity == 54321, tei_pclv9.teiHeader.fileDesc.extent.measure.quantity
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.publisher == "Publisher", tei_pclv9.teiHeader.fileDesc.publicationStmt.publisher
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.pubPlace == "Place", tei_pclv9.teiHeader.fileDesc.publicationStmt.pubPlace
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.date == "2001", tei_pclv9.teiHeader.fileDesc.publicationStmt.date
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.type == "ISBN", tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.type
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.text == "978-1-906964-22-1", tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.text
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.text == "Unknown", tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.text
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.p == None, tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.p.text
assert tei_pclv9.teiHeader.fileDesc.notesStmt.note[0].text == "No remarks", tei_pclv9.teiHeader.fileDesc.notesStmt.note[0].text
assert tei_pclv9.teiHeader.fileDesc.editionStmt.edition.text == "Edition", tei_pclv9.teiHeader.fileDesc.editionStmt.edition.text
assert tei_pclv9.teiHeader.fileDesc.sourceDesc.text == "Provided by the editor", tei_pclv9.teiHeader.fileDesc.sourceDesc.text
assert tei_pclv9.teiHeader.encodingDesc.projectDesc.p[0].text == "DIVITAL", tei_pclv9.teiHeader.encodingDesc.projectDesc.p[0].text
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.ident == "en", tei_pclv9.teiHeader.profileDesc.langUsage.language.ident
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.langOri == "oc", tei_pclv9.teiHeader.profileDesc.langUsage.language.langOri
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.variant == "dialect", tei_pclv9.teiHeader.profileDesc.langUsage.language.variant
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.variantOri == "gascon", tei_pclv9.teiHeader.profileDesc.langUsage.language.variantOri
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.script == "latine", tei_pclv9.teiHeader.profileDesc.langUsage.language.script
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
assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].when == "13/05/25", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].when
assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].who == "Céline Buret", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].who
assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].text == "File creation", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].text

## Read text
tei = pyteilib.txt_read(INPUT_DIR + "example6.txt", tei_pclv9)
assert tei.__class__.__name__ == "PCLv9", tei.__class__.__name__
assert tei.get_filename() == "example6_pcl_v9.xml", tei.get_filename()
assert tei.id == 12345, tei.id

# Test text body
assert tei.text.body.div[0].__class__.__name__ == "div", tei.text.body.div[0].__class__.__name__
assert tei.text.body.div[0].text == None, tei.text.body.div[0].text
assert tei.text.body.div[0].head.seg == "Chapitre premier", tei.text.body.div[0].head.seg
assert tei.text.body.div[0].p[0].text == None, tei.text.body.div[0].p[0].text
assert tei.text.body.div[0].p[0].s[0].text == "This is a short story.", tei.text.body.div[0].p[0].s[0].text
assert tei.text.body.div[0].p[0].s[1].text == "With several chapters.", tei.text.body.div[0].p[0].s[1].text
assert tei.text.body.div[0].p[0].s[2].text == "And several languages.", tei.text.body.div[0].p[0].s[2].text
assert tei.text.body.div[0].p[1].text == None, tei.text.body.div[0].p[1].text
assert tei.text.body.div[0].p[1].s[0].text == "And several paragraphs.", tei.text.body.div[0].p[1].s[0].text
assert tei.text.body.div[1].__class__.__name__ == "div", tei.text.body.div[1].__class__.__name__
assert tei.text.body.div[1].text == None, tei.text.body.div[1].text
assert tei.text.body.div[1].head.seg == "Chapter 2", tei.text.body.div[1].head.seg
assert tei.text.body.div[1].p[0].text == None, tei.text.body.div[1].p[0].text
assert tei.text.body.div[1].p[0].s[0].text == "Dans ce chapitre, nous aborderons la question des interrogations ?", tei.text.body.div[1].p[0].s[0].text
assert tei.text.body.div[1].p[0].s[1].text == "Des exclamations !", tei.text.body.div[1].p[0].s[1].text
assert tei.text.body.div[1].p[0].s[2].text == "Des dialogues, etc.", tei.text.body.div[1].p[0].s[2].text
assert tei.text.body.div[1].p[1].text == None, tei.text.body.div[1].p[1].text
assert tei.text.body.div[1].p[1].s[0].text == "- Depuis combien de temps travailles-tu ?", tei.text.body.div[1].p[1].s[0].text
assert tei.text.body.div[1].p[1].s[1].text == "Je ne sais pas.", tei.text.body.div[1].p[1].s[1].text
assert tei.text.body.div[1].p[2].s[0].text == "- Trabalhi sus de tèxtes en occitan.", tei.text.body.div[1].p[2].s[0].text
assert tei.text.body.div[1].p[2].s[1].text == "E tu?", tei.text.body.div[1].p[2].s[1].text
assert tei.text.body.div[2].__class__.__name__ == "div", tei.text.body.div[2].__class__.__name__
assert tei.text.body.div[2].text == None, tei.text.body.div[2].text
assert tei.text.body.div[2].head.seg == "III", tei.text.body.div[2].head.seg
assert tei.text.body.div[2].p[0].text == None, tei.text.body.div[2].p[0].text
assert tei.text.body.div[2].p[0].s[0].text == "Òc, i a encara un fum de causas a far!", tei.text.body.div[2].p[0].s[0].text

## Simply export to metadata v9 format and ParCoLab v9 XML
pyteilib.export_header(tei, OUTPUT_DIR + "example6_metadata_v9.csv")
pyteilib.tei_write(tei, OUTPUT_DIR + tei.get_filename(), xml_type='PCLv9')
assert tei.get_filename() == OUTPUT_DIR + "example6_pcl_v9.xml", tei.get_filename()

## Release created objects
del tei_pclv9, tei

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

#### Scenario 2 : Read ParCoLab v8 XML and transform it to BaTelÒc XML

## Read ParCoLab v8 XML
tei_corpusv8 = pyteilib.tei_read(INPUT_DIR + "example2_pcl_v8.xml", xml_type='PCLv8')
assert tei_corpusv8.get_filename() == INPUT_DIR + "example2_pcl_v8.xml", tei_corpusv8.get_filename()
tei_pclv8 = tei_corpusv8.TEI
assert tei_pclv8.__class__.__name__ == "PCLv8", tei_pclv8.__class__.__name__
assert tei_pclv8.id == "test_2", tei_pclv8.id

# Test teiHeader
assert tei_pclv8.teiHeader.fileDesc.titleStmt.title == "Title", tei_pclv8.teiHeader.fileDesc.titleStmt.title
assert tei_pclv8.teiHeader.fileDesc.titleStmt.subtitle == "Subtitle", tei_pclv8.teiHeader.fileDesc.titleStmt.subtitle
assert tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.forename == "Firstname", tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.surname == "Lastname", tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.author[1].name.forename == "Firstname2", tei_pclv8.teiHeader.fileDesc.titleStmt.author[1].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.author[1].name.surname == "Lastname2", tei_pclv8.teiHeader.fileDesc.titleStmt.author[1].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].resp == "translator", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename == "Firstname", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname == "Lastname", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].resp == "translator", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].name.forename == "Firstname2", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].name.surname == "Lastname2", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[2].resp == "transcriber", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[2].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.collection == "BaTelÒc", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.collection
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp == "resp_collection", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename == "Firstname", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname == "Lastname", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp == "resp_collection", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.forename == "LL-OCRE", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.surname == "CLLE", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.surname
assert tei_pclv8.teiHeader.fileDesc.editionStmt.edition.text == "Series 123", tei_pclv8.teiHeader.fileDesc.editionStmt.edition.text
assert tei_pclv8.teiHeader.fileDesc.extent.measure.unit == "words", tei_pclv8.teiHeader.fileDesc.extent.measure.unit
assert tei_pclv8.teiHeader.fileDesc.extent.measure.quantity == "114", tei_pclv8.teiHeader.fileDesc.extent.measure.quantity
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.publisher == "Publisher", tei_pclv8.teiHeader.fileDesc.publicationStmt.publisher
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.pubPlace == "Place", tei_pclv8.teiHeader.fileDesc.publicationStmt.pubPlace
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.date == "Date", tei_pclv8.teiHeader.fileDesc.publicationStmt.date
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.text == "restricted", tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.text
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.p.text == "à utiliser dans un cadre de recherche ou d'enseignement après accord du dépositaire des droits", tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.p.text
assert tei_pclv8.teiHeader.fileDesc.sourceDesc.p.text == "Imported from BaTelÒc", tei_pclv8.teiHeader.fileDesc.sourceDesc.p.text
assert tei_pclv8.teiHeader.encodingDesc.projectDesc.p[0].text == "BaTelÒc : Basa de Tèxtes en Lenga Occitana", tei_pclv8.teiHeader.encodingDesc.projectDesc.p[0].text
assert tei_pclv8.teiHeader.encodingDesc.projectDesc.p[1].text == "Encodatge de tèxtes occitans segon la nòrma de la Text Encoding Initiative, TEIP5", tei_pclv8.teiHeader.encodingDesc.projectDesc.p[1].text
assert tei_pclv8.teiHeader.encodingDesc.projectDesc.p[2].text == "http://www.tei-c.org/release/doc/tei-p5-doc", tei_pclv8.teiHeader.encodingDesc.projectDesc.p[2].text
assert tei_pclv8.teiHeader.profileDesc.langUsage.language.ident == "oc", tei_pclv8.teiHeader.profileDesc.langUsage.language.ident
assert tei_pclv8.teiHeader.profileDesc.langUsage.language.langOri == "oc", tei_pclv8.teiHeader.profileDesc.langUsage.language.langOri
assert tei_pclv8.teiHeader.profileDesc.category.type == "dialecte", tei_pclv8.teiHeader.profileDesc.category.type
assert tei_pclv8.teiHeader.profileDesc.category.catDesc[0].text == "Lengadocian", tei_pclv8.teiHeader.profileDesc.category.catDesc[0].text
assert tei_pclv8.teiHeader.profileDesc.creation.date == "2003", tei_pclv8.teiHeader.profileDesc.creation.date
assert tei_pclv8.teiHeader.profileDesc.textDesc.derivation.type == "original", tei_pclv8.teiHeader.profileDesc.derivation.type
assert tei_pclv8.teiHeader.profileDesc.textDesc.domain[0].type == "literature", tei_pclv8.teiHeader.profileDesc.textDesc.domain[0].type
assert tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].lang == "en", tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].lang
assert tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].type == "essay", tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].type
assert tei_pclv8.teiHeader.profileDesc.textDesc.textForm.type == "prose", tei_pclv8.teiHeader.profileDesc.textDesc.textForm.type

# Test text body
assert tei_pclv8.text.body.div[0].__class__.__name__ == "div", tei_pclv8.text.body.div[0].__class__.__name__
assert tei_pclv8.text.body.div[0].text == '', tei_pclv8.text.body.div[0].text
assert tei_pclv8.text.body.div[0].head.seg == None, tei_pclv8.text.body.div[0].head.seg
assert tei_pclv8.text.body.div[0].p[0].text == '', tei_pclv8.text.body.div[0].p[0].text
assert tei_pclv8.text.body.div[0].p[0].s[0].text == "This is a quote.", tei_pclv8.text.body.div[0].p[0].s[0].text
assert tei_pclv8.text.body.div[0].p[1].text == '', tei_pclv8.text.body.div[0].p[1].text
assert tei_pclv8.text.body.div[0].p[1].s[0].text == "Firstname LASTNAME.", tei_pclv8.text.body.div[0].p[1].s[0].text
assert tei_pclv8.text.body.div[1].__class__.__name__ == "div", tei_pclv8.text.body.div[1].__class__.__name__
assert tei_pclv8.text.body.div[1].text == '', tei_pclv8.text.body.div[1].text
assert tei_pclv8.text.body.div[1].head.seg == None, tei_pclv8.text.body.div[1].head.seg
assert tei_pclv8.text.body.div[1].p[0].text == '', tei_pclv8.text.body.div[1].p[0].text
assert tei_pclv8.text.body.div[1].p[0].s[0].text == "Aquò es un exemple.", tei_pclv8.text.body.div[1].p[0].s[0].text
assert tei_pclv8.text.body.div[1].p[1].text == '', tei_pclv8.text.body.div[1].p[1].text
assert tei_pclv8.text.body.div[1].p[1].s[0].text == "Amb qualquas frasas.", tei_pclv8.text.body.div[1].p[1].s[0].text
assert tei_pclv8.text.body.div[1].p[2].text == '', tei_pclv8.text.body.div[1].p[2].text
assert tei_pclv8.text.body.div[1].p[2].s[0].text == "E de partidas en italicas.", tei_pclv8.text.body.div[1].p[2].s[0].text
assert tei_pclv8.text.body.div[1].p[2].s[1].text == "De questions?", tei_pclv8.text.body.div[1].p[2].s[1].text
assert tei_pclv8.text.body.div[1].p[2].s[2].text == "O encara: d'exclamacions!", tei_pclv8.text.body.div[1].p[2].s[2].text
assert tei_pclv8.text.body.div[1].p[2].s[3].text == "Plan.", tei_pclv8.text.body.div[1].p[2].s[3].text
assert tei_pclv8.text.body.div[1].p[3].text == '', tei_pclv8.text.body.div[1].p[3].text
assert tei_pclv8.text.body.div[1].p[3].s[0].text == "De verguetas : \"100% des tests doivent passer\".", tei_pclv8.text.body.div[1].p[3].s[0].text
assert tei_pclv8.text.body.div[1].p[3].s[1].text == "Totjorn.", tei_pclv8.text.body.div[1].p[3].s[1].text
assert tei_pclv8.text.body.div[1].p[3].s[2].text == "\"Alara ?\"", tei_pclv8.text.body.div[1].p[3].s[2].text
assert tei_pclv8.text.body.div[1].p[4].text == '', tei_pclv8.text.body.div[1].p[4].text
assert tei_pclv8.text.body.div[1].p[4].s[0].text == "Ça, c'est une phrase qui commence par un caractère spécial.", tei_pclv8.text.body.div[1].p[4].s[0].text
assert tei_pclv8.text.body.div[1].p[4].s[1].text == "Ô oui!", tei_pclv8.text.body.div[1].p[4].s[1].text
assert tei_pclv8.text.body.div[1].p[4].s[2].text == "Ò aquesta tanben.", tei_pclv8.text.body.div[1].p[4].s[2].text
assert tei_pclv8.text.body.div[2].__class__.__name__ == "div", tei_pclv8.text.body.div[2].__class__.__name__
assert tei_pclv8.text.body.div[2].text == '', tei_pclv8.text.body.div[2].text
assert tei_pclv8.text.body.div[2].head.seg == "Titre du chapitre", tei_pclv8.text.body.div[2].head.seg
assert tei_pclv8.text.body.div[2].p[0].text == '', tei_pclv8.text.body.div[2].p[0].text
assert tei_pclv8.text.body.div[2].p[0].s[0].text == "Maintenant testons les abbréviations comme F.T.P ou F.F.I. par exemple.", tei_pclv8.text.body.div[2].p[0].s[0].text
assert tei_pclv8.text.body.div[2].p[0].s[1].text == "Ou St. (St ?) Mr. et Ste Mme.", tei_pclv8.text.body.div[2].p[0].s[1].text
assert tei_pclv8.text.body.div[2].p[1].text == '', tei_pclv8.text.body.div[2].p[1].text
assert tei_pclv8.text.body.div[2].p[1].s[0].text == "Ainsi que les différentes ponctuations,  comme ; et encore : ainsi de suite...", tei_pclv8.text.body.div[2].p[1].s[0].text
assert tei_pclv8.text.body.div[2].p[1].s[1].text == "Voilà.", tei_pclv8.text.body.div[2].p[1].s[1].text
assert tei_pclv8.text.body.div[2].p[2].text == '', tei_pclv8.text.body.div[2].p[2].text
assert tei_pclv8.text.body.div[2].p[2].s[0].text == "Nous devons aussi tester les dialogues.", tei_pclv8.text.body.div[2].p[2].s[0].text
assert tei_pclv8.text.body.div[2].p[2].s[1].text == "Quelqu'un dit : - Que fait-on ?", tei_pclv8.text.body.div[2].p[2].s[1].text
assert tei_pclv8.text.body.div[2].p[2].s[2].text == "Doit-on continuer ?", tei_pclv8.text.body.div[2].p[2].s[2].text
assert tei_pclv8.text.body.div[2].p[3].text == '', tei_pclv8.text.body.div[2].p[3].text
assert tei_pclv8.text.body.div[2].p[3].s[0].text == "- Je ne sais pas...", tei_pclv8.text.body.div[2].p[3].s[0].text
assert tei_pclv8.text.body.div[2].p[3].s[1].text == "Qu'en penses-tu ?", tei_pclv8.text.body.div[2].p[3].s[1].text
assert tei_pclv8.text.body.div[3].__class__.__name__ == "div", tei_pclv8.text.body.div[3].__class__.__name__
assert tei_pclv8.text.body.div[3].text == '', tei_pclv8.text.body.div[3].text
assert tei_pclv8.text.body.div[3].head.seg == None, tei_pclv8.text.body.div[3].head.seg
assert tei_pclv8.text.body.div[3].p[0].text == '', tei_pclv8.text.body.div[3].p[0].text
assert tei_pclv8.text.body.div[3].p[0].s[0].text == "C'est la fin.", tei_pclv8.text.body.div[3].p[0].s[0].text
assert tei_pclv8.text.body.div[3].p[0].s[1].text == "On termine avec une signature.", tei_pclv8.text.body.div[3].p[0].s[1].text

## Simply export it to ParCoLab v8 XML
pyteilib.tei_write(tei_pclv8, OUTPUT_DIR + "example2_pcl_v8.xml", xml_type='PCLv8')
assert tei_pclv8.get_filename() == OUTPUT_DIR + "example2_pcl_v8.xml", tei_pclv8.get_filename()

## Export metadata to v8 format
pyteilib.export_header(tei_pclv8, OUTPUT_DIR + "example2_metadata_v8.csv")

## Transform it to BaTelÒc XML
tei_bto = pyteilib.transform(tei_pclv8, from_type='PCLv8', to_type='BTO')
assert tei_bto.__class__.__name__ == "BTO", tei_bto.__class__.__name__
assert tei_bto.id == "test_2", tei_bto.id

# Test teiHeader
assert tei_bto.teiHeader.fileDesc.titleStmt.title == "Title", tei_bto.teiHeader.fileDesc.titleStmt.title
assert tei_bto.teiHeader.fileDesc.titleStmt.author == "Lastname Firstname", tei_bto.teiHeader.fileDesc.titleStmt.author
assert tei_bto.teiHeader.fileDesc.titleStmt.editor == None, tei_bto.teiHeader.fileDesc.titleStmt.editor
assert tei_bto.teiHeader.fileDesc.titleStmt.principal == "Firstname Lastname", tei_bto.teiHeader.fileDesc.titleStmt.principal
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].resp == "balhaire fichièr sorga", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].name == None, tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].name
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].resp == "portaire fichièr sorga", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].name == None, tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].name
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].resp == "donadas pel header", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].name == None, tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].name
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].resp == "pretractament e balisatge del tèxte segon la TEI P5", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].name == None, tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].name
assert tei_bto.teiHeader.fileDesc.editionStmt.edition.date == None, tei_bto.teiHeader.fileDesc.editionStmt.edition.date
assert tei_bto.teiHeader.fileDesc.extent == "114 words", tei_bto.teiHeader.fileDesc.extent
assert tei_bto.teiHeader.fileDesc.publicationStmt.distributor.name == "CLLE-LL-OCRE", tei_bto.teiHeader.fileDesc.publicationStmt.distributor.name
assert tei_bto.teiHeader.fileDesc.publicationStmt.distributor.address == None, tei_bto.teiHeader.fileDesc.publicationStmt.distributor.address
assert tei_bto.teiHeader.fileDesc.publicationStmt.availability.status == "restricted", tei_bto.teiHeader.fileDesc.publicationStmt.availability.status
assert tei_bto.teiHeader.fileDesc.publicationStmt.availability.p.text == "à utiliser dans un cadre de recherche ou d'enseignement après accord du dépositaire des droits", tei_bto.teiHeader.fileDesc.publicationStmt.availability.p.text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.lang == "fr", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.lang
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].id == "traducteur", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].id
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].surname == "Lastname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].surname
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].forename == "Firstname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].forename
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datebirth == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datebirth
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datedead == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datedead
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].id == "auteurOriginal", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].id
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].surname == "Lastname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].surname
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].forename == "Firstname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].forename
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datebirth == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datebirth
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datedead == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datedead
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].type == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].text == "Title", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].type == "parallel", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].text == "Subtitle", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.date == "Date", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.date
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.publisher == "Publisher", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.publisher
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.series == "Series", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.series
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.pubplace == "Place", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.pubplace
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].type == "ISBN", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].text == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].type == "numero edition", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].text == "123", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].text
assert tei_bto.teiHeader.encodingDesc.projectDesc.p[0].text == "BaTelÒc : Basa de Tèxtes en Lenga Occitana", tei_bto.teiHeader.encodingDesc.projectDesc.p[0].text
assert tei_bto.teiHeader.encodingDesc.projectDesc.p[1].text == "Encodatge de tèxtes occitans segon la nòrma de la Text Encoding Initiative, TEIP5", tei_bto.teiHeader.encodingDesc.projectDesc.p[1].text
assert tei_bto.teiHeader.encodingDesc.projectDesc.p[2].text == "http://www.tei-c.org/release/doc/tei-p5-doc", tei_bto.teiHeader.encodingDesc.projectDesc.p[2].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.bibl == "Frantext", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.bibl
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].type == "dialecte", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].catDesc[0].text == "Lengadocian", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].catDesc[0].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].type == "graphie", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].catDesc[0].text == None, tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].catDesc[0].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].type == "genre", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].type == "principal", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].text == "ensag", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].type == "sub", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].text == None, tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].type == "corpus", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].type
assert len(tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].catDesc) == 0, len(tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].catDesc)
assert tei_bto.teiHeader.profileDesc.creation.date == "2003", tei_bto.teiHeader.profileDesc.creation.date
assert tei_bto.teiHeader.profileDesc.langUsage.language.ident == "oc", tei_bto.teiHeader.profileDesc.langUsage.language.ident
assert tei_bto.teiHeader.profileDesc.langUsage.language.text == "Occitan", tei_bto.teiHeader.profileDesc.langUsage.language.text

# Test text body
assert tei_bto.text.body.div[0].__class__.__name__ == "div", tei_bto.text.body.div[0].__class__.__name__
assert tei_bto.text.body.div[0].text == '', tei_bto.text.body.div[0].text
assert tei_bto.text.body.div[0].head.text == None, tei_bto.text.body.div[0].head.text
assert tei_bto.text.body.div[0].p[0].text == "This is a quote.", tei_bto.text.body.div[0].p[0].text
assert tei_bto.text.body.div[0].p[1].text == "Firstname LASTNAME.", tei_bto.text.body.div[0].p[1].text
assert tei_bto.text.body.div[1].__class__.__name__ == "div", tei_bto.text.body.div[1].__class__.__name__
assert tei_bto.text.body.div[1].text == '', tei_bto.text.body.div[1].text
assert tei_bto.text.body.div[1].head.text == None, tei_bto.text.body.div[1].head.text
assert tei_bto.text.body.div[1].p[0].text == "Aquò es un exemple.", tei_bto.text.body.div[1].p[0].text
assert tei_bto.text.body.div[1].p[1].text == "Amb qualquas frasas.", tei_bto.text.body.div[1].p[1].text
assert tei_bto.text.body.div[1].p[2].text == "E de partidas en italicas. De questions? O encara: d'exclamacions! Plan.", tei_bto.text.body.div[1].p[2].text
assert tei_bto.text.body.div[1].p[3].text == "De verguetas : \"100% des tests doivent passer\". Totjorn. \"Alara ?\"", tei_bto.text.body.div[1].p[3].text
assert tei_bto.text.body.div[1].p[4].text == "Ça, c'est une phrase qui commence par un caractère spécial. Ô oui! Ò aquesta tanben.", tei_bto.text.body.div[1].p[4].text
assert tei_bto.text.body.div[2].__class__.__name__ == "div", tei_bto.text.body.div[2].__class__.__name__
assert tei_bto.text.body.div[2].text == '', tei_bto.text.body.div[2].text
assert tei_bto.text.body.div[2].head.text == "Titre du chapitre", tei_bto.text.body.div[2].head.text
assert tei_bto.text.body.div[2].p[0].text == "Maintenant testons les abbréviations comme F.T.P ou F.F.I. par exemple. Ou St. (St ?) Mr. et Ste Mme.", tei_bto.text.body.div[2].p[0].text
assert tei_bto.text.body.div[2].p[1].text == "Ainsi que les différentes ponctuations,  comme ; et encore : ainsi de suite... Voilà.", tei_bto.text.body.div[2].p[1].text
assert tei_bto.text.body.div[2].p[2].text == "Nous devons aussi tester les dialogues. Quelqu'un dit : - Que fait-on ? Doit-on continuer ?", tei_bto.text.body.div[2].p[2].text
assert tei_bto.text.body.div[2].p[3].text == "- Je ne sais pas... Qu'en penses-tu ?", tei_bto.text.body.div[2].p[3].text
assert tei_bto.text.body.div[3].__class__.__name__ == "div", tei_bto.text.body.div[3].__class__.__name__
assert tei_bto.text.body.div[3].text == '', tei_bto.text.body.div[3].text
assert tei_bto.text.body.div[3].head.text == None, tei_bto.text.body.div[3].head.text
assert tei_bto.text.body.div[3].p[0].text == "C'est la fin. On termine avec une signature.", tei_bto.text.body.div[3].p[0].text

## Simply export it to BaTelÒc XML
pyteilib.tei_write(tei_bto, OUTPUT_DIR + "example2_bto.xml", xml_type='BTO')
assert tei_bto.get_filename() == OUTPUT_DIR + "example2_bto.xml", tei_bto.get_filename()

## Release created objects
del tei_pclv8, tei_bto

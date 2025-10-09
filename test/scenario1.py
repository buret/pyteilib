#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import TEI library properly
# Also automatically define 'ftest_path' as location of pyteilib/test/ folder
from startup import *
import os
from datetime import datetime

INPUT_DIR = ftest_path + "input/"
OUTPUT_DIR = ftest_path + "output/"
# Create result folder
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

#### Scenario 1 : Read BaTelÒc XML and transform it to ParCoLab v8/v9 XML

### Do not keep highlighted text

## Read BaTelÒc XML and set TEI identifier
tei_bto = pyteilib.tei_read(INPUT_DIR + "example1_bto.xml", xml_type='BTO', keep_highlighted=False)
tei_bto.id = "test_1"
assert tei_bto.__class__.__name__ == "BTO", tei_bto.__class__.__name__
assert tei_bto.get_filename() == INPUT_DIR + "example1_bto.xml", tei_bto.get_filename()

# Test teiHeader
assert tei_bto.teiHeader.fileDesc.titleStmt.title == "Title", tei_bto.teiHeader.fileDesc.titleStmt.title
assert tei_bto.teiHeader.fileDesc.titleStmt.author[0].text == "Author Qualqu'un", tei_bto.teiHeader.fileDesc.titleStmt.author[0].text
assert tei_bto.teiHeader.fileDesc.titleStmt.editor == "CLLE-ERSS TELOC", tei_bto.teiHeader.fileDesc.titleStmt.editor
assert tei_bto.teiHeader.fileDesc.titleStmt.principal == "Firstname Lastname", tei_bto.teiHeader.fileDesc.titleStmt.principal
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].resp == "balhaire fichièr sorga", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].name == "Firstname Lastname, organisation", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[0].name
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].resp == "portaire fichièr sorga", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].name == "Firstame Lastname", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[1].name
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].resp == "pretractament e balisatge del tèxte segon la TEI P5", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].name == "Firstame Lastname (body)", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[2].name
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].resp == "donadas pel header", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].name == "Firstame Lastname (header)", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[3].name
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[4].resp == "-", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[4].resp
assert tei_bto.teiHeader.fileDesc.titleStmt.respStmt[4].name == "-", tei_bto.teiHeader.fileDesc.titleStmt.respStmt[4].name
assert tei_bto.teiHeader.fileDesc.editionStmt.edition.date == "01/01/2001", tei_bto.teiHeader.fileDesc.editionStmt.edition.date
assert tei_bto.teiHeader.fileDesc.extent == "0 Ko", tei_bto.teiHeader.fileDesc.extent
assert tei_bto.teiHeader.fileDesc.publicationStmt.distributor.name == "CLLE-ERSS", tei_bto.teiHeader.fileDesc.publicationStmt.distributor.name
assert tei_bto.teiHeader.fileDesc.publicationStmt.distributor.address == """Maison de la recherche
                            5 allées Antonio Machado
                            F 31058 TOULOUSE CEDEX""", tei_bto.teiHeader.fileDesc.publicationStmt.distributor.address
assert tei_bto.teiHeader.fileDesc.publicationStmt.availability.status == "restricted", tei_bto.teiHeader.fileDesc.publicationStmt.availability.status
assert tei_bto.teiHeader.fileDesc.publicationStmt.availability.p.text == "à utiliser dans un cadre de recherche ou d'enseignement après accord du dépositaire des droits", tei_bto.teiHeader.fileDesc.publicationStmt.availability.p.text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.lang == "FR", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.lang
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].id == "traducteur", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].id
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].surname == "Lastname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].surname
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].forename == "Firstname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].forename
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datebirth == "DOB", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datebirth
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datedead == "DOD", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[0].datedead
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].id == "auteurOriginal", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].id
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].surname == "Lastname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].surname
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].forename == "Firstname", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].forename
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datebirth == "DOB", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datebirth
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datedead == "-", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author[1].datedead
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].type == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].text == "Main title", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[0].text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].type == "parallel", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].text == "Parallel title", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title[1].text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.date == "Date", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.date
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.publisher == "Publisher", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.publisher
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.series == "Series", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.series
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.pubplace == "Place", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.pubplace
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].type == "ISBN", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].text == "0-12345-678-9", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[0].text
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].type == "numero edition", tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].type
assert tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].text == None, tei_bto.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno[1].text
assert tei_bto.teiHeader.encodingDesc.projectDesc.p[0].text == "BaTelÒc : Basa de Tèxtes en Lenga Occitana", tei_bto.teiHeader.encodingDesc.projectDesc.p[0].text
assert tei_bto.teiHeader.encodingDesc.projectDesc.p[1].text == "Encodatge de tèxtes occitans segon la nòrma de la Text Encoding Initiative, TEIP5", tei_bto.teiHeader.encodingDesc.projectDesc.p[1].text
assert tei_bto.teiHeader.encodingDesc.projectDesc.p[2].text == "http://www.tei-c.org/release/doc/tei-p5-doc", tei_bto.teiHeader.encodingDesc.projectDesc.p[2].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.bibl == "Frantext", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.bibl
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].type == "dialecte", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].catDesc[0].text == "lengadocian", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[0].catDesc[0].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].type == "graphie", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].catDesc[0].text == "classica", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[1].catDesc[0].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].type == "genre", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].type == "principal", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].text == "ensag", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[0].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].type == "sub", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].text == None, tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc[1].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].type == "corpus", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].type
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].catDesc[0].text == "descobèrta", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].catDesc[0].text
assert tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].catDesc[1].text == "roergue", tei_bto.teiHeader.encodingDesc.classDecl.taxonomy.category[3].catDesc[0].text
assert tei_bto.teiHeader.profileDesc.creation.date == "2003", tei_bto.teiHeader.profileDesc.creation.date
assert tei_bto.teiHeader.profileDesc.langUsage.language.ident == "oc", tei_bto.teiHeader.profileDesc.langUsage.language.ident
assert tei_bto.teiHeader.profileDesc.langUsage.language.text == "occitan", tei_bto.teiHeader.profileDesc.langUsage.language.text

# Test text front
assert tei_bto.text.front.docTitle.bibl.docAuthor == "Firstname Lastname", tei_bto.text.front.docTitle.bibl.docAuthor
assert tei_bto.text.front.docTitle.titlePart.type == "principal", tei_bto.text.front.docTitle.titlePart.type
assert tei_bto.text.front.docTitle.titlePart.text == "TITLE", tei_bto.text.front.docTitle.titlePart.text
assert tei_bto.text.front.docTitle.dedicace == "Per Firstname", tei_bto.text.front.docTitle.dedicace
assert tei_bto.text.front.docTitle.epigraph.quote.lang == "en", tei_bto.text.front.docTitle.epigraph.quote.lang
assert tei_bto.text.front.docTitle.epigraph.quote.text == "This is a quote.", tei_bto.text.front.docTitle.epigraph.quote.text
assert tei_bto.text.front.docTitle.epigraph.cit.text == "Citation epigraph.", tei_bto.text.front.docTitle.epigraph.cit.text
assert tei_bto.text.front.docTitle.epigraph.bibl.text == "Firstname LASTNAME.", tei_bto.text.front.docTitle.epigraph.bibl.text
assert tei_bto.text.front.titlePage.epigraph.cit.quote.text == "Citation épigraphe 1.", tei_bto.text.front.titlePage.epigraph.cit.quote.text
assert tei_bto.text.front.titlePage.epigraph.note == "Note épigraphe 1.", tei_bto.text.front.titlePage.epigraph.note
assert tei_bto.text.front.div[0].type == "preface", tei_bto.text.front.div.type
assert tei_bto.text.front.div[0].p[0].text == "Ceci est une préface.", tei_bto.text.front.div[0].p[0].text
assert tei_bto.text.front.div[0].p[1].text == "Avec plusieurs paragraphes.", tei_bto.text.front.div[0].p[1].text
assert tei_bto.text.front.div[1].type == "ack", tei_bto.text.front.div[1].type
assert tei_bto.text.front.div[1].text == "Remerciements.", tei_bto.text.front.div[1].text
assert tei_bto.text.front.div[2].type == "dedication", tei_bto.text.front.div[2].type
assert tei_bto.text.front.div[2].text == "Dédicace.", tei_bto.text.front.div[2].text
assert tei_bto.text.front.prologue.text == "Ceci est un prologue.", tei_bto.text.front.prologue.text
assert tei_bto.text.front.prologue.p[0].text == "Avec un premier parapgraphe.", tei_bto.text.front.prologue.p[0].text
assert tei_bto.text.front.prologue.p[1].text == "Et un second paragraphe.", tei_bto.text.front.prologue.p[1].text

# Test text body
assert tei_bto.text.body.div[0].epigraph.cit.quote.text == "Citation épigraphe 2.", tei_bto.text.body.div[0].epigraph.cit.quote.text
assert tei_bto.text.body.div[0].epigraph.cit.bibl.title.text == "Titre épigraphe 2.", tei_bto.text.body.div[0].epigraph.cit.bibl.title.text
assert tei_bto.text.body.div[0].epigraph.cit.bibl.author.text == "Auteur épigraphe 2.", tei_bto.text.body.div[0].epigraph.cit.bibl.author.text
assert tei_bto.text.body.div[1].type == "sous-partie1", tei_bto.text.body.div[1].type
assert tei_bto.text.body.div[1].p[0].text == "Aquò es un exemple.", tei_bto.text.body.div[1].p[0].text
assert tei_bto.text.body.div[1].p[1].text == "Amb qualquas frasas.", tei_bto.text.body.div[1].p[1].text
assert tei_bto.text.body.div[1].p[2].text == "E de partidas en italicas. De questions? O encara: d'exclamacions! Plan.", tei_bto.text.body.div[1].p[2].text
assert tei_bto.text.body.div[1].p[3].text == "De verguetas : \"100% des tests doivent passer\". Totjorn. \"Alara ?\"", tei_bto.text.body.div[1].p[3].text
assert tei_bto.text.body.div[1].p[4].text == "Ça, c'est une phrase qui commence par un caractère spécial. Ô oui! Ò aquesta tanben.", tei_bto.text.body.div[1].p[4].text
assert tei_bto.text.body.div[2].type == "sous-partie1", tei_bto.text.body.div[2].type
assert tei_bto.text.body.div[2].head.text == "Titre de la sous-partie 1", tei_bto.text.body.div[2].head.text
assert tei_bto.text.body.div[2].p[0].text == "Maintenant testons les abbréviations comme F.T.P ou F.F.I. par exemple. Ou St. (St ?) Mr. et Ste Mme.", tei_bto.text.body.div[2].p[0].text
assert tei_bto.text.body.div[2].p[1].text == "Ainsi que les différentes ponctuations,  comme ; et encore : ainsi de suite... Voilà.", tei_bto.text.body.div[2].p[1].text
assert tei_bto.text.body.div[2].p[2].text == "Nous devons aussi tester les dialogues. Quelqu'un dit : - Que fait-on ? Doit-on continuer ?", tei_bto.text.body.div[2].p[2].text
assert tei_bto.text.body.div[2].p[3].text == "- Je ne sais pas... Qu'en penses-tu ?", tei_bto.text.body.div[2].p[3].text
assert tei_bto.text.body.div[3].type == "chapitre", tei_bto.text.body.div[3].type
assert tei_bto.text.body.div[3].head.text == "POSTFACI", tei_bto.text.body.div[3].head.text
assert tei_bto.text.body.div[3].p[0].text == "C'est la fin. On termine avec une signature.", tei_bto.text.body.div[3].p[0].text
assert tei_bto.text.body.div[3].p[1].text == """Aquí, uèi
                     - F. L.""", tei_bto.text.body.div[3].p[1].text
assert tei_bto.text.body.div[4].__class__.__name__ == "div1", tei_bto.text.body.div[4].__class__.__name__
assert tei_bto.text.body.div[4].type == "chapter", tei_bto.text.body.div[4].type
assert tei_bto.text.body.div[4].head.text == "Titre du chapitre 1", tei_bto.text.body.div[4].head.text
assert tei_bto.text.body.div[4].p[0].text == "Contenu de chapitre 1.", tei_bto.text.body.div[4].p[0].text
assert tei_bto.text.body.div[4].div[0].__class__.__name__ == "div2", tei_bto.text.body.div[4].div[0].__class__.__name__
assert tei_bto.text.body.div[4].div[0].head.text == "Titre de la sous-partie du chapitre 1", tei_bto.text.body.div[4].div[0].head.text
assert tei_bto.text.body.div[4].div[0].p[0].text == "Sous-partie du chapitre 1.", tei_bto.text.body.div[4].div[0].p[0].text
assert tei_bto.text.body.div[4].div[0].div[0].__class__.__name__ == "div3", tei_bto.text.body.div[4].div[0].div[0].__class__.__name__
assert tei_bto.text.body.div[4].div[0].div[0].p[0].text == "Encore une sous-partie.", tei_bto.text.body.div[4].div[0].div[0].p.text
assert tei_bto.text.body.div[5].head.text == "Dernier chapitre", tei_bto.text.body.div[5].head.text

# Test text back
assert tei_bto.text.back.epilogue.div[0].__class__.__name__ == "div2", tei_bto.text.back.epilogue.div[0].__class__.__name__
assert tei_bto.text.back.epilogue.div[0].type == "chapter", tei_bto.text.back.epilogue.div[0].type
assert tei_bto.text.back.epilogue.div[0].head.text == "Epilòg", tei_bto.text.back.epilogue.div[0].head.text
assert tei_bto.text.back.epilogue.div[1].__class__.__name__ == "div2", tei_bto.text.back.epilogue.div[1].__class__.__name__
assert tei_bto.text.back.epilogue.div[1].type == "chapter", tei_bto.text.back.epilogue.div[1].type
assert tei_bto.text.back.epilogue.div[1].head.text == "TITOL", tei_bto.text.back.epilogue.div[1].head.text
assert tei_bto.text.back.epilogue.div[1].p[0].text == "\"Aquì lo tèxte.", tei_bto.text.back.epilogue.div[1].p[0].text
assert tei_bto.text.back.epilogue.div[1].p[1].text == "- Va plan !\"", tei_bto.text.back.epilogue.div[1].p[1].text
assert tei_bto.text.back.epilogue.div[1].p[2].text == "E aquì tanben.", tei_bto.text.back.epilogue.div[1].p[2].text
assert tei_bto.text.back.epilogue.div[1].p[3].text == "\"Ici un texte en français\".", tei_bto.text.back.epilogue.div[1].p[3].text
assert tei_bto.text.back.epilogue.div[1].note.n == "1", tei_bto.text.back.epilogue.div[1].note.n
assert tei_bto.text.back.epilogue.div[1].note.place == "foot", tei_bto.text.back.epilogue.div[1].note.place
assert tei_bto.text.back.epilogue.div[1].note.text == "Note à ne pas conserver.", tei_bto.text.back.epilogue.div[1].note.text
assert tei_bto.text.back.epilogue.div[1].p[4].text == "", tei_bto.text.back.epilogue.div[1].p[4].text
assert tei_bto.text.back.epilogue.div[1].p[4].s[0].text == None, tei_bto.text.back.epilogue.div[1].p[4].s[0].text
assert tei_bto.text.back.epilogue.div[1].p[4].s[1].text == "Primièra frasa", tei_bto.text.back.epilogue.div[1].p[4].s[1].text
assert tei_bto.text.back.epilogue.div[1].p[4].s[2].text == "Allez !", tei_bto.text.back.epilogue.div[1].p[4].s[2].text
assert tei_bto.text.back.div[0].__class__.__name__ == "div1", tei_bto.text.back.div[0].__class__.__name__
assert tei_bto.text.back.div[0].type == "subpart", tei_bto.text.back.div[0].type
assert tei_bto.text.back.div[0].head.text == None, tei_bto.text.back.div[0].head.text
assert tei_bto.text.back.div[0].note.div[0].__class__.__name__ == "div2", tei_bto.text.back.div[0].note.div[0].__class__.__name__
assert tei_bto.text.back.div[0].note.div[0].type == "chapter", tei_bto.text.back.div[0].note.div[0].type
assert tei_bto.text.back.div[0].note.div[0].head.text == "NOTES DE L'AUTEUR", tei_bto.text.back.div[0].note.div[0].head.text
assert tei_bto.text.back.div[0].note.div[1].__class__.__name__ == "div2", tei_bto.text.back.div[0].note.div[1].__class__.__name__
assert tei_bto.text.back.div[0].note.div[1].type == "chapter", tei_bto.text.back.div[0].note.div[0].type
assert tei_bto.text.back.div[0].note.div[1].head.text == "TITRE", tei_bto.text.back.div[0].note.div[0].head.text
assert tei_bto.text.back.div[0].note.div[1].p[0].text == "Ici des notes en français", tei_bto.text.back.div[0].note.div[1].p[0].text
assert tei_bto.text.back.div[0].note.div[1].p[1].text == "", tei_bto.text.back.div[0].note.div[1].p[1].text
assert tei_bto.text.back.div[0].note.div[1].p[1].s[0].text == "- Item 1.", tei_bto.text.back.div[0].note.div[1].p[1].s[0].text
assert tei_bto.text.back.div[0].note.div[1].p[1].s[1].text == "- Item 2.", tei_bto.text.back.div[0].note.div[1].p[1].s[1].text

## Simply export it to BaTelÒc XML
pyteilib.tei_write(tei_bto, OUTPUT_DIR + "example1_bto.xml", xml_type='BTO')
assert tei_bto.get_filename() == OUTPUT_DIR + "example1_bto.xml", tei_bto.get_filename()

## Transform it to ParCoLab v8 XML
tei_pclv8 = pyteilib.transform(tei_bto, from_type='BTO', to_type='PCLv8')
assert tei_pclv8.__class__.__name__ == "PCLv8", tei_pclv8.__class__.__name__
assert tei_pclv8.id == "test_1", tei_pclv8.id

# Test teiHeader
assert tei_pclv8.teiHeader.fileDesc.titleStmt.title == "Main title", tei_pclv8.teiHeader.fileDesc.titleStmt.title
assert tei_pclv8.teiHeader.fileDesc.titleStmt.subtitle == "Parallel title", tei_pclv8.teiHeader.fileDesc.titleStmt.subtitle
assert tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.forename == "Firstname", tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.surname == "Lastname", tei_pclv8.teiHeader.fileDesc.titleStmt.author[0].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].resp == "translator", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename == "Firstname", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname == "Lastname", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].resp == "translator", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[1].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[2].resp == "translator", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[2].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[3].resp == "transcriber", tei_pclv8.teiHeader.fileDesc.titleStmt.respStmt[3].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.collection == "BaTelÒc", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.collection
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp == "resp_collection", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename == "Firstname", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname == "Lastname", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp == "resp_collection", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp
assert tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].resp == "resp_collection", tei_pclv8.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].resp
assert tei_pclv8.teiHeader.fileDesc.editionStmt.edition.text == "Series", tei_pclv8.teiHeader.fileDesc.editionStmt.edition.text
assert tei_pclv8.teiHeader.fileDesc.extent.measure.unit == "words", tei_pclv8.teiHeader.fileDesc.extent.measure.unit
assert tei_pclv8.teiHeader.fileDesc.extent.measure.quantity == 181, tei_pclv8.teiHeader.fileDesc.extent.measure.quantity
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.publisher == "Publisher", tei_pclv8.teiHeader.fileDesc.publicationStmt.publisher
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.pubPlace == "Place", tei_pclv8.teiHeader.fileDesc.publicationStmt.pubPlace
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.date == "Date", tei_pclv8.teiHeader.fileDesc.publicationStmt.date
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.text == "restricted", tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.text
assert tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.p.text == "à utiliser dans un cadre de recherche ou d'enseignement après accord du dépositaire des droits", tei_pclv8.teiHeader.fileDesc.publicationStmt.availability.licence.p.text
assert tei_pclv8.teiHeader.fileDesc.sourceDesc.text == "Imported from BaTelÒc", tei_pclv8.teiHeader.fileDesc.sourceDesc.text
assert tei_pclv8.teiHeader.encodingDesc.projectDesc.p[0].text == "BaTelÒc : Basa de Tèxtes en Lenga Occitana", tei_pclv8.teiHeader.encodingDesc.projectDesc.p[0].text
assert tei_pclv8.teiHeader.encodingDesc.projectDesc.p[1].text == "Encodatge de tèxtes occitans segon la nòrma de la Text Encoding Initiative, TEIP5", tei_pclv8.teiHeader.encodingDesc.projectDesc.p[1].text
assert tei_pclv8.teiHeader.encodingDesc.projectDesc.p[2].text == "http://www.tei-c.org/release/doc/tei-p5-doc", tei_pclv8.teiHeader.encodingDesc.projectDesc.p[2].text
assert tei_pclv8.teiHeader.profileDesc.langUsage.language.ident == "oc", tei_pclv8.teiHeader.profileDesc.langUsage.language.ident
assert tei_pclv8.teiHeader.profileDesc.langUsage.language.langOri == "oc", tei_pclv8.teiHeader.profileDesc.langUsage.language.langOri
assert tei_pclv8.teiHeader.profileDesc.category.type == "dialecte", tei_pclv8.teiHeader.profileDesc.category.type
assert tei_pclv8.teiHeader.profileDesc.category.catDesc[0].text == "lengadocian", tei_pclv8.teiHeader.profileDesc.category.catDesc[0].text
assert tei_pclv8.teiHeader.profileDesc.creation.date == "2003", tei_pclv8.teiHeader.profileDesc.creation.date
assert tei_pclv8.teiHeader.profileDesc.textDesc.derivation.type == "original", tei_pclv8.teiHeader.profileDesc.derivation.type
assert tei_pclv8.teiHeader.profileDesc.textDesc.domain[0].type == "literature", tei_pclv8.teiHeader.profileDesc.textDesc.domain[0].type
assert tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].lang == "en", tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].lang
assert tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].type == "essay", tei_pclv8.teiHeader.profileDesc.textDesc.genre[0].type
assert tei_pclv8.teiHeader.profileDesc.textDesc.genre[1].lang == "oc", tei_pclv8.teiHeader.profileDesc.textDesc.genre[1].lang
assert tei_pclv8.teiHeader.profileDesc.textDesc.genre[1].type == "ensag", tei_pclv8.teiHeader.profileDesc.textDesc.genre[1].type
assert tei_pclv8.teiHeader.profileDesc.textDesc.textForm.type == "prose", tei_pclv8.teiHeader.profileDesc.textDesc.textForm.type

# Test text body
assert tei_pclv8.text.body.div[0].__class__.__name__ == "div", tei_pclv8.text.body.div[0].__class__.__name__
assert tei_pclv8.text.body.div[0].text == None, tei_pclv8.text.body.div[0].text
assert tei_pclv8.text.body.div[0].head.seg == None, tei_pclv8.text.body.div[0].head.seg
assert tei_pclv8.text.body.div[0].p[0].text == None, tei_pclv8.text.body.div[0].p[0].text
assert tei_pclv8.text.body.div[0].p[0].s[0].text == "Ceci est un prologue.", tei_pclv8.text.body.div[0].p[0].s[0].text
assert tei_pclv8.text.body.div[0].p[1].text == None, tei_pclv8.text.body.div[0].p[1].text
assert tei_pclv8.text.body.div[0].p[1].s[0].text == "Avec un premier parapgraphe.", tei_pclv8.text.body.div[0].p[1].s[0].text
assert tei_pclv8.text.body.div[0].p[2].text == None, tei_pclv8.text.body.div[0].p[2].text
assert tei_pclv8.text.body.div[0].p[2].s[0].text == "Et un second paragraphe.", tei_pclv8.text.body.div[0].p[2].s[0].text
assert tei_pclv8.text.body.div[1].__class__.__name__ == "div", tei_pclv8.text.body.div[1].__class__.__name__
assert tei_pclv8.text.body.div[1].text == None, tei_pclv8.text.body.div[1].text
assert tei_pclv8.text.body.div[1].head.seg == None, tei_pclv8.text.body.div[1].head.seg
assert tei_pclv8.text.body.div[1].p[0].text == None, tei_pclv8.text.body.div[1].p[0].text
assert tei_pclv8.text.body.div[1].p[0].s[0].text == "Aquò es un exemple.", tei_pclv8.text.body.div[1].p[0].s[0].text
assert tei_pclv8.text.body.div[1].p[1].text == None, tei_pclv8.text.body.div[1].p[1].text
assert tei_pclv8.text.body.div[1].p[1].s[0].text == "Amb qualquas frasas.", tei_pclv8.text.body.div[1].p[1].s[0].text
assert tei_pclv8.text.body.div[1].p[2].text == None, tei_pclv8.text.body.div[1].p[2].text
assert tei_pclv8.text.body.div[1].p[2].s[0].text == "E de partidas en italicas.", tei_pclv8.text.body.div[1].p[2].s[0].text
assert tei_pclv8.text.body.div[1].p[2].s[1].text == "De questions?", tei_pclv8.text.body.div[1].p[2].s[1].text
assert tei_pclv8.text.body.div[1].p[2].s[2].text == "O encara: d'exclamacions!", tei_pclv8.text.body.div[1].p[2].s[2].text
assert tei_pclv8.text.body.div[1].p[2].s[3].text == "Plan.", tei_pclv8.text.body.div[1].p[2].s[3].text
assert tei_pclv8.text.body.div[1].p[3].text == None, tei_pclv8.text.body.div[1].p[3].text
assert tei_pclv8.text.body.div[1].p[3].s[0].text == "De verguetas : \"100% des tests doivent passer\".", tei_pclv8.text.body.div[1].p[3].s[0].text
assert tei_pclv8.text.body.div[1].p[3].s[1].text == "Totjorn.", tei_pclv8.text.body.div[1].p[3].s[1].text
assert tei_pclv8.text.body.div[1].p[3].s[2].text == "\"Alara ?\"", tei_pclv8.text.body.div[1].p[3].s[2].text
assert tei_pclv8.text.body.div[1].p[4].text == None, tei_pclv8.text.body.div[1].p[4].text
assert tei_pclv8.text.body.div[1].p[4].s[0].text == "Ça, c'est une phrase qui commence par un caractère spécial.", tei_pclv8.text.body.div[1].p[4].s[0].text
assert tei_pclv8.text.body.div[1].p[4].s[1].text == "Ô oui!", tei_pclv8.text.body.div[1].p[4].s[1].text
assert tei_pclv8.text.body.div[1].p[4].s[2].text == "Ò aquesta tanben.", tei_pclv8.text.body.div[1].p[4].s[2].text
assert tei_pclv8.text.body.div[2].__class__.__name__ == "div", tei_pclv8.text.body.div[2].__class__.__name__
assert tei_pclv8.text.body.div[2].text == None, tei_pclv8.text.body.div[2].text
assert tei_pclv8.text.body.div[2].head.seg == "Titre de la sous-partie 1", tei_pclv8.text.body.div[2].head.seg
assert tei_pclv8.text.body.div[2].p[0].text == None, tei_pclv8.text.body.div[2].p[0].text
assert tei_pclv8.text.body.div[2].p[0].s[0].text == "Maintenant testons les abbréviations comme F.T.P ou F.F.I. par exemple.", tei_pclv8.text.body.div[2].p[0].s[0].text
assert tei_pclv8.text.body.div[2].p[0].s[1].text == "Ou St.", tei_pclv8.text.body.div[2].p[0].s[1].text
assert tei_pclv8.text.body.div[2].p[0].s[2].text == "(St ?)", tei_pclv8.text.body.div[2].p[0].s[2].text
assert tei_pclv8.text.body.div[2].p[0].s[3].text == "Mr. et Ste Mme.", tei_pclv8.text.body.div[2].p[0].s[3].text
assert tei_pclv8.text.body.div[2].p[1].text == None, tei_pclv8.text.body.div[2].p[1].text
assert tei_pclv8.text.body.div[2].p[1].s[0].text == "Ainsi que les différentes ponctuations,  comme ; et encore : ainsi de suite...", tei_pclv8.text.body.div[2].p[1].s[0].text
assert tei_pclv8.text.body.div[2].p[1].s[1].text == "Voilà.", tei_pclv8.text.body.div[2].p[1].s[1].text
assert tei_pclv8.text.body.div[2].p[2].text == None, tei_pclv8.text.body.div[2].p[2].text
assert tei_pclv8.text.body.div[2].p[2].s[0].text == "Nous devons aussi tester les dialogues.", tei_pclv8.text.body.div[2].p[2].s[0].text
assert tei_pclv8.text.body.div[2].p[2].s[1].text == "Quelqu'un dit : - Que fait-on ?", tei_pclv8.text.body.div[2].p[2].s[1].text
assert tei_pclv8.text.body.div[2].p[2].s[2].text == "Doit-on continuer ?", tei_pclv8.text.body.div[2].p[2].s[2].text
assert tei_pclv8.text.body.div[2].p[3].text == None, tei_pclv8.text.body.div[2].p[3].text
assert tei_pclv8.text.body.div[2].p[3].s[0].text == "- Je ne sais pas...", tei_pclv8.text.body.div[2].p[3].s[0].text
assert tei_pclv8.text.body.div[2].p[3].s[1].text == "Qu'en penses-tu ?", tei_pclv8.text.body.div[2].p[3].s[1].text
assert tei_pclv8.text.body.div[3].__class__.__name__ == "div", tei_pclv8.text.body.div[3].__class__.__name__
assert tei_pclv8.text.body.div[3].text == None, tei_pclv8.text.body.div[3].text
assert tei_pclv8.text.body.div[3].head.seg == "POSTFACI", tei_pclv8.text.body.div[3].head.seg
assert tei_pclv8.text.body.div[3].p[0].text == None, tei_pclv8.text.body.div[3].p[0].text
assert tei_pclv8.text.body.div[3].p[0].s[0].text == "C'est la fin.", tei_pclv8.text.body.div[3].p[0].s[0].text
assert tei_pclv8.text.body.div[3].p[0].s[1].text == "On termine avec une signature.", tei_pclv8.text.body.div[3].p[0].s[1].text
assert tei_pclv8.text.body.div[3].p[1].text == None, tei_pclv8.text.body.div[3].p[1].text
assert tei_pclv8.text.body.div[3].p[1].s[0].text == "Aquí, uèi", tei_pclv8.text.body.div[3].p[1].s[0].text
assert tei_pclv8.text.body.div[3].p[1].s[1].text == "- F. L.", tei_pclv8.text.body.div[3].p[1].s[1].text
assert tei_pclv8.text.body.div[4].__class__.__name__ == "div", tei_pclv8.text.body.div[4].__class__.__name__
assert tei_pclv8.text.body.div[4].text == None, tei_pclv8.text.body.div[4].text
assert tei_pclv8.text.body.div[4].head.seg == "Titre du chapitre 1", tei_pclv8.text.body.div[4].head.seg
assert tei_pclv8.text.body.div[4].p[0].text == None, tei_pclv8.text.body.div[4].p[0].text
assert tei_pclv8.text.body.div[4].p[0].s[0].text == "Contenu de chapitre 1.", tei_pclv8.text.body.div[4].p[0].s[0].text
assert tei_pclv8.text.body.div[5].__class__.__name__ == "div", tei_pclv8.text.body.div[5].__class__.__name__
assert tei_pclv8.text.body.div[5].text == None, tei_pclv8.text.body.div[5].text
assert tei_pclv8.text.body.div[5].head.seg == "Titre de la sous-partie du chapitre 1", tei_pclv8.text.body.div[5].head.seg
assert tei_pclv8.text.body.div[5].p[0].text == None, tei_pclv8.text.body.div[5].p[0].text
assert tei_pclv8.text.body.div[5].p[0].s[0].text == "Sous-partie du chapitre 1.", tei_pclv8.text.body.div[5].p[0].s[0].text
assert tei_pclv8.text.body.div[6].__class__.__name__ == "div", tei_pclv8.text.body.div[6].__class__.__name__
assert tei_pclv8.text.body.div[6].text == None, tei_pclv8.text.body.div[6].text
assert tei_pclv8.text.body.div[6].head.seg == None, tei_pclv8.text.body.div[6].head.seg
assert tei_pclv8.text.body.div[6].p[0].text == None, tei_pclv8.text.body.div[6].p[0].text
assert tei_pclv8.text.body.div[6].p[0].s[0].text == "Encore une sous-partie.", tei_pclv8.text.body.div[6].p[0].s[0].text
assert tei_pclv8.text.body.div[7].__class__.__name__ == "div", tei_pclv8.text.body.div[7].__class__.__name__
assert tei_pclv8.text.body.div[7].text == None, tei_pclv8.text.body.div[7].text
assert tei_pclv8.text.body.div[7].head.seg == "Dernier chapitre", tei_pclv8.text.body.div[7].head.seg
assert tei_pclv8.text.body.div[7].p[0].text == None, tei_pclv8.text.body.div[7].p[0].text
assert tei_pclv8.text.body.div[7].p[0].s[0].text == "Contenu du dernier chapitre.", tei_pclv8.text.body.div[7].p[0].s[0].text
assert tei_pclv8.text.body.div[8].__class__.__name__ == "div", tei_pclv8.text.body.div[8].__class__.__name__
assert tei_pclv8.text.body.div[8].head.seg == "Epilòg", tei_pclv8.text.body.div[8].head.seg
assert tei_pclv8.text.body.div[8].text == None, tei_pclv8.text.body.div[8].text
assert tei_pclv8.text.body.div[9].__class__.__name__ == "div", tei_pclv8.text.body.div[9].__class__.__name__
assert tei_pclv8.text.body.div[9].head.seg == "TITOL", tei_pclv8.text.body.div[9].head.seg
assert tei_pclv8.text.body.div[9].text == None, tei_pclv8.text.body.div[9].text
assert tei_pclv8.text.body.div[9].p[0].text == None, tei_pclv8.text.body.div[9].p[0].text
assert tei_pclv8.text.body.div[9].p[0].s[0].text == "\"Aquì lo tèxte.", tei_pclv8.text.body.div[9].p[0].s[0].text
assert tei_pclv8.text.body.div[9].p[1].text == None, tei_pclv8.text.body.div[9].p[1].text
assert tei_pclv8.text.body.div[9].p[1].s[0].text == "- Va plan !\"", tei_pclv8.text.body.div[9].p[1].s[0].text
assert tei_pclv8.text.body.div[9].p[2].text == None, tei_pclv8.text.body.div[9].p[2].text
assert tei_pclv8.text.body.div[9].p[2].s[0].text == "E aquì tanben.", tei_pclv8.text.body.div[9].p[2].s[0].text
assert tei_pclv8.text.body.div[9].p[3].text == None, tei_pclv8.text.body.div[9].p[3].text
assert tei_pclv8.text.body.div[9].p[3].s[0].text == "\"Ici un texte en français\".", tei_pclv8.text.body.div[9].p[3].s[0].text
assert tei_pclv8.text.body.div[9].note == None, tei_pclv8.text.body.div[9].note
assert tei_pclv8.text.body.div[9].p[4].text == None, tei_pclv8.text.body.div[9].p[4].text
assert tei_pclv8.text.body.div[9].p[4].s[0].text == "Primièra frasa", tei_pclv8.text.body.div[9].p[4].s[0].text
assert tei_pclv8.text.body.div[9].p[4].s[1].text == "Allez !", tei_pclv8.text.body.div[9].p[4].s[1].text

## Write it to ParCoLab v8 XML
pyteilib.tei_write(tei_pclv8, OUTPUT_DIR + "example1_pcl_v8.xml", xml_type='PCLv8')
assert tei_pclv8.get_filename() == OUTPUT_DIR + "example1_pcl_v8.xml", tei_pclv8.get_filename()

## Export metadata to v8 format
pyteilib.export_header(tei_pclv8, OUTPUT_DIR + "example1_metadata_v8.csv")

## Transform it to ParCoLab v9 XML
tei_pclv9 = pyteilib.transform(tei_bto, from_type='BTO', to_type='PCLv9')
assert tei_pclv9.__class__.__name__ == "PCLv9", tei_pclv9.__class__.__name__
assert tei_pclv9.id == "test_1", tei_pclv9.id

# Test teiHeader
assert tei_pclv9.teiHeader.fileDesc.titleStmt.title == "Main title", tei_pclv9.teiHeader.fileDesc.titleStmt.title
assert tei_pclv9.teiHeader.fileDesc.titleStmt.subtitle == "Parallel title", tei_pclv9.teiHeader.fileDesc.titleStmt.subtitle
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.forename == "Firstname", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.surname == "Lastname", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].birth == "DOB", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].death == "-", tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].placeName == None, tei_pclv9.teiHeader.fileDesc.titleStmt.author[0].placeName
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].resp == "translator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename == "Firstname", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname == "Lastname", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].birth == "DOB", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].birth
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].death == "DOD", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[0].death
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].resp == "translator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[1].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].resp == "translator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[2].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].resp == "transcriber", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[3].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].resp == "publisher_provider", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].name == "Firstname Lastname, organisation", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].date == None, tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[4].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].resp == "project_provider", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].name == "Firstame Lastname", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[5].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].resp == "teihdr_creator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].name == "Firstame Lastname (header)", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].date == None, tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[6].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].resp == "teibdy_creator", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].name == "Firstame Lastname (body)", tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].name
assert tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].date == None, tei_pclv9.teiHeader.fileDesc.titleStmt.respStmt[7].date
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.collection == "BaTelÒc", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.collection
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp == "resp_collection", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename == "Firstname", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname == "Lastname", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp == "resp_collection", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].resp
assert tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].resp == "resp_collection", tei_pclv9.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].resp
assert tei_pclv9.teiHeader.fileDesc.editionStmt.edition.text == "Series", tei_pclv9.teiHeader.fileDesc.editionStmt.edition.text
assert tei_pclv9.teiHeader.fileDesc.extent.measure.unit == "words", tei_pclv9.teiHeader.fileDesc.extent.measure.unit
assert tei_pclv9.teiHeader.fileDesc.extent.measure.quantity == 181, tei_pclv9.teiHeader.fileDesc.extent.measure.quantity
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.publisher == "Publisher", tei_pclv9.teiHeader.fileDesc.publicationStmt.publisher
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.pubPlace == "Place", tei_pclv9.teiHeader.fileDesc.publicationStmt.pubPlace
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.date == "Date", tei_pclv9.teiHeader.fileDesc.publicationStmt.date
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.type == "ISBN", tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.type
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.text == "0-12345-678-9", tei_pclv9.teiHeader.fileDesc.publicationStmt.idno.text
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.text == "restricted", tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.text
assert tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.p.text == "à utiliser dans un cadre de recherche ou d'enseignement après accord du dépositaire des droits", tei_pclv9.teiHeader.fileDesc.publicationStmt.availability.licence.p.text
assert tei_pclv9.teiHeader.fileDesc.sourceDesc.text == "Imported from BaTelÒc", tei_pclv9.teiHeader.fileDesc.sourceDesc.text
assert tei_pclv9.teiHeader.encodingDesc.projectDesc.p[0].text == "BaTelÒc : Basa de Tèxtes en Lenga Occitana", tei_pclv9.teiHeader.encodingDesc.projectDesc.p[0].text
assert tei_pclv9.teiHeader.encodingDesc.projectDesc.p[1].text == "Encodatge de tèxtes occitans segon la nòrma de la Text Encoding Initiative, TEIP5", tei_pclv9.teiHeader.encodingDesc.projectDesc.p[1].text
assert tei_pclv9.teiHeader.encodingDesc.projectDesc.p[2].text == "http://www.tei-c.org/release/doc/tei-p5-doc", tei_pclv9.teiHeader.encodingDesc.projectDesc.p[2].text
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.ident == "oc", tei_pclv9.teiHeader.profileDesc.langUsage.language.ident
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.langOri == "oc", tei_pclv9.teiHeader.profileDesc.langUsage.language.langOri
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.variant == "lengadocian", tei_pclv9.teiHeader.profileDesc.langUsage.language.variant
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.script == "classica", tei_pclv9.teiHeader.profileDesc.langUsage.language.script
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.variantOri == "lengadocian", tei_pclv9.teiHeader.profileDesc.langUsage.language.variantOri
assert tei_pclv9.teiHeader.profileDesc.langUsage.language.scriptOri == "classica", tei_pclv9.teiHeader.profileDesc.langUsage.language.scriptOri
assert tei_pclv9.teiHeader.profileDesc.creation.date == "2003", tei_pclv9.teiHeader.profileDesc.creation.date
assert tei_pclv9.teiHeader.profileDesc.textDesc.derivation.type == "original", tei_pclv9.teiHeader.profileDesc.derivation.type
assert tei_pclv9.teiHeader.profileDesc.textDesc.domain[0].type == "literature", tei_pclv9.teiHeader.profileDesc.textDesc.domain[0].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].lang == "en", tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].lang
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].type == "essay", tei_pclv9.teiHeader.profileDesc.textDesc.genre[0].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].lang == "oc", tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].lang
assert tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].type == "ensag", tei_pclv9.teiHeader.profileDesc.textDesc.genre[1].type
assert tei_pclv9.teiHeader.profileDesc.textDesc.textForm.type == "prose", tei_pclv9.teiHeader.profileDesc.textDesc.textForm.type
assert tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[0].text == "descobèrta", tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[0].text
assert tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[1].text == "roergue", tei_pclv9.teiHeader.profileDesc.textClass.keywords.term[1].text
assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].who == "pyteilib", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].who
assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].when == str(datetime.now()).split()[0], tei_pclv9.teiHeader.revisionDesc.listChange.change[0].when
assert tei_pclv9.teiHeader.revisionDesc.listChange.change[0].text == "File creation", tei_pclv9.teiHeader.revisionDesc.listChange.change[0].text

# Test text body
assert tei_pclv9.text.body.div[0].__class__.__name__ == "div", tei_pclv9.text.body.div[0].__class__.__name__
assert tei_pclv9.text.body.div[0].text == None, tei_pclv9.text.body.div[0].text
assert tei_pclv9.text.body.div[0].head.seg == None, tei_pclv9.text.body.div[0].head.seg
assert tei_pclv9.text.body.div[0].p[0].text == None, tei_pclv9.text.body.div[0].p[0].text
assert tei_pclv9.text.body.div[0].p[0].s[0].text == "Ceci est un prologue.", tei_pclv9.text.body.div[0].p[0].s[0].text
assert tei_pclv9.text.body.div[0].p[1].text == None, tei_pclv9.text.body.div[0].p[1].text
assert tei_pclv9.text.body.div[0].p[1].s[0].text == "Avec un premier parapgraphe.", tei_pclv9.text.body.div[0].p[1].s[0].text
assert tei_pclv9.text.body.div[0].p[2].text == None, tei_pclv9.text.body.div[0].p[2].text
assert tei_pclv9.text.body.div[0].p[2].s[0].text == "Et un second paragraphe.", tei_pclv9.text.body.div[0].p[2].s[0].text
assert tei_pclv9.text.body.div[1].__class__.__name__ == "div", tei_pclv9.text.body.div[1].__class__.__name__
assert tei_pclv9.text.body.div[1].text == None, tei_pclv9.text.body.div[1].text
assert tei_pclv9.text.body.div[1].head.seg == None, tei_pclv9.text.body.div[1].head.seg
assert tei_pclv9.text.body.div[1].p[0].text == None, tei_pclv9.text.body.div[1].p[0].text
assert tei_pclv9.text.body.div[1].p[0].s[0].text == "Aquò es un exemple.", tei_pclv9.text.body.div[1].p[0].s[0].text
assert tei_pclv9.text.body.div[1].p[1].text == None, tei_pclv9.text.body.div[1].p[1].text
assert tei_pclv9.text.body.div[1].p[1].s[0].text == "Amb qualquas frasas.", tei_pclv9.text.body.div[1].p[1].s[0].text
assert tei_pclv9.text.body.div[1].p[2].text == None, tei_pclv9.text.body.div[1].p[2].text
assert tei_pclv9.text.body.div[1].p[2].s[0].text == "E de partidas en italicas.", tei_pclv9.text.body.div[1].p[2].s[0].text
assert tei_pclv9.text.body.div[1].p[2].s[1].text == "De questions?", tei_pclv9.text.body.div[1].p[2].s[1].text
assert tei_pclv9.text.body.div[1].p[2].s[2].text == "O encara: d'exclamacions!", tei_pclv9.text.body.div[1].p[2].s[2].text
assert tei_pclv9.text.body.div[1].p[2].s[3].text == "Plan.", tei_pclv9.text.body.div[1].p[2].s[3].text
assert tei_pclv9.text.body.div[1].p[3].text == None, tei_pclv9.text.body.div[1].p[3].text
assert tei_pclv9.text.body.div[1].p[3].s[0].text == "De verguetas : \"100% des tests doivent passer\".", tei_pclv9.text.body.div[1].p[3].s[0].text
assert tei_pclv9.text.body.div[1].p[3].s[1].text == "Totjorn.", tei_pclv9.text.body.div[1].p[3].s[1].text
assert tei_pclv9.text.body.div[1].p[3].s[2].text == "\"Alara ?\"", tei_pclv9.text.body.div[1].p[3].s[2].text
assert tei_pclv9.text.body.div[1].p[4].text == None, tei_pclv9.text.body.div[1].p[4].text
assert tei_pclv9.text.body.div[1].p[4].s[0].text == "Ça, c'est une phrase qui commence par un caractère spécial.", tei_pclv9.text.body.div[1].p[4].s[0].text
assert tei_pclv9.text.body.div[1].p[4].s[1].text == "Ô oui!", tei_pclv9.text.body.div[1].p[4].s[1].text
assert tei_pclv9.text.body.div[1].p[4].s[2].text == "Ò aquesta tanben.", tei_pclv9.text.body.div[1].p[4].s[2].text
assert tei_pclv9.text.body.div[2].__class__.__name__ == "div", tei_pclv9.text.body.div[2].__class__.__name__
assert tei_pclv9.text.body.div[2].text == None, tei_pclv9.text.body.div[2].text
assert tei_pclv9.text.body.div[2].head.seg == "Titre de la sous-partie 1", tei_pclv9.text.body.div[2].head.seg
assert tei_pclv9.text.body.div[2].p[0].text == None, tei_pclv9.text.body.div[2].p[0].text
assert tei_pclv9.text.body.div[2].p[0].s[0].text == "Maintenant testons les abbréviations comme F.T.P ou F.F.I. par exemple.", tei_pclv9.text.body.div[2].p[0].s[0].text
assert tei_pclv9.text.body.div[2].p[0].s[1].text == "Ou St.", tei_pclv9.text.body.div[2].p[0].s[1].text
assert tei_pclv9.text.body.div[2].p[0].s[2].text == "(St ?)", tei_pclv9.text.body.div[2].p[0].s[2].text
assert tei_pclv9.text.body.div[2].p[0].s[3].text == "Mr. et Ste Mme.", tei_pclv9.text.body.div[2].p[0].s[3].text
assert tei_pclv9.text.body.div[2].p[1].text == None, tei_pclv9.text.body.div[2].p[1].text
assert tei_pclv9.text.body.div[2].p[1].s[0].text == "Ainsi que les différentes ponctuations,  comme ; et encore : ainsi de suite...", tei_pclv9.text.body.div[2].p[1].s[0].text
assert tei_pclv9.text.body.div[2].p[1].s[1].text == "Voilà.", tei_pclv9.text.body.div[2].p[1].s[1].text
assert tei_pclv9.text.body.div[2].p[2].text == None, tei_pclv9.text.body.div[2].p[2].text
assert tei_pclv9.text.body.div[2].p[2].s[0].text == "Nous devons aussi tester les dialogues.", tei_pclv9.text.body.div[2].p[2].s[0].text
assert tei_pclv9.text.body.div[2].p[2].s[1].text == "Quelqu'un dit : - Que fait-on ?", tei_pclv9.text.body.div[2].p[2].s[1].text
assert tei_pclv9.text.body.div[2].p[2].s[2].text == "Doit-on continuer ?", tei_pclv9.text.body.div[2].p[2].s[2].text
assert tei_pclv9.text.body.div[2].p[3].text == None, tei_pclv9.text.body.div[2].p[3].text
assert tei_pclv9.text.body.div[2].p[3].s[0].text == "- Je ne sais pas...", tei_pclv9.text.body.div[2].p[3].s[0].text
assert tei_pclv9.text.body.div[2].p[3].s[1].text == "Qu'en penses-tu ?", tei_pclv9.text.body.div[2].p[3].s[1].text
assert tei_pclv9.text.body.div[3].__class__.__name__ == "div", tei_pclv9.text.body.div[3].__class__.__name__
assert tei_pclv9.text.body.div[3].text == None, tei_pclv9.text.body.div[3].text
assert tei_pclv9.text.body.div[3].head.seg == "POSTFACI", tei_pclv9.text.body.div[3].head.seg
assert tei_pclv9.text.body.div[3].p[0].text == None, tei_pclv9.text.body.div[3].p[0].text
assert tei_pclv9.text.body.div[3].p[0].s[0].text == "C'est la fin.", tei_pclv9.text.body.div[3].p[0].s[0].text
assert tei_pclv9.text.body.div[3].p[0].s[1].text == "On termine avec une signature.", tei_pclv9.text.body.div[3].p[0].s[1].text
assert tei_pclv9.text.body.div[3].p[1].text == None, tei_pclv9.text.body.div[3].p[1].text
assert tei_pclv9.text.body.div[3].p[1].s[0].text == "Aquí, uèi", tei_pclv9.text.body.div[3].p[1].s[0].text
assert tei_pclv9.text.body.div[3].p[1].s[1].text == "- F. L.", tei_pclv9.text.body.div[3].p[1].s[1].text
assert tei_pclv9.text.body.div[4].__class__.__name__ == "div", tei_pclv9.text.body.div[4].__class__.__name__
assert tei_pclv9.text.body.div[4].text == None, tei_pclv9.text.body.div[4].text
assert tei_pclv9.text.body.div[4].head.seg == "Titre du chapitre 1", tei_pclv9.text.body.div[4].head.seg
assert tei_pclv9.text.body.div[4].p[0].text == None, tei_pclv9.text.body.div[4].p[0].text
assert tei_pclv9.text.body.div[4].p[0].s[0].text == "Contenu de chapitre 1.", tei_pclv9.text.body.div[4].p[0].s[0].text
assert tei_pclv9.text.body.div[5].__class__.__name__ == "div", tei_pclv9.text.body.div[5].__class__.__name__
assert tei_pclv9.text.body.div[5].text == None, tei_pclv9.text.body.div[5].text
assert tei_pclv9.text.body.div[5].head.seg == "Titre de la sous-partie du chapitre 1", tei_pclv9.text.body.div[5].head.seg
assert tei_pclv9.text.body.div[5].p[0].text == None, tei_pclv9.text.body.div[5].p[0].text
assert tei_pclv9.text.body.div[5].p[0].s[0].text == "Sous-partie du chapitre 1.", tei_pclv9.text.body.div[5].p[0].s[0].text
assert tei_pclv9.text.body.div[6].__class__.__name__ == "div", tei_pclv9.text.body.div[6].__class__.__name__
assert tei_pclv9.text.body.div[6].text == None, tei_pclv9.text.body.div[6].text
assert tei_pclv9.text.body.div[6].head.seg == None, tei_pclv9.text.body.div[6].head.seg
assert tei_pclv9.text.body.div[6].p[0].text == None, tei_pclv9.text.body.div[6].p[0].text
assert tei_pclv9.text.body.div[6].p[0].s[0].text == "Encore une sous-partie.", tei_pclv9.text.body.div[6].p[0].s[0].text
assert tei_pclv9.text.body.div[7].__class__.__name__ == "div", tei_pclv9.text.body.div[7].__class__.__name__
assert tei_pclv9.text.body.div[7].text == None, tei_pclv9.text.body.div[7].text
assert tei_pclv9.text.body.div[7].head.seg == "Dernier chapitre", tei_pclv9.text.body.div[7].head.seg
assert tei_pclv9.text.body.div[7].p[0].text == None, tei_pclv9.text.body.div[7].p[0].text
assert tei_pclv9.text.body.div[7].p[0].s[0].text == "Contenu du dernier chapitre.", tei_pclv9.text.body.div[7].p[0].s[0].text
assert tei_pclv9.text.body.div[8].__class__.__name__ == "div", tei_pclv9.text.body.div[8].__class__.__name__
assert tei_pclv9.text.body.div[8].head.seg == "Epilòg", tei_pclv9.text.body.div[8].head.seg
assert tei_pclv9.text.body.div[8].text == None, tei_pclv9.text.body.div[8].text
assert tei_pclv9.text.body.div[9].__class__.__name__ == "div", tei_pclv9.text.body.div[9].__class__.__name__
assert tei_pclv9.text.body.div[9].head.seg == "TITOL", tei_pclv9.text.body.div[9].head.seg
assert tei_pclv9.text.body.div[9].text == None, tei_pclv9.text.body.div[9].text
assert tei_pclv9.text.body.div[9].p[0].text == None, tei_pclv9.text.body.div[9].p[0].text
assert tei_pclv9.text.body.div[9].p[0].s[0].text == "\"Aquì lo tèxte.", tei_pclv9.text.body.div[9].p[0].s[0].text
assert tei_pclv9.text.body.div[9].p[1].text == None, tei_pclv9.text.body.div[9].p[1].text
assert tei_pclv9.text.body.div[9].p[1].s[0].text == "- Va plan !\"", tei_pclv9.text.body.div[9].p[1].s[0].text
assert tei_pclv9.text.body.div[9].p[2].text == None, tei_pclv9.text.body.div[9].p[2].text
assert tei_pclv9.text.body.div[9].p[2].s[0].text == "E aquì tanben.", tei_pclv9.text.body.div[9].p[2].s[0].text
assert tei_pclv9.text.body.div[9].p[3].text == None, tei_pclv9.text.body.div[9].p[3].text
assert tei_pclv9.text.body.div[9].p[3].s[0].text == "\"Ici un texte en français\".", tei_pclv9.text.body.div[9].p[3].s[0].text
assert tei_pclv9.text.body.div[9].note == None, tei_pclv9.text.body.div[9].note
assert tei_pclv9.text.body.div[9].p[4].text == None, tei_pclv9.text.body.div[9].p[4].text
assert tei_pclv9.text.body.div[9].p[4].s[0].text == "Primièra frasa", tei_pclv9.text.body.div[9].p[4].s[0].text
assert tei_pclv9.text.body.div[9].p[4].s[1].text == "Allez !", tei_pclv9.text.body.div[9].p[4].s[1].text

## Write it to ParCoLab v9 XML
pyteilib.tei_write(tei_pclv9, OUTPUT_DIR + "example1_pcl_v9.xml", xml_type='PCLv9')
assert tei_pclv9.get_filename() == OUTPUT_DIR + "example1_pcl_v9.xml", tei_pclv9.get_filename()

## Export metadata to v9 format
pyteilib.export_header(tei_pclv9, OUTPUT_DIR + "example1_metadata_v9.csv")

### Keep highlighted text

## Read BaTelÒc XML
tei_bto_hi = pyteilib.tei_read(INPUT_DIR + "example1_bto.xml", xml_type='BTO', keep_highlighted=True)

# Test text body
assert tei_bto_hi.text.body.div[1].p[2].text == "E de partidas <hi rend=\"I\">en italicas</hi>. De questions? O encara: d'exclamacions! Plan.", tei_bto_hi.text.body.div[1].p[2].text

# Test text back
assert tei_bto_hi.text.back.epilogue.div[0].head.text == "<hi rend=\"G\">Epilòg</hi>", tei_bto_hi.text.back.epilogue.div[0].head.text
assert tei_bto_hi.text.back.epilogue.div[1].p[2].text == "E <hi rend=\"I\">aquì</hi> tanben.", tei_bto_hi.text.back.epilogue.div[1].p[2].text
assert tei_bto_hi.text.back.epilogue.div[1].p[3].text == "\"Ici un texte en <hi rend=\"I\">français</hi>\".", tei_bto_hi.text.back.epilogue.div[1].p[3].text
assert tei_bto_hi.text.back.epilogue.div[1].p[4].s[2].text == "<hi rend=\"I\">Allez !</hi>", tei_bto_hi.text.back.epilogue.div[1].p[4].s[2].text
assert tei_bto_hi.text.back.div[0].note.div[0].head.text == "<hi rend=\"G\">NOTES DE L'AUTEUR</hi>", tei_bto_hi.text.back.div[0].note.div[0].head.text
assert tei_bto_hi.text.back.div[0].note.div[1].p[0].text == "Ici des notes en <hi rend=\"I\">français</hi>", tei_bto_hi.text.back.div[0].note.div[1].p[0].text

## Simply export it to BaTelÒc XML
pyteilib.tei_write(tei_bto_hi, OUTPUT_DIR + "example1_bto_hi.xml", xml_type='BTO')

## Transform it to ParCoLab v8 XML
tei_pclv8_hi = pyteilib.transform(tei_bto_hi, from_type='BTO', to_type='PCLv8')

# Test text body
assert tei_pclv8_hi.text.body.div[1].p[2].s[0].text == "E de partidas <hi rend=\"I\">en italicas</hi>.", tei_pclv8_hi.text.body.div[1].p[2].s[0].text
assert tei_pclv8_hi.text.body.div[8].head.seg == "<hi rend=\"G\">Epilòg</hi>", tei_pclv8_hi.text.body.div[8].head.seg
assert tei_pclv8_hi.text.body.div[9].p[2].s[0].text == "E <hi rend=\"I\">aquì</hi> tanben.", tei_pclv8_hi.text.body.div[9].p[2].s[0].text
assert tei_pclv8_hi.text.body.div[9].p[3].s[0].text == "\"Ici un texte en <hi rend=\"I\">français</hi>\".", tei_pclv8_hi.text.body.div[9].p[3].s[0].text
assert tei_pclv8_hi.text.body.div[9].p[4].s[1].text == "<hi rend=\"I\">Allez !</hi>", tei_pclv8_hi.text.body.div[9].p[4].s[1].text

## Write it to ParCoLab v8 XML
pyteilib.tei_write(tei_pclv8_hi, OUTPUT_DIR + "example1_pcl_v8_hi.xml", xml_type='PCLv8')

## Transform it to ParCoLab v9 XML
tei_pclv9_hi = pyteilib.transform(tei_bto_hi, from_type='BTO', to_type='PCLv9')

# Test text body
assert tei_pclv9_hi.text.body.div[1].p[2].s[0].text == "E de partidas <hi rend=\"I\">en italicas</hi>.", tei_pclv9_hi.text.body.div[1].p[2].s[0].text
assert tei_pclv9_hi.text.body.div[8].head.seg == "<hi rend=\"G\">Epilòg</hi>", tei_pclv9_hi.text.body.div[8].head.seg
assert tei_pclv9_hi.text.body.div[9].p[2].s[0].text == "E <hi rend=\"I\">aquì</hi> tanben.", tei_pclv9_hi.text.body.div[9].p[2].s[0].text
assert tei_pclv9_hi.text.body.div[9].p[3].s[0].text == "\"Ici un texte en <hi rend=\"I\">français</hi>\".", tei_pclv9_hi.text.body.div[9].p[3].s[0].text
assert tei_pclv9_hi.text.body.div[9].p[4].s[1].text == "<hi rend=\"I\">Allez !</hi>", tei_pclv9_hi.text.body.div[9].p[4].s[1].text

## Write it to ParCoLab v9 XML
pyteilib.tei_write(tei_pclv9_hi, OUTPUT_DIR + "example1_pcl_v9_hi.xml", xml_type='PCLv9')

## Release created objects
del tei_bto, tei_pclv8, tei_pclv9

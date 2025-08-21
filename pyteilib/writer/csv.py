#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package writer
"""

import csv, os

def export_header(tei, filename):
    """! @brief Write a CSV metadata file.
    @param tei The TEI instance to export as CSV.
    @param filename The name of the CSV file to write with full path, for instance 'user/output/example_metadata.csv'.
    """
    print("Export ParCoLab " + tei.__class__.__name__[-2:] + " metadata to CSV file " + filename)
    if tei.__class__.__name__ == "PCLv8" or tei.__class__.__name__ == "PCLv9":
        csv_file = open(filename, 'w', newline='')
        if tei.__class__.__name__ == "PCLv8":
            fieldnames = ['file', 'id', 'title', 'subtitle', 'author-firstname1', 'author-lastname1', 'author-firstname2', 'author-lastname2', 'author-firstname3', 'author-lastname3', 'translator-firstname1', 'translator-lastname1', 'translator-firstname2', 'translator-lastname2', 'translator-firstname3', 'translator-lastname3', 'transcriber-firstname1', 'transcriber-lastname1', 'collection', 'resp_collection-firstname1', 'resp_collection-lastname1', 'resp_collection-firstname2', 'resp_collection-lastname2', 'resp_collection-firstname3', 'resp_collection-lastname3', 'words', 'publisher', 'pubPlace', 'date', 'licence', 'note', 'edition', 'sourceDesc', 'projectDesc', 'language', 'language_ori', 'dialect', 'creationDate', 'derivation', 'domain1', 'domain2', 'domain3', 'genre1', 'genre2', 'genre3', 'textForm']
        elif tei.__class__.__name__ == "PCLv9":
            fieldnames = ['file', 'id', 'title', 'subtitle', 'author-firstname1', 'author-lastname1', 'author-birth1', 'author-death1', 'author-place1', 'author-firstname2', 'author-lastname2', 'author-birth2', 'author-death2', 'author-place2', 'author-firstname3', 'author-lastname3', 'author-birth3', 'author-death3', 'author-place3', 'translator-firstname1', 'translator-lastname1', 'translator-birth1', 'translator-death1', 'translator-firstname2', 'translator-lastname2', 'translator-birth2', 'translator-death2', 'translator-firstname3', 'translator-lastname3', 'translator-birth3', 'translator-death3', 'transcriber-firstname1', 'transcriber-lastname1', 'publisher_provider-name', 'publisher_provider-date', 'project_provider-name', 'teihdr_creator-name', 'teihdr_creator-date', 'teibdy_creator-name', 'teibdy_creator-date', 'collection', 'resp_collection-firstname1', 'resp_collection-lastname1', 'resp_collection-firstname2', 'resp_collection-lastname2', 'resp_collection-firstname3', 'resp_collection-lastname3', 'words', 'publisher', 'pubPlace', 'date', 'isbn', 'licence', 'note', 'edition', 'sourceDesc', 'projectDesc', 'language', 'language_ori', 'dialect', 'dialect_ori', 'script', 'script_ori', 'creationDate', 'derivation', 'domain1', 'domain2', 'domain3', 'genre1', 'genre2', 'genre3', 'textForm', 'predefined_corpora', 'contributor-date1', 'contributor-name1']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write columns name
        writer.writeheader()
        ## Compute row values
        file = os.path.basename(tei.get_filename())
        id = tei.id
        title = tei.teiHeader.fileDesc.titleStmt.title
        subtitle = tei.teiHeader.fileDesc.titleStmt.subtitle
        author_firstname1 = tei.teiHeader.fileDesc.titleStmt.author[0].name.forename
        author_lastname1 = tei.teiHeader.fileDesc.titleStmt.author[0].name.surname
        author_firstname2 = tei.teiHeader.fileDesc.titleStmt.author[1].name.forename
        author_lastname2 = tei.teiHeader.fileDesc.titleStmt.author[1].name.surname
        author_firstname3 = tei.teiHeader.fileDesc.titleStmt.author[2].name.forename
        author_lastname3 = tei.teiHeader.fileDesc.titleStmt.author[2].name.surname
        translator_firstname1 = tei.teiHeader.fileDesc.titleStmt.respStmt[0].name.forename
        translator_lastname1 = tei.teiHeader.fileDesc.titleStmt.respStmt[0].name.surname
        translator_firstname2 = tei.teiHeader.fileDesc.titleStmt.respStmt[1].name.forename
        translator_lastname2 = tei.teiHeader.fileDesc.titleStmt.respStmt[1].name.surname
        translator_firstname3 = tei.teiHeader.fileDesc.titleStmt.respStmt[2].name.forename
        translator_lastname3 = tei.teiHeader.fileDesc.titleStmt.respStmt[2].name.surname
        transcriber_firstname1 = tei.teiHeader.fileDesc.titleStmt.respStmt[3].name.forename
        transcriber_lastname1  = tei.teiHeader.fileDesc.titleStmt.respStmt[3].name.surname
        collection = tei.teiHeader.fileDesc.titleStmt.collectionStmt.collection
        resp_collection_firstname1 = tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.forename
        resp_collection_lastname1 = tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[0].name.surname
        resp_collection_firstname2 = tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.forename
        resp_collection_lastname2 = tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[1].name.surname
        resp_collection_firstname3 = tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.forename
        resp_collection_lastname3 = tei.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt[2].name.surname
        words = tei.teiHeader.fileDesc.extent.measure.quantity
        publisher = tei.teiHeader.fileDesc.publicationStmt.publisher
        pubPlace = tei.teiHeader.fileDesc.publicationStmt.pubPlace
        date = tei.teiHeader.fileDesc.publicationStmt.date
        licence = tei.teiHeader.fileDesc.publicationStmt.availability.licence
        note = ''
        for n in tei.teiHeader.fileDesc.notesStmt.note:
            note += n + '\n'
        note = note.rstrip('\n')
        edition = tei.teiHeader.fileDesc.editionStmt.edition
        sourceDesc = tei.teiHeader.fileDesc.sourceDesc.text
        projectDesc = ''
        for p in tei.teiHeader.encodingDesc.projectDesc.p:
            projectDesc += p.text + '\n'
        projectDesc = projectDesc.rstrip('\n')
        language = tei.teiHeader.profileDesc.langUsage.language.ident
        language_ori = tei.teiHeader.profileDesc.langUsage.language.langOri
        dialect = None
        if tei.__class__.__name__ == "PCLv8":
            if len(tei.teiHeader.profileDesc.category.catDesc) > 0:
                dialect = tei.teiHeader.profileDesc.category.catDesc[0].text
        elif tei.__class__.__name__ == "PCLv9":
            dialect = tei.teiHeader.profileDesc.langUsage.language.variant
        creationDate = tei.teiHeader.profileDesc.creation.date
        derivation = tei.teiHeader.profileDesc.textDesc.derivation.type
        domain1 = tei.teiHeader.profileDesc.textDesc.domain[0].type
        domain2 = tei.teiHeader.profileDesc.textDesc.domain[1].type
        domain3 = tei.teiHeader.profileDesc.textDesc.domain[2].type
        genre1 = tei.teiHeader.profileDesc.textDesc.genre[0].type
        genre2 = tei.teiHeader.profileDesc.textDesc.genre[1].type
        genre3 = tei.teiHeader.profileDesc.textDesc.genre[2].type
        textForm = tei.teiHeader.profileDesc.textDesc.textForm.type
        csv_dict = {'file': file, 'id': id, 'title':title, 'subtitle':subtitle, 'author-firstname1':author_firstname1, 'author-lastname1':author_lastname1, 'author-firstname2':author_firstname2, 'author-lastname2':author_lastname2, 'author-firstname3':author_firstname3, 'author-lastname3':author_lastname3, 'translator-firstname1':translator_firstname1, 'translator-lastname1':translator_lastname1, 'translator-firstname2':translator_firstname2, 'translator-lastname2':translator_lastname2, 'translator-firstname3':translator_firstname3, 'translator-lastname3':translator_lastname3, 'transcriber-firstname1':transcriber_firstname1, 'transcriber-lastname1':transcriber_lastname1, 'collection':collection, 'resp_collection-firstname1':resp_collection_firstname1, 'resp_collection-lastname1':resp_collection_lastname1, 'resp_collection-firstname2':resp_collection_firstname2, 'resp_collection-lastname2':resp_collection_lastname2, 'resp_collection-firstname3':resp_collection_firstname3, 'resp_collection-lastname3':resp_collection_lastname3, 'words':words, 'publisher':publisher, 'pubPlace':pubPlace, 'date':date, 'licence':licence, 'note':note, 'edition':edition, 'sourceDesc':sourceDesc, 'projectDesc':projectDesc, 'language':language, 'language_ori':language_ori, 'dialect':dialect, 'creationDate':creationDate, 'derivation':derivation, 'domain1':domain1, 'domain2':domain2, 'domain3':domain3, 'genre1':genre1, 'genre2':genre2, 'genre3':genre3, 'textForm':textForm}
        if tei.__class__.__name__ == "PCLv8":
            writer.writerow(csv_dict)
        elif tei.__class__.__name__ == "PCLv9":
            ## Add row values for PCLv9
            author_birth1 = tei.teiHeader.fileDesc.titleStmt.author[0].birth
            author_death1 = tei.teiHeader.fileDesc.titleStmt.author[0].death
            author_place1 = tei.teiHeader.fileDesc.titleStmt.author[0].placeName
            author_birth2 = tei.teiHeader.fileDesc.titleStmt.author[1].birth
            author_death2 = tei.teiHeader.fileDesc.titleStmt.author[1].death
            author_place2 = tei.teiHeader.fileDesc.titleStmt.author[1].placeName
            author_birth3 = tei.teiHeader.fileDesc.titleStmt.author[2].birth
            author_death3 = tei.teiHeader.fileDesc.titleStmt.author[2].death
            author_place3 = tei.teiHeader.fileDesc.titleStmt.author[2].placeName
            translator_birth1 = tei.teiHeader.fileDesc.titleStmt.respStmt[0].birth
            translator_death1 = tei.teiHeader.fileDesc.titleStmt.respStmt[0].death
            translator_birth2 = tei.teiHeader.fileDesc.titleStmt.respStmt[1].birth
            translator_death2 = tei.teiHeader.fileDesc.titleStmt.respStmt[1].death
            translator_birth3 = tei.teiHeader.fileDesc.titleStmt.respStmt[2].birth
            translator_death3 = tei.teiHeader.fileDesc.titleStmt.respStmt[2].death
            publisher_provider_name = tei.teiHeader.fileDesc.titleStmt.respStmt[4].name
            publisher_provider_date = tei.teiHeader.fileDesc.titleStmt.respStmt[4].date
            project_provider_name = tei.teiHeader.fileDesc.titleStmt.respStmt[5].name
            teihdr_creator_name = tei.teiHeader.fileDesc.titleStmt.respStmt[6].name
            teihdr_creator_date = tei.teiHeader.fileDesc.titleStmt.respStmt[6].date
            teibdy_creator_name = tei.teiHeader.fileDesc.titleStmt.respStmt[7].name
            teibdy_creator_date = tei.teiHeader.fileDesc.titleStmt.respStmt[7].date
            isbn = tei.teiHeader.fileDesc.publicationStmt.idno.text
            dialect_ori = tei.teiHeader.profileDesc.langUsage.language.variantOri
            script = tei.teiHeader.profileDesc.langUsage.language.script
            script_ori = tei.teiHeader.profileDesc.langUsage.language.scriptOri
            predefined_corpora = ''
            for corpus in tei.teiHeader.profileDesc.textClass.keywords.term:
                predefined_corpora += corpus.text + ' ; '
            predefined_corpora = predefined_corpora.rstrip(' ; ')
            contributor_date1 = tei.teiHeader.revisionDesc.listChange.change[0].when
            contributor_name1 = tei.teiHeader.revisionDesc.listChange.change[0].who
            csv_dict.update({'author-birth1':author_birth1, 'author-death1':author_death1, 'author-place1':author_place1, 'author-birth2':author_birth2, 'author-death2':author_death2, 'author-place2':author_place2, 'author-birth3':author_birth3, 'author-death3':author_death3, 'author-place3':author_place3, 'translator-birth1':translator_birth1, 'translator-death1':translator_death1, 'translator-birth2':translator_birth2, 'translator-death2':translator_death2, 'translator-birth3':translator_birth3, 'translator-death3':translator_death3, 'publisher_provider-name':publisher_provider_name, 'publisher_provider-date':publisher_provider_date, 'project_provider-name':project_provider_name, 'teihdr_creator-name':teihdr_creator_name, 'teihdr_creator-date':teihdr_creator_date, 'teibdy_creator-name':teibdy_creator_name, 'teibdy_creator-date':teibdy_creator_date, 'isbn':isbn, 'dialect_ori':dialect_ori, 'script':script, 'script_ori':script_ori, 'predefined_corpora':predefined_corpora, 'contributor-date1':contributor_date1, 'contributor-name1':contributor_name1})
            writer.writerow(csv_dict)
        csv_file.close()
    else:
        print("Can only export ParCoLab metadata")

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package tei
"""

from tei_p5 import TEI, author, respStmt, edition, distributor, seriesStmt, biblStruct, author, title, idno, classDecl, category, catDesc, front, back

### TEI BaTelÒc

class BTO(TEI):
    """! TEI BaTelÒc class.
    """
    def __init__(self, id='0'):
        """! @brief Constructor.
        TEI instance.
        @param id IDentifier. If not provided, default value is '0'.
        @return A TEI instance.
        """
        TEI.__init__(self, id)
        # TEI header
        self.teiHeader.fileDesc.titleStmt.author = [author()]
        self.teiHeader.fileDesc.titleStmt.respStmt = [respStmt(resp='balhaire fichièr sorga'), respStmt(resp='portaire fichièr sorga'), respStmt(resp='donadas pel header'), respStmt(resp='pretractament e balisatge del tèxte segon la TEI P5')]
        self.teiHeader.fileDesc.editionStmt.edition = edition()
        self.teiHeader.fileDesc.publicationStmt.distributor = distributor()
        self.teiHeader.fileDesc.seriesStmt = seriesStmt()
        self.teiHeader.fileDesc.sourceDesc.biblStruct = biblStruct()
        self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author = [author(id='traducteur'), author(id='auteurOriginal')]
        self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title = [title(), title(type='parallel')]
        self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno = [idno(type='ISBN'), idno(type='numero edition')]
        self.teiHeader.encodingDesc.classDecl = classDecl()
        self.teiHeader.encodingDesc.classDecl.taxonomy.category = [category(type='dialecte'), category(type='graphie'), category(type='genre'), category(type='corpus')]
        self.teiHeader.encodingDesc.classDecl.taxonomy.category[0].catDesc = [catDesc()]
        self.teiHeader.encodingDesc.classDecl.taxonomy.category[1].catDesc = [catDesc()]
        self.teiHeader.encodingDesc.classDecl.taxonomy.category[2].catDesc = [catDesc(type='principal'), catDesc(type='sub')]
        # TEI text
        self.text.front = front()
        self.text.back = back()

    def __del__(self):
        """! @brief Destructor.
        Release all created instances.
        """
        del self.text.back
        del self.text.front
        if self.teiHeader.encodingDesc.classDecl.taxonomy.category is not None:
            for category in self.teiHeader.encodingDesc.classDecl.taxonomy.category:
                if category.catDesc is not None:
                    for catDesc in category.catDesc:
                        del catDesc
                del category
        del self.teiHeader.encodingDesc.classDecl
        if self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno is not None:
            for idno in self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.imprint.idno:
                del idno
        if self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title is not None:
            for title in self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.title:
                del title
        if self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author is not None:
            for author in self.teiHeader.fileDesc.sourceDesc.biblStruct.monogr.author:
                del author
        del self.teiHeader.fileDesc.sourceDesc.biblStruct
        del self.teiHeader.fileDesc.seriesStmt
        del self.teiHeader.fileDesc.publicationStmt.distributor
        del self.teiHeader.fileDesc.editionStmt.edition
        if self.teiHeader.fileDesc.titleStmt.respStmt is not None:
            for respStmt in self.teiHeader.fileDesc.titleStmt.respStmt:
                del respStmt
        if self.teiHeader.fileDesc.titleStmt.author is not None:
            for author in self.teiHeader.fileDesc.titleStmt.author:
                del author
        TEI.__del__(self)

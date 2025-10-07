#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package tei
"""

from tei_p5 import TEI, author, name, respStmt, collectionStmt, extent, licence, notesStmt, category, textDesc, domain, genre

### TEI ParCoLab v8

class PCLv8(TEI):
    """! TEI ParCoLab v8 class.
    """
    def __init__(self, id='0'):
        """! @brief Constructor.
        TEI instance.
        @param id IDentifier. If not provided, default value is '0'.
        @return A TEI instance.
        """
        TEI.__init__(self, id)
        self.teiHeader.fileDesc.titleStmt.author = [author(), author(), author()]
        for author_inst in self.teiHeader.fileDesc.titleStmt.author:
            author_inst.name = name()
        self.teiHeader.fileDesc.titleStmt.respStmt = [respStmt(resp='translator'), respStmt(resp='translator'), respStmt(resp='translator'), respStmt(resp='transcriber')]
        for resp_stmt in self.teiHeader.fileDesc.titleStmt.respStmt:
            resp_stmt.name = name()
        self.teiHeader.fileDesc.titleStmt.collectionStmt = collectionStmt()
        self.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt = [respStmt(resp='resp_collection'), respStmt(resp='resp_collection'), respStmt(resp='resp_collection')]
        for resp_stmt in self.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt:
            resp_stmt.name = name()
        self.teiHeader.fileDesc.extent = extent()
        self.teiHeader.fileDesc.publicationStmt.availability.licence = licence()
        self.teiHeader.fileDesc.notesStmt = notesStmt()
        self.teiHeader.profileDesc.category = category()
        self.teiHeader.profileDesc.category.type = "dialecte"
        self.teiHeader.profileDesc.textDesc = textDesc()
        self.teiHeader.profileDesc.textDesc.domain = [domain(), domain(), domain()]
        self.teiHeader.profileDesc.textDesc.genre = [genre(), genre(), genre(), genre()]

    def __del__(self):
        """! @brief Destructor.
        Release all created instances.
        """
        if self.teiHeader.profileDesc.textDesc.genre is not None:
            for genre in self.teiHeader.profileDesc.textDesc.genre:
                del genre
        if self.teiHeader.profileDesc.textDesc.domain is not None:
            for domain in self.teiHeader.profileDesc.textDesc.domain:
                del domain
        del self.teiHeader.profileDesc.textDesc
        del self.teiHeader.profileDesc.category
        del self.teiHeader.fileDesc.notesStmt
        del self.teiHeader.fileDesc.publicationStmt.availability.licence
        del self.teiHeader.fileDesc.extent
        if self.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt is not None:
            for respStmt in self.teiHeader.fileDesc.titleStmt.collectionStmt.respStmt:
                if respStmt.name is not None:
                    del respStmt.name
                del respStmt
        del self.teiHeader.fileDesc.titleStmt.collectionStmt
        if self.teiHeader.fileDesc.titleStmt.respStmt is not None:
            for respStmt in self.teiHeader.fileDesc.titleStmt.respStmt:
                if respStmt.name is not None:
                    del respStmt.name
                del respStmt
        if self.teiHeader.fileDesc.titleStmt.author is not None:
            for author in self.teiHeader.fileDesc.titleStmt.author:
                if author.name is not None:
                    del author.name
                del author
        TEI.__del__(self)

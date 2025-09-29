#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package tei
"""

### fileDesc

class name():
    """! TEI header name class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(name, proper noun) contains a proper noun or noun phrase" (tei-c.org).
        @return A TEI header name instance.
        """
        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address binaryObject cb choice cit corr date del distinct ellipsis email emph expan foreign gap gb gloss graphic hi index lb measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled term time title unclear unit / dictionaries: lang oRef pRef / figures: figure formula notatedMusic / gaiji: g / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef specDesc specList tag val / textcrit: app witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data" (tei-c.org)
        # "(forename) contains a forename, given or baptismal name. May contain character data" (tei-c.org)
        self.forename = None
        # "(surname) contains a family (inherited) name, as opposed to a given, baptismal, or nick name. May contain character data" (tei-c.org)
        self.surname = None

class author():
    """! TEI header author class.
    """
    def __init__(self, id=None, text=None):
        """! @brief Constructor.
        "(author) in a bibliographic reference, contains the name(s) of an author, personal or corporate, of a work; for example in the same form as that provided by a recognized bibliographic name authority" (tei-c.org).
        @param id "att.global > xml:id (identifier) provides a unique identifier for the element bearing the attribute" (tei-c.org).
        @param text Contents.
        @return A TEI header author instance.
        """
        # "att.global > xml:id (identifier) provides a unique identifier for the element bearing the attribute." (tei-c.org)
        self.id = id # used only in BTO sourceDesc / biblStruct / monogr

        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address binaryObject cb choice cit corr date del distinct ellipsis email emph expan foreign gap gb gloss graphic hi index lb measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled term time title unclear unit / dictionaries: lang oRef pRef / figures: figure formula notatedMusic / gaiji: g / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef specDesc specList tag val / textcrit: app witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data" (tei-c.org)
        self.text = text # used only in BTO fileDesc / titleStmt
        # "(name, proper noun) contains a proper noun or noun phrase." (tei-c.org)
        self.name = None # used only in PCL fileDesc / titleStmt
        # "(forename) contains a forename, given or baptismal name." (tei-c.org)
        self.forename = None # used only in BTO fileDesc / sourceDesc / biblStruct / monogr
        # "(place name) contains an absolute or relative place name." (tei-c.org)
        self.placeName = None # used only in PCLv9 fileDesc / titleStmt
        # "(surname) contains a family (inherited) name, as opposed to a given, baptismal, or nick name." (tei-c.org)
        self.surname = None # used only in BTO fileDesc / sourceDesc / biblStruct / monogr

        ## Not totally TEI-compliant: should be contained by <person role="author"/>
        # "(birth) contains information about a person's birth, such as its date and place." (tei-c.org)
        self.birth = None # used only in PCLv9 fileDesc / titleStmt
        # "(death) contains information about a person's death, such as its date and place." (tei-c.org)
        self.death = None # used only in PCLv9 fileDesc / titleStmt

        ## Not TEI-compliant
        self.datebirth = None # used only in BTO fileDesc / sourceDesc / biblStruct / monogr
        self.datedead = None # used only in BTO fileDesc / sourceDesc / biblStruct / monogr

class respStmt():
    """! TEI header responsible statement class.
    """
    def __init__(self, resp=None):
        """! @brief Constructor.
        "(statement of responsibility) supplies a statement of responsibility for the intellectual content of a text, edition, recording, or series, where the specialized elements for authors, editors, etc. do not suffice or do not apply. May also be used to encode information about individuals or organizations which have played a role in the production or distribution of a bibliographic work" (tei-c.org).
        @param resp "(responsibility) contains a phrase describing the nature of a person's intellectual responsibility, or an organization's role in the production or distribution of a work" (tei-c.org).
        @return A TEI header responsible statement instance.
        """
        ## May contain core: name note resp / namesdates: orgName persName
        # "(responsibility) contains a phrase describing the nature of a person's intellectual responsibility, or an organization's role in the production or distribution of a work." (tei-c.org)
        self.resp = resp
        # "(name, proper noun) contains a proper noun or noun phrase." (tei-c.org)
        self.name = None

        ## Not TEI-compliant
        self.date = None # only used in PCLv9
        self.birth = None # only used in PCLv9
        self.death = None # only used in PCLv9

# Not TEI-compliant, used only in PCL
class collectionStmt():
    def __init__(self):
        self.collection = None
        self.respStmt = []
    def __del__(self):
        for respStmt in self.respStmt:
            #if respStmt.name is not None:
                #del respStmt.name
            del respStmt

class titleStmt():
    """! TEI header file description / title statement class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(title statement) groups information about the title of a work and those responsible for its content" (tei-c.org).
        @return A TEI header file description / title statement instance.
        """
        # "(title) contains a title for any kind of work." (tei-c.org)
        self.title = ""
        # Not TEI-compliant
        self.subtitle = None # used only in PCL
        # "(author) in a bibliographic reference, contains the name(s) of an author, personal or corporate, of a work; for example in the same form as that provided by a recognized bibliographic name authority." (tei-c.org)
        self.author = []
        # "(editor) contains a secondary statement of responsibility for a bibliographic item, for example the name of an individual, institution or organization, (or of several such) acting as editor, compiler, translator, etc." (tei-c.org)
        self.editor = None # for BTO
        # "(sponsor) specifies the name of a sponsoring organization or institution." (tei-c.org)
        #self.sponsor = None # not used
        # "(funding body) specifies the name of an individual, institution, or organization responsible for the funding of a project or text." (tei-c.org)
        #self.funder = None # not used
        # "(principal researcher) supplies the name of the principal researcher responsible for the creation of an electronic text." (tei-c.org)
        self.principal = None
        # OPTIONAL "(statement of responsibility) supplies a statement of responsibility for the intellectual content of a text, edition, recording, or series, where the specialized elements for authors, editors, etc. do not suffice or do not apply. May also be used to encode information about individuals or organizations which have played a role in the production or distribution of a bibliographic work." (tei-c.org)
        self.respStmt = []

        ## Not TEI-compliant
        self.collectionStmt = None # used only in PCL

    def __del__(self):
        """! @brief Destructor.
        Release auhtors and responsible statements instances.
        """
        for author in self.author:
            del author
        for respStmt in self.respStmt:
            del respStmt

class edition():
    """! TEI header file description / edition statement / edition class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(edition) describes the particularities of one edition of a text" (tei-c.org).
        @param text Contents.
        @return A TEI header file description / edition statement / edition instance.
        """
        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address binaryObject cb choice cit corr date del distinct ellipsis email emph expan foreign gap gb gloss graphic hi index lb measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled term time title unclear unit / dictionaries: lang oRef pRef / figures: figure formula notatedMusic / gaiji: g / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef specDesc specList tag val / textcrit: app witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme" (tei-c.org)
        # "character data" (tei-c.org)
        self.text = None
        # "(date) contains a date in any format. May contain character data" (tei-c.org)
        self.date = None

class editionStmt():
    """! TEI header file description / edition statement class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(edition statement) groups information relating to one edition of a text" (tei-c.org).
        @return A TEI header file description / edition statement instance.
        """
        ## "May contain core: author editor meeting p respStmt / header: edition funder principal sponsor / linking: ab" (tei-c.org)
        # "(statement of responsibility) supplies a statement of responsibility for the intellectual content of a text, edition, recording, or series, where the specialized elements for authors, editors, etc. do not suffice or do not apply. May also be used to encode information about individuals or organizations which have played a role in the production or distribution of a bibliographic work." (tei-c.org)
        self.respStmt = respStmt()
        # "(edition) describes the particularities of one edition of a text." (tei-c.org)
        self.edition = edition()

    def __del__(self):
        """! @brief Destructor.
        Release responsible statement instance.
        """
        del self.respStmt
        #del self.edition

class measure():
    """! TEI header file description / extent / measure class.
    """
    def __init__(self, unit="words", quantity=0):
        """! @brief Constructor.
        "(measure) contains a word or phrase referring to some quantity of an object or commodity, usually comprising a number, a unit, and a commodity name" (tei-c.org).
        @param unit "(att.measurement > unit) indicates the units used for the measurement, usually using the standard symbol for the desired units". If not provided, default value is 'words' (tei-c.org).
        @param quantity "(att.measurement > quantity) specifies the number of the specified units that comprise the measurement". If not provided, default value is 0 (tei-c.org).
        @return A TEI header file description / extent / measure instance.
        """
        ## "Attributes" (tei-c.org)
        # "(att.measurement > unit) indicates the units used for the measurement, usually using the standard symbol for the desired units. Suggested values include: m / kg / s / Hz / Pa / Ω / L / t / ha / Å / mL / cm / dB / kbit / Kibit / kB / KiB / MB / MiB" (tei-c.org)
        self.unit = unit
        # "(att.measurement > quantity) specifies the number of the specified units that comprise the measurement" (tei-c.org)
        self.quantity = quantity
        # "(type) specifies the type of measurement in any convenient typology." (tei-c.org)
        #self.type = None # not used

        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address binaryObject cb choice cit corr date del distinct ellipsis email emph expan foreign gap gb gloss graphic hi index lb measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled term time title unclear unit / dictionaries: lang oRef pRef / figures: figure formula notatedMusic / gaiji: g / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef specDesc specList tag val / textcrit: app witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data" (tei-c.org)
        # "(unit) contains a symbol, a word or a phrase referring to a unit of measurement in any kind of formal or informal system. May contain character data" (tei-c.org)

class extent():
    """! TEI header file description / extent class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(extent) describes the approximate size of a text stored on some carrier medium or of some other object, digital or non-digital, specified in any convenient units" (tei-c.org).
        @return A TEI header file description / extent instance.
        """
        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address binaryObject cb choice cit corr date del distinct ellipsis email emph expan foreign gap gb gloss graphic hi index lb measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled term time title unclear unit / dictionaries: lang oRef pRef / figures: figure formula notatedMusic / gaiji: g / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef specDesc specList tag val / textcrit: app witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data" (tei-c.org)
        # "(measure) contains a word or phrase referring to some quantity of an object or commodity, usually comprising a number, a unit, and a commodity name." (tei-c.org)
        self.measure = measure() # used only in PCL

    def __del__(self):
        """! @brief Destructor.
        Release measure instance.
        """
        del self.measure

class distributor():
    """! TEI header file description / publication statement / distributor class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(distributor) supplies the name of a person or other agency responsible for the distribution of a text" (tei-c.org).
        @return A TEI header file description / publication statement / distributor instance.
        """
        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address binaryObject cb choice cit corr date del distinct ellipsis email emph expan foreign gap gb gloss graphic hi index lb measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled term time title unclear unit / dictionaries: lang oRef pRef / figures: figure formula notatedMusic / gaiji: g / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef specDesc specList tag val / textcrit: app witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data" (tei-c.org)
        # "(address) contains a postal address, for example of a publisher, an organization, or an individual." (tei-c.org)
        self.address = None
        # "(name, proper noun) contains a proper noun or noun phrase. Main contain character data" (tei-c.org)
        self.name = ""

class idno():
    """! TEI header file description / publication statement / idno class.
    """
    def __init__(self, type='ISBN', text=None):
        """! @brief Constructor.
        "(identifier) supplies any form of identifier used to identify some object, such as a bibliographic item, a person, a title, an organization, etc. in a standardized way" (tei-c.org).
        @param type "(type) categorizes the identifier, for example as an ISBN, Social Security number, etc" (tei-c.org). If not provided, default value is 'ISBN'.
        @param text Contents.
        @return A TEI header file description / publication statement / idno instance.
        """
        ## "Attributes" (tei-c.org)
        # "(type) categorizes the identifier, for example as an ISBN, Social Security number, etc. Suggested values include: 1] ISBN; 2] ISSN; 3] DOI; 4] URI; 5] VIAF; 6] ESTC; 7] OCLC" (tei-c.org).
        self.type = type

        ## "May contain gaiji: g / header: idno / character data" (tei-c.org)
        self.text = text

class licence():
    """! TEI header file description / publication statement / availability /licence class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(licence) contains information about a licence or other legal agreement applicable to the text" (tei-c.org).
        @param text Contents.
        @return A TEI header file description / publication statement / availability /licence instance.
        """
        # "character data" (tei-c.org)
        self.text = text
        # "(paragraph) marks paragraphs in prose." (tei-c.org)
        self.p = None

class availability():
    """! TEI header file description / publication statement / availability class.
    """
    def __init__(self, status=None, text=None):
        """! @brief Constructor.
        "(availability) supplies information about the availability of a text, for example any restrictions on its use or distribution, its copyright status, any licence applying to it, etc" (tei-c.org).
        @param status "(status) supplies a code identifying the current availability of the text" (tei-c.org).
        @param text Contents.
        @return A TEI header file description / publication statement / availability instance.
        """
        ## "Attributes" (tei-c.org)
        # "(status) supplies a code identifying the current availability of the text. Legal values are: free / unknown / restricted" (tei-c.org)
        self.status = status

        ## "May contain core: p / header: licence / linking: ab" (tei-c.org)
        # "(paragraph) marks paragraphs in prose." (tei-c.org)
        self.p = p(text) # used only in BTO
        # "(licence) contains information about a licence or other legal agreement applicable to the text." (tei-c.org)
        self.licence = None

class publicationStmt():
    """! TEI header file description / publication statement class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(publication statement) groups information concerning the publication or distribution of an electronic or other text" (tei-c.org).
        @return A TEI header file description / publication statement instance.
        """
        ## "May contain core: address date p ptr pubPlace publisher ref / header: authority availability distributor idno / linking: ab / tagdocs: listRef
        # "(publisher) provides the name of the organization responsible for the publication or distribution of a bibliographic item." (tei-c.org)
        self.publisher = None
        # "(distributor) supplies the name of a person or other agency responsible for the distribution of a text." (tei-c.org)
        self.distributor = None # used only in BTO
        # "(release authority) supplies the name of a person or other agency responsible for making a work available, other than a publisher or distributor." (tei-c.org)
        #self.authority = None # not used
        # "(publication place) contains the name of the place where a bibliographic item was published." (tei-c.org)
        self.pubPlace = None
        # "(address) contains a postal address, for example of a publisher, an organization, or an individual." (tei-c.org)
        self.address = None # used only in BTO
        # "(identifier) supplies any form of identifier used to identify some object, such as a bibliographic item, a person, a title, an organization, etc. in a standardized way." (tei-c.org)
        self.idno = None
        # "(availability) supplies information about the availability of a text, for example any restrictions on its use or distribution, its copyright status, any licence applying to it, etc." (tei-c.org)
        self.availability = availability()
        # "(date) contains a date in any format." (tei-c.org)
        self.date = None

    def __del__(self):
        """! @brief Destructor.
        Release availability instance.
        """
        del self.availability

class seriesStmt():
    """! TEI header file description / series statement class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(series statement) groups information about the series, if any, to which a publication belongs" (tei-c.org).
        @return A TEI header file description / series statement instance.
        """
        ## "May contain core: biblScope editor p respStmt title / header: idno / linking: ab" (tei-c.org)
        # "(title) contains a title for any kind of work." (tei-c.org)
        self.title = None
        # "(identifier) supplies any form of identifier used to identify some object, such as a bibliographic item, a person, a title, an organization, etc. in a standardized way." (tei-c.org)
        self.idno = None
        # "(statement of responsibility) supplies a statement of responsibility for the intellectual content of a text, edition, recording, or series, where the specialized elements for authors, editors, etc. do not suffice or do not apply. May also be used to encode information about individuals or organizations which have played a role in the production or distribution of a bibliographic work." (tei-c.org)
        self.respStmt = respStmt()

    def __del__(self):
        """! @brief Destructor.
        Release responsible statement instance.
        """
        del self.respStmt

class notesStmt():
    """! TEI header file description / notes statement class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(notes statement) collects together any notes providing information about a text additional to that recorded in other parts of the bibliographic description" (tei-c.org).
        @return A TEI header file description / notes statement instance.
        """
        ## "May contain core: note noteGrp relatedItem" (tei-c.org)
        # "(note) contains a note or annotation." (tei-c.org)
        self.note = []

    def __del__(self):
        """! @brief Destructor.
        Release notes instance.
        """
        for note in self.note:
            del note

class title():
    """! TEI (header file description / source description / bibliography structure / monography) or (text body division / epigraph / citation / bibliography) / title class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        "(title) contains a title for any kind of work" (tei-c.org).
        @param type "(type) classifies the title according to some convenient typology." (tei-c.org)
        @return A TEI (header file description / source description / bibliography structure / monography) or (text body division / epigraph / citation / bibliography) / title instance.
        """
        ## "Attributes" (tei-c.org)
        # "(type) classifies the title according to some convenient typology. Sample values include: main / sub / alt / short / desc" (tei-c.org)
        self.type = type
        # "(level) indicates the bibliographic level for a title, that is, whether it identifies an article, book, journal, series, or unpublished material. Legal values are: a / m / j / s / u" (tei-c.org)
        #self.level = None # not used

        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address bibl biblStruct binaryObject cb choice cit corr date del desc distinct ellipsis email emph expan foreign gap gb gloss graphic hi index l label lb lg list listBibl measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled stage term time title unclear unit / dictionaries: lang oRef pRef / drama: camera caption castList move sound tech view / figures: figure formula notatedMusic table / gaiji: g / header: biblFull idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material msDesc objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName listEvent listNym listObject listOrg listPerson listPlace listRelation location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att classSpec code constraintSpec dataSpec eg egXML elementSpec gi ident listRef macroSpec moduleSpec outputRendition specDesc specGrp specGrpRef specList tag val / textcrit: app listApp listWit witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data" (tei-c.org)
        self.text = text

class imprint():
    """! TEI header file description / source description / bibliography structure / monography / imprint class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(imprint) groups information relating to the publication or distribution of a bibliographic item" (tei-c.org).
        @return A TEI header file description / source description / bibliography structure / monography / imprint instance.
        """
        ## "May contain analysis: interp interpGrp span spanGrp / certainty: certainty precision respons / core: biblScope cb date ellipsis gap gb index lb milestone note noteGrp pb pubPlace publisher respStmt time / figures: figure notatedMusic / header: catRef classCode distributor / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp timeline / spoken: incident kinesic pause shift vocal writing / textcrit: app witDetail / transcr: addSpan damageSpan delSpan fw listTranspose metamark space substJoin" (tei-c.org)
        # "(date) contains a date in any format." (tei-c.org)
        self.date = None
        # "(publication place) contains the name of the place where a bibliographic item was published." (tei-c.org)
        self.pubplace = None
        # "(publisher) provides the name of the organization responsible for the publication or distribution of a bibliographic item." (tei-c.org)
        self.publisher = None

        ## Not TEI-compliant
        self.series = None
        self.idno = []

    def __del__(self):
        """! @brief Destructor.
        Release idnos instance.
        """
        for idno in self.idno:
            del idno

class monogr():
    """! TEI header file description / source description / bibliography structure / monography class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(monographic level) contains bibliographic elements describing an item (e.g. a book or journal) published as an independent item (i.e. as a separate physical object)" (tei-c.org).
        @return A TEI header file description / source description / bibliography structure / monography instance.
        """
        ## "May contain core: author biblScope editor imprint meeting note noteGrp ptr ref respStmt textLang title / header: authority availability edition extent funder idno sponsor / tagdocs: listRef" (tei-c.org)
        # "(author) in a bibliographic reference, contains the name(s) of an author, personal or corporate, of a work; for example in the same form as that provided by a recognized bibliographic name authority." (tei-c.org)
        self.author = []
        # "(imprint) groups information relating to the publication or distribution of a bibliographic item." (tei-c.org)
        self.imprint = imprint()
        # "(title) contains a title for any kind of work." (tei-c.org)
        self.title = []

    def __del__(self):
        """! @brief Destructor.
        Release authors, imprint and titles instances.
        """
        for author in self.author:
            del author
        del self.imprint
        for title in self.title:
            del title

class biblStruct():
    """! TEI header file description / source description / bibliography structure class.
    """
    def __init__(self, lang=None):
        """! @brief Constructor.
        "(structured bibliographic citation) contains a structured bibliographic citation, in which only bibliographic sub-elements appear and in a specified order" (tei-c.org).
        @param lang "att.global > xml:lang (language) indicates the language of the element content using a ‘tag’ generated according to BCP 47" (tei-c.org).
        @return A TEI header file description / source description / bibliography structure instance.
        """
        ## "Attributes" (tei-c.org)
        # "att.global > xml:lang (language) indicates the language of the element content using a ‘tag’ generated according to BCP 47." (tei-c.org)
        self.lang = None

        ## "May contain core: analytic citedRange monogr note noteGrp ptr ref relatedItem series / tagdocs: listRef" (tei-c.org)
        # "(monographic level) contains bibliographic elements describing an item (e.g. a book or journal) published as an independent item (i.e. as a separate physical object)." (tei-c.org)
        self.monogr = monogr()

    def __del__(self):
        """! @brief Destructor.
        Release monography instance.
        """
        del self.monogr

class sourceDesc():
    """! TEI header file description / source description class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(source description) describes the source(s) from which an electronic text was derived or generated, typically a bibliographic description in the case of a digitized text, or a phrase such as ‘born digital’ for a text which has no previous existence" (tei-c.org).
        @param text Contents.
        @return A TEI header file description / source description instance.
        """
        ## "May contain core: bibl biblStruct list listBibl p / figures: table / header: biblFull / linking: ab / msdescription: msDesc / namesdates: listEvent listNym listObject listOrg listPerson listPlace listRelation / spoken: recordingStmt scriptStmt / textcrit: listApp listWit" (tei-c.org)
        # "(bibliographic citation) contains a loosely-structured bibliographic citation of which the sub-components may or may not be explicitly tagged." (tei-c.org)
        self.bibl = None
        # "(fully-structured bibliographic citation) contains a fully-structured bibliographic citation, in which all components of the TEI file description are present." (tei-c.org)
        #self.biblFull = None # not used
        # "(structured bibliographic citation) contains a structured bibliographic citation, in which only bibliographic sub-elements appear and in a specified order." (tei-c.org)
        self.biblStruct = None # used only in BTO
        # "(citation list) contains a list of bibliographic citations of any kind." (tei-c.org)
        #self.listBibl = None # not used
        # "(paragraph) marks paragraphs in prose." (tei-c.org)
        self.p = None
        # "(manuscript description) contains a description of a single identifiable manuscript or other text-bearing object such as an early printed book." (tei-c.org)
        self.msDesc = None

        ## Not TEI-compliant
        self.text = text

class fileDesc():
    """! TEI header file description class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(file description) contains a full bibliographic description of an electronic file" (tei-c.org).
        @return A TEI header file description instance.
        """
        # MANDATORY "(title statement) groups information about the title of a work and those responsible for its content." (tei-c.org)
        self.titleStmt = titleStmt()
        # OPTIONAL BUT RECOMMENDED "(edition statement) groups information relating to one edition of a text." (tei-c.org)
        self.editionStmt = editionStmt()
        # OPTIONAL "(extent) describes the approximate size of a text stored on some carrier medium or of some other object, digital or non-digital, specified in any convenient units." (tei-c.org)
        self.extent = None
        # MANDATORY "(publication statement) groups information concerning the publication or distribution of an electronic or other text." (tei-c.org)
        self.publicationStmt = publicationStmt()
        # OPTIONAL "(series statement) groups information about the series, if any, to which a publication belongs." (tei-c.org)
        self.seriesStmt = None # used only in BTO
        # OPTIONAL "(notes statement) collects together any notes providing information about a text additional to that recorded in other parts of the bibliographic description." (tei-c.org)
        self.notesStmt = None # used only in PCL
        # MANDATORY "(source description) describes the source(s) from which an electronic text was derived or generated, typically a bibliographic description in the case of a digitized text, or a phrase such as ‘born digital’ for a text which has no previous existence." (tei-c.org)
        self.sourceDesc = sourceDesc()

    def __del__(self):
        """! @brief Destructor.
        Release title, edition, publication statements and source description instances.
        """
        del self.titleStmt
        del self.editionStmt
        del self.publicationStmt
        del self.sourceDesc

### encodingDesc

class projectDesc():
    """! TEI header encoding description / project description class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(project description) describes in detail the aim or purpose for which an electronic file was encoded, together with any other relevant information concerning the process by which it was assembled or collected." (tei-c.org)
        @return A TEI header encoding description / project description instance.
        """
        ## "May contain core: p / linking: ab" (tei-c.org)
        # "(paragraph) marks paragraphs in prose." (tei-c.org)
        self.p = []

    def __del__(self):
        """! @brief Destructor.
        Release paragraphs instance.
        """
        for p in self.p:
            del p

class catDesc():
    """! TEI header encoding description / class declaration / taxonomy / category / category description class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        "(category description) describes some category within a taxonomy or text typology, either in the form of a brief prose description or in terms of the situational parameters used by the TEI formal textDesc" (tei-c.org).
        @param type Type of category description.
        @param text Contents.
        @return A TEI header encoding description / class declaration / taxonomy / category / category description instance.
        """
        ## "May contain core: abbr address choice date distinct email emph expan foreign gloss hi measure measureGrp mentioned name num ptr q ref rs soCalled term time title unit / corpus: textDesc / dictionaries: lang / header: idno / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / tagdocs: att code gi ident listRef tag val / transcr: am ex subst" (tei-c.org)
        # "character data" (tei-c.org)
        self.text = text

        ## Not TEI-compliant
        self.type = type

class category():
    """! TEI header encoding description / class declaration / taxonomy / category class.
    """
    def __init__(self, type=None):
        """! @brief Constructor.
        "(category) contains an individual descriptive category, possibly nested within a superordinate category, within a user-defined taxonomy" (tei-c.org).
        @param type Type of category.
        @return A TEI header encoding description / class declaration / taxonomy / category instance.
        """
        ## "May contain core: desc gloss / header: catDesc category / tagdocs: equiv" (tei-c.org)
        # "(category description) describes some category within a taxonomy or text typology, either in the form of a brief prose description or in terms of the situational parameters used by the TEI formal textDesc." (tei-c.org)
        self.catDesc = []

        ## Not TEI-compliant
        self.type = type

    def __del__(self):
        """! @brief Destructor.
        Release category descriptions instance.
        """
        for catDesc in self.catDesc:
            del catDesc

class taxonomy():
    """! TEI header encoding description / class declaration / taxonomy class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(taxonomy) defines a typology either implicitly, by means of a bibliographic citation, or explicitly by a structured taxonomy" (tei-c.org).
        @return A TEI header encoding description / class declaration / taxonomy instance.
        """
        ## "May contain core: bibl biblStruct desc gloss listBibl / header: biblFull category taxonomy / msdescription: msDesc / tagdocs: equiv" (tei-c.org)
        # "(bibliographic citation) contains a loosely-structured bibliographic citation of which the sub-components may or may not be explicitly tagged.
        # character data" (tei-c.org)
        self.bibl = ""
        # "(category) contains an individual descriptive category, possibly nested within a superordinate category, within a user-defined taxonomy." (tei-c.org)
        self.category = []

    def __del__(self):
        """! @brief Destructor.
        Release catagories instance.
        """
        for category in self.category:
            del category

class classDecl():
    """! TEI header encoding description / class declaration class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(classification declarations) contains one or more taxonomies defining any classificatory codes used elsewhere in the text" (tei-c.org).
        @return A TEI header encoding description / class declaration instance.
        """
        ## "May contain header: taxonomy" (tei-c.org)
        # "(taxonomy) defines a typology either implicitly, by means of a bibliographic citation, or explicitly by a structured taxonomy." (tei-c.org)
        self.taxonomy = taxonomy()

    def __del__(self):
        """! @brief Destructor.
        Release taxinomy instance.
        """
        del self.taxonomy

class encodingDesc():
    """! TEI header encoding description class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(encoding description) documents the relationship between an electronic text and the source or sources from which it was derived" (tei-c.org).
        @return A TEI header encoding description instance.
        """
        ## "May contain core: p / gaiji: charDecl / header: appInfo classDecl editorialDecl geoDecl listPrefixDef projectDesc refsDecl samplingDecl schemaRef styleDefDecl tagsDecl unitDecl / iso-fs: fsdDecl / linking: ab / spoken: transcriptionDesc / tagdocs: constraintDecl schemaSpec / textcrit: variantEncoding / verse: metDecl" (tei-c.org)
        # "(project description) describes in detail the aim or purpose for which an electronic file was encoded, together with any other relevant information concerning the process by which it was assembled or collected." (tei-c.org)
        self.projectDesc = projectDesc()
        # "(sampling declaration) contains a prose description of the rationale and methods used in selecting texts, or parts of a text, for inclusion in the resource." (tei-c.org)
        #self.samplingDecl = None # not used
        # "(editorial practice declaration) provides details of editorial principles and practices applied during the encoding of a text." (tei-c.org)
        #self.editorialDecl = None # not used
        # "(tagging declaration) provides detailed information about the tagging applied to a document." (tei-c.org)
        #self.tagsDecl = None # not used
        # "(style definition language declaration) specifies the name of the formal language in which style or renditional information is supplied elsewhere in the document. The specific version of the scheme may also be supplied." (tei-c.org)
        #self.styleDefDecl = None # not used
        # "(references declaration) specifies how canonical references are constructed for this text." (tei-c.org)
        #self.refsDecl = None # not used
        # "(classification declarations) contains one or more taxonomies defining any classificatory codes used elsewhere in the text." (tei-c.org)
        self.classDecl = None # used only in BTO
        # "(geographic coordinates declaration) documents the notation and the datum used for geographic coordinates expressed as content of the geo element elsewhere within the document." (tei-c.org)
        #self.geoDecl = None # not used
        # "(unit declarations) provides information about units of measurement that are not members of the International System of Units." (tei-c.org)
        #self.unitDecl = None # not used
        # "(schema specification) generates a TEI-conformant schema and documentation for it." (tei-c.org)
        #self.schemaSpec = None # not used
        # "(schema reference) describes or points to a related customization or schema file." (tei-c.org)
        #self.schemaRef = None # not used

### profileDesc

class creation():
    """! TEI header profile description / creation class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(creation) contains information about the creation of a text" (tei-c.org).
        @return A TEI header profile description / creation instance.
        """
        ## May contain core: abbr address choice date distinct email emph expan foreign gloss hi measure measureGrp mentioned name num ptr q ref rs soCalled term time title unit / dictionaries: lang / header: idno listChange / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / tagdocs: att code gi ident listRef tag val / transcr: am ex subst / character data" (tei-c.org)
        # "(date) contains a date in any format. May contain character data" (tei-c.org)
        self.date = None

class language():
    """! TEI header profile description / language usage / language class.
    """
    def __init__(self, ident=None, usage=None, text=None):
        """! @brief Constructor.
        "(language) characterizes a single language or sublanguage used within a text" (tei-c.org).
        @param ident "(identifier) Supplies a language code constructed as defined in BCP 47 which is used to identify the language documented by this element, and which may be referenced by the global xml:lang attribute" (tei-c.org).
        @param usage "(usage) specifies the approximate percentage of the text which uses this language" (tei-c.org).
        @param text Contents.
        @return A TEI header profile description / language usage / language instance.
        """
        ## "Attributes" (tei-c.org)
        # "ident (identifier) Supplies a language code constructed as defined in BCP 47 which is used to identify the language documented by this element, and which may be referenced by the global xml:lang attribute." (tei-c.org)
        self.ident = None
        # "(usage) specifies the approximate percentage of the text which uses this language." (tei-c.org)
        self.usage = None

        ## May contain analysis: interp interpGrp span spanGrp / certainty: certainty precision respons / core: abbr address cb choice date distinct ellipsis email emph expan foreign gap gb gloss hi index lb measure measureGrp mentioned milestone name note noteGrp num pb ptr q ref rs soCalled term time title unit / dictionaries: lang / figures: figure notatedMusic / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef tag val / textcrit: app witDetail / transcr: addSpan am damageSpan delSpan ex fw listTranspose metamark space subst substJoin / character data
        self.text = text # used only in BTO

        ## Not TEI-compliant
        self.langOri = None # used only in PCLv8 and PCLv9
        self.variant = None # dialect, used only in PCLv8 and PCLv9
        self.script = None # used only in PCLv9
        self.variantOri = None # used only in PCLv9
        self.scriptOri = None # used only in PCLv9

class langUsage():
    """! TEI header profile description / language usage class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(language usage) describes the languages, sublanguages, registers, dialects, etc. represented within a text" (tei-c.org).
        @return A TEI header profile description / language usage instance.
        """
        ## "May contain core: p / header: language / linking: ab" (tei-c.org)
        self.language = language()

    def __del__(self):
        """! @brief Destructor.
        Release language instance.
        """
        del self.language

class term():
    """! TEI header profile description / text class / keywords / term class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(term) contains a single-word, multi-word, or symbolic designation which is regarded as a technical term" (tei-c.org).
        @param text Contents.
        @return A TEI header profile description / text class / keywords / term instance.
        """
        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address binaryObject cb choice cit corr date del distinct ellipsis email emph expan foreign gap gb gloss graphic hi index lb measure measureGrp media mentioned milestone name note noteGrp num orig pb ptr q quote ref reg rs ruby said sic soCalled term time title unclear unit / dictionaries: lang oRef pRef / figures: figure formula notatedMusic / gaiji: g / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef specDesc specList tag val / textcrit: app witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data" (tei-c.org)
        self.text = text

class keywords():
    """! TEI header profile description / text class / keywords class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(keywords) contains a list of keywords or phrases identifying the topic or nature of a text" (tei-c.org).
        @return A TEI header profile description / text class / keywords instance.
        """
        ## "Attributes" (tei-c.org)
        # "(scheme) identifies the controlled vocabulary within which the set of keywords concerned is defined, for example by a taxonomy element, or by some other resource." (tei-c.org)
        #self.scheme = None # not used

        ## "May contain core: list term" (tei-c.org)
        # "(term) contains a single-word, multi-word, or symbolic designation which is regarded as a technical term." (tei-c.org)
        self.term = []

    def __del__(self):
        """! @brief Destructor.
        Release terms instance.
        """
        for term in self.term:
            del term

class textClass():
    """! TEI header profile description / text class class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(text classification) groups information which describes the nature or topic of a text in terms of a standard classification scheme, thesaurus, etc" (tei-c.org)
        @return A TEI header profile description / text class instance.
        """
        ## "May contain header: catRef classCode keywords" (tei-c.org)
        # "(keywords) contains a list of keywords or phrases identifying the topic or nature of a text." (tei-c.org)
        self.keywords = keywords()

    def __del__(self):
        """! @brief Destructor.
        Release keywords instance.
        """
        del self.keywords

class derivation():
    """! TEI header profile description / text description / derivation class.
    """
    def __init__(self, type=None):
        """! @brief Constructor.
        "(derivation) describes the nature and extent of originality of this text" (tei-c.org).
        @param type "(type) categorizes the derivation of the text" (tei-c.org).
        @return A TEI header profile description / text description / derivation instance.
        """
        ## "Attributes" (tei-c.org)
        # "(type) categorizes the derivation of the text. Sample values include: original / revision / translation / abridgment / plagiarism / traditional" (tei-c.org)
        self.type = None

        ## "May contain analysis: interp interpGrp span spanGrp / certainty: certainty precision respons / core: abbr address cb choice date distinct ellipsis email emph expan foreign gap gb gloss hi index lb measure measureGrp mentioned milestone name note noteGrp num pb ptr q ref rs soCalled term time title unit / dictionaries: lang / figures: figure notatedMusic / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef tag val / textcrit: app witDetail / transcr: addSpan am damageSpan delSpan ex fw listTranspose metamark space subst substJoin / character data

class domain():
    """! TEI header profile description / text description / domain class.
    """
    def __init__(self, type=None):
        """! @brief Constructor.
        "(domain of use) describes the most important social context in which the text was realized or for which it is intended, for example private vs. public, education, religion, etc" (tei-c.org).
        @param type "(type) categorizes the domain of use" (tei-c.org).
        @return A TEI header profile description / text description / domain instance.
        """
        ## "Attributes" (tei-c.org)
        # "(type) categorizes the domain of use. Sample values include: art / domestic / religious / business / education / govt / public" (tei-c.org)
        self.type = None

        ## May contain analysis: interp interpGrp span spanGrp / certainty: certainty precision respons / core: abbr address cb choice date distinct ellipsis email emph expan foreign gap gb gloss hi index lb measure measureGrp mentioned milestone name note noteGrp num pb ptr q ref rs soCalled term time title unit / dictionaries: lang / figures: figure notatedMusic / header: idno / iso-fs: fLib fs fvLib / linking: alt altGrp anchor join joinGrp link linkGrp timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / spoken: incident kinesic pause shift vocal writing / tagdocs: att code gi ident listRef tag val / textcrit: app witDetail / transcr: addSpan am damageSpan delSpan ex fw listTranspose metamark space subst substJoin / character data

# Not TEI-compliant, used only in PCL
class genre():
    def __init__(self, lang="en", type=None):
        self.lang = lang
        self.type = type
class textForm():
    def __init__(self, type=None):
        self.type = type

class textDesc():
    """! TEI header profile description / text description class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(text description) provides a description of a text in terms of its situational parameters" (tei-c.org).
        @return A TEI header profile description / text description instance.
        """
        ## "May contain corpus: channel constitution derivation domain factuality interaction preparedness purpose" (tei-c.org)
        # "(derivation) describes the nature and extent of originality of this text." (tei-c.org)
        self.derivation = derivation()
        # "(domain of use) describes the most important social context in which the text was realized or for which it is intended, for example private vs. public, education, religion, etc." (tei-c.org)
        self.domain = []

        ## Not TEI-compliant
        self.genre = [] # used only in PCL
        self.textForm = textForm() # used only in PCL

    def __del__(self):
        """! @brief Destructor.
        Release derivation, domains, genres and text form instances.
        """
        del self.derivation
        for domain in self.domain:
            del domain
        for genre in self.genre:
            del genre
        del self.textForm

class profileDesc():
    """! TEI header profile description class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(text-profile description) provides a detailed description of non-bibliographic aspects of a text, specifically the languages and sublanguages used, the situation in which it was produced, the participants and their setting" (tei-c.org).
        @return A TEI header profile description instance.
        """
        ## "May contain corpus: particDesc settingDesc textDesc / header: abstract calendarDesc correspDesc creation langUsage textClass / transcr: handNotes listTranspose" (tei-c.org)
        # "(abstract) contains a summary or formal abstract prefixed to an existing source document by the encoder." (tei-c.org)
        #self.abstract = None # not used
        # "(creation) contains information about the creation of a text." (tei-c.org)
        self.creation = creation()
        # "(language usage) describes the languages, sublanguages, registers, dialects, etc. represented within a text." (tei-c.org)
        self.langUsage = langUsage()
        # "(text classification) groups information which describes the nature or topic of a text in terms of a standard classification scheme, thesaurus, etc." (tei-c.org)
        self.textClass = None # used only in PCLv9
        # "(correspondence description) contains a description of the actions related to one act of correspondence." (tei-c.org)
        #self.correspDesc = None # not used
        # "(calendar description) contains a description of the calendar system used in any dating expression found in the text." (tei-c.org)
        #self.calendarDesc = None # not used
        # "(text description) provides a description of a text in terms of its situational parameters." (tei-c.org)
        self.textDesc = None # used only in PCL
        # "(participation description) describes the identifiable speakers, voices, or other participants in any kind of text or other persons named or otherwise referred to in a text, edition, or metadata." (tei-c.org)
        #self.particDesc = None # not used
        # "(setting description) describes the setting or settings within which a language interaction takes place, or other places otherwise referred to in a text, edition, or metadata." (tei-c.org)
        #self.settingDesc = None # not used

        ## Not TEI-compliant
        self.category = None # used only in PCLv8

    def __del__(self):
        """! @brief Destructor.
        Release lang usage and creation instances.
        """
        del self.langUsage
        del self.creation

### revisionDesc

class change():
    """! TEI header revision description / list of changes / change class.
    """
    def __init__(self, who=None, when=None, text=None):
        """! @brief Constructor.
        "(change) documents a change or set of changes made during the production of a source document, or during the revision of an electronic file" (tei-c.org).
        @param who "(att.ascribed > who) indicates the person, or group of people, to whom the element content is ascribed" (tei-c.org).
        @param when "(att.datable.w3c > when) supplies the value of the date or time in a standard form, e.g. yyyy-mm-dd" (tei-c.org).
        @param text Contents.
        @return A TEI header revision description / list of changes / change instance.
        """
        ## "Attributes" (tei-c.org)
        # "(target) points to one or more elements that belong to this change." (tei-c.org)
        #self.target = None # not used
        # "(att.ascribed > who) indicates the person, or group of people, to whom the element content is ascribed." (tei-c.org)
        self.who = who
        # "(att.datable.w3c > when) supplies the value of the date or time in a standard form, e.g. yyyy-mm-dd." (tei-c.org)
        self.when = when

        ## "May contain analysis: c cl interp interpGrp m pc phr s span spanGrp w / certainty: certainty precision respons / core: abbr add address bibl biblStruct binaryObject cb choice cit corr date del desc distinct ellipsis email emph expan foreign gap gb gloss graphic hi index l label lb lg list listBibl measure measureGrp media mentioned milestone name note noteGrp num orig p pb ptr q quote ref reg rs ruby said sic soCalled sp stage term time title unclear unit / dictionaries: lang oRef pRef / drama: camera caption castList move sound spGrp tech view / figures: figure formula notatedMusic table / gaiji: g / header: biblFull idno / iso-fs: fLib fs fvLib / linking: ab alt altGrp anchor join joinGrp link linkGrp seg timeline / msdescription: catchwords depth dim dimensions height heraldry locus locusGrp material msDesc objectType origDate origPlace secFol signatures stamp watermark width / namesdates: addName affiliation bloc climate country district eventName forename genName geo geogFeat geogName listEvent listNym listObject listOrg listPerson listPlace listRelation location nameLink objectName offset orgName persName persPronouns placeName population region roleName settlement state surname terrain trait / nets: eTree forest graph listForest tree / spoken: annotationBlock incident kinesic pause shift u vocal writing / tagdocs: att classSpec code constraintSpec dataSpec eg egXML elementSpec gi ident listRef macroSpec moduleSpec outputRendition specDesc specGrp specGrpRef specList tag val / textcrit: app listApp listWit witDetail / textstructure: floatingText / transcr: addSpan am damage damageSpan delSpan ex fw handShift listTranspose metamark mod redo restore retrace secl space subst substJoin supplied surplus undo / verse: caesura rhyme / character data
        self.text = text

class listChange():
    """! TEI header revision description / list of changes class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(list of changes) groups a number of change descriptions associated with either the creation of a source text or the revision of an encoded text" (tei-c.org).
        @return A TEI header revision description / list of changes instance.
        """
        ## "Attributes" (tei-c.org)
        # "(ordered) indicates whether the ordering of its child change elements is to be considered significant or not." (tei-c.org)
        #self.ordered = None # not used

        ## "May contain core: desc / header: change listChange" (tei-c.org)
        # "(change) documents a change or set of changes made during the production of a source document, or during the revision of an electronic file." (tei-c.org)
        from datetime import datetime
        self.change = [change(who="pyteilib", when=str(datetime.now()).split()[0], text="File creation")]

    def __del__(self):
        """! @brief Destructor.
        Release changes instances.
        """
        for change in self.change:
            del change

class revisionDesc():
    """! TEI header revision description class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(revision description) summarizes the revision history for a file" (tei-c.org).
        @return A TEI header revision description instance.
        """
        ## "May contain core: list / header: change listChange" (tei-c.org)
        # "(list of changes) groups a number of change descriptions associated with either the creation of a source text or the revision of an encoded text." (tei-c.org)
        self.listChange = listChange()

    def __del__(self):
        """! @brief Destructor.
        Release list of changes instance.
        """
        del self.listChange

### TEI header

class teiHeader():
    """! TEI header class.
    """
    def __init__(self):
        """! @brief Constructor.
        "TEI header supplies descriptive and declarative metadata associated with a digital resource or set of resources" (tei-c.org).
        @return A TEI header instance.
        """
        # MANDATORY "(file description) contains a full bibliographic description of an electronic file." (tei-c.org)
        self.fileDesc = fileDesc()
        # "(encoding description) documents the relationship between an electronic text and the source or sources from which it was derived." (tei-c.org)
        self.encodingDesc = encodingDesc()
        # "(text-profile description) provides a detailed description of non-bibliographic aspects of a text, specifically the languages and sublanguages used, the situation in which it was produced, the participants and their setting." (tei-c.org)
        self.profileDesc = profileDesc()
        # "(non-TEI metadata) provides a container element into which metadata in non-TEI formats may be placed." (tei-c.org)
        #self.xenoData = None # not used
        # "(revision description) summarizes the revision history for a file." (tei-c.org)
        self.revisionDesc = None # used only in PCLv9

    def __del__(self):
        """! @brief Destructor.
        Release TEI instance.
        """
        del self.fileDesc
        del self.encodingDesc
        del self.profileDesc

### TEI body

class s():
    """! TEI text front or body or back / division / paragraph / sentence class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(s-unit) contains a sentence-like division of a text" (tei-c.org).
        @param text Contents.
        @return A TEI text front or body or back / division / paragraph / sentence instance.
        """
        # "character data" (tei-c.org)
        self.text = text
        # "(reference) defines a reference to another location, possibly modified by additional text or comment." (tei-c.org)
        self.ref = None # used only in BTO

class p():
    """! TEI text front or body or back / division / paragraph class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(paragraph) marks paragraphs in prose" (tei-c.org).
        @param text Contents.
        @return A TEI text front or body or back / division / paragraph instance.
        """
        # "character data" (tei-c.org)
        self.text = text
        # "(s-unit) contains a sentence-like division of a text." (tei-c.org)
        self.s = []
        # "(note) contains a note or annotation." (tei-c.org)
        self.note = None # used only in BTO
        # "(reference) defines a reference to another location, possibly modified by additional text or comment." (tei-c.org)
        self.ref = None # used only in BTO
        # "(quotation) contains a phrase or passage attributed by the narrator or author to some agency external to the text." (tei-c.org)
        self.quote = None

# For BaTelÒc
class note():
    """! TEI text back / division / note class.
    """
    def __init__(self, n=None, place=None, text=None):
        """! @brief Constructor.
        "(note) contains a note or annotation" (tei-c.org).
        @param n "(att.global > number) gives a number (or other label) for an element, which is not necessarily unique within the document" (tei-c.org).
        @param place "(att.placement > place) specifies where this item is placed" (tei-c.org).
        @param text Contents.
        @return A TEI text back / division / note instance.
        """
        self.n = n # used only in BTO
        # "Suggested values include: top / bottom / margin / opposite / overleaf / above / right / below / left / end / inline / inspace" (tei-c.org)
        self.place = place
        self.text = text

        self.div = [] # for BTO

class closer():
    """! TEI text body / division / closer class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(closer) groups together salutations, datelines, bylines, and similar phrases appearing as a final group at the end of a division, especially of a letter" (tei-c.org).
        @param text Contents.
        @return A TEI text body / division / closer instance.
        """
        # "character data" (tei-c.org)
        self.text = text
        # "(name, proper noun) contains a proper noun or noun phrase." (tei-c.org)
        self.name = None

class head():
    """! TEI text front or body or back / division / head class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(heading) contains any type of heading, for example the title of a section, or the heading of a list, glossary, manuscript description, etc" (tei-c.org).
        @param text Contents.
        @return A TEI text front or body or back / division / head instance.
        """
        # "May contain character data" (tei-c.org)
        self.text = None # used only in BTO
        # "(arbitrary segment) represents any segmentation of text below the ‘chunk’ level." (tei-c.org)
        self.seg = None # used only in PCL

class div():
    """! TEI text front or body or back / division class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        "(text division) contains a subdivision of the front, body, or back of a text" (tei-c.org).
        @param type "(att.typed > type) characterizes the element in some sense, using any convenient classification scheme or typology" (tei-c.org).
        @param text Contents.
        @return A TEI text front or body or back / division instance.
        """
        ## "Attributes" (tei-c.org)
        # "(att.typed > type) characterizes the element in some sense, using any convenient classification scheme or typology." (tei-c.org)
        self.type = type

        ## May contain May contain analysis: interp interpGrp span spanGrp / certainty: certainty precision respons / cmc: post / core: bibl biblStruct cb cit desc divGen ellipsis gap gb head index l label lb lg list listBibl meeting milestone note noteGrp p pb q quote said sp stage / dictionaries: entry entryFree superEntry / drama: camera caption castList move sound spGrp tech view / figures: figure notatedMusic table / header: biblFull / iso-fs: fLib fs fvLib / linking: ab alt altGrp anchor join joinGrp link linkGrp timeline / msdescription: msDesc / namesdates: listEvent listNym listObject listOrg listPerson listPlace listRelation / nets: eTree forest graph listForest tree / spoken: annotationBlock incident kinesic pause shift u vocal writing / tagdocs: classSpec constraintSpec dataSpec eg egXML elementSpec macroSpec moduleSpec outputRendition schemaSpec specGrp specGrpRef / textcrit: app listApp listWit witDetail / textstructure: argument byline closer dateline div docAuthor docDate epigraph floatingText opener postscript salute signed trailer / transcr: addSpan damageSpan delSpan fw listTranspose metamark space substJoin
        # "(heading) contains any type of heading, for example the title of a section, or the heading of a list, glossary, manuscript description, etc." (tei-c.org)
        self.head = head()
        # "(paragraph) marks paragraphs in prose." (tei-c.org)
        self.p = []
        # "(text division) contains a subdivision of the front, body, or back of a text." (tei-c.org)
        self.div = []
        # "(epigraph) contains a quotation, anonymous or attributed, appearing at the start or end of a section or on a title page." (tei-c.org)
        self.epigraph = None # used only in BTO
        # "(cited quotation) contains a quotation from some other document, together with a bibliographic reference to its source." (tei-c.org)
        self.cit = None # used only in BTO
        # "(note) contains a note or annotation." (tei-c.org)
        self.note = None # used only in BTO
        # "(opener) groups together dateline, byline, salutation, and similar phrases appearing as a preliminary group at the start of a division, especially of a letter." (tei-c.org)
        self.opener = None # used only in BTO
        # "(closer) groups together salutations, datelines, bylines, and similar phrases appearing as a final group at the end of a division, especially of a letter." (tei-c.org)
        self.closer = None # used only in BTO
        # "(dateline) contains a brief description of the place, date, time, etc. of production of a letter, newspaper story, or other work, prefixed or suffixed to it as a kind of heading or trailer." (tei-c.org)
        self.dateline = None # used only in BTO
        # "(salutation) contains a salutation or greeting prefixed to a foreword, dedicatory epistle, or other division of a text, or the salutation in the closing of a letter, preface, etc." (tei-c.org)
        self.salute = None # used only in BTO
        # "(quotation) contains a phrase or passage attributed by the narrator or author to some agency external to the text." (tei-c.org)
        self.quote = None # used only in BTO

        ## Not TEI-compliant
        self.text = text

    def __del__(self):
        """! @brief Destructor.
        Release paragraphs and divisions instances.
        """
        for p in self.p:
            del p
        for div in self.div:
            del div
        del self.closer

## Handle BaTelÒc XML TEI text front: 'docTitle', 'bibl', 'docAuthor', 'titlePart', 'dedicace', 'epigraph', 'quote', 'cit', 'note', 'titlePage', 'prologue'

class bibl():
    """! TEI text front / document title / bibliography class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(bibliographic citation) contains a loosely-structured bibliographic citation of which the sub-components may or may not be explicitly tagged" (tei-c.prg).
        @param text Contents.
        @return A TEI text front / document title / bibliography instance.
        """
        # "character data" (tei-c.org)
        self.text = text
        # "(author) in a bibliographic reference, contains the name(s) of an author, personal or corporate, of a work; for example in the same form as that provided by a recognized bibliographic name authority." (tei-c.org)
        self.author = None
        # "(title) contains a title for any kind of work." (tei-c.org)
        self.title = None

        ## Not TEI-compliant
        self.docAuthor = None

class titlePart():
    """! TEI text front / document title / title part  class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        "(title part) contains a subsection or division of the title of a work, as indicated on a title page" (tei-c.org).
        @param type "(att_typed > type) specifies the role of this subdivision of the title" (tei-c.org).
        @param text Contents.
        @return A TEI text front / document title / title part instance.
        """
        # Suggested values include: main / sub / alt / short / desc
        self.type = type
        # "character data" (tei-c.org)
        self.text = text

class quote():
    """! TEI text front / document title or title page / epigraph / citation / quote class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(quotation) contains a phrase or passage attributed by the narrator or author to some agency external to the text" (tei-c.org)
        @param text Contents.
        @return A TEI text front / document title or title page / epigraph / citation / quote instance.
        """
        # "character data" (tei-c.org)
        self.text = text
        # "(language name) contains the name of a language mentioned in etymological or other linguistic discussion." (tei-c.org)
        self.lang = None
        # "(paragraph) marks paragraphs in prose." (tei-c.org)
        self.p = None

class cit():
    """! TEI text front / document title or title page / epigraph / citation class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(cited quotation) contains a quotation from some other document, together with a bibliographic reference to its source" (tei-c.org).
        @param text Contents.
        @return A TEI text front / document title or title page / epigraph / citation instance.
        """
        # "(bibliographic citation) contains a loosely-structured bibliographic citation of which the sub-components may or may not be explicitly tagged." (tei-c.org)
        self.bibl = None
        # "(quotation) contains a phrase or passage attributed by the narrator or author to some agency external to the text." (tei-c.org)
        self.quote = None

        ## Not TEI-compliant
        self.text = text
        self.p = None

class epigraph():
    """! TEI text (front / document title) or (body / division) / epigraph class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(epigraph) contains a quotation, anonymous or attributed, appearing at the start or end of a section or on a title page" (tei-c.org)
        @return A TEI text (front / document title) or (body / division) / epigraph instance.
        """
        # "(bibliographic citation) contains a loosely-structured bibliographic citation of which the sub-components may or may not be explicitly tagged." (tei-c.org)
        self.bibl = None
        # "(cited quotation) contains a quotation from some other document, together with a bibliographic reference to its source." (tei-c.org)
        self.cit = cit()
        # "(note) contains a note or annotation." (tei-c.org)
        self.note = ""
        # "(quotation) contains a phrase or passage attributed by the narrator or author to some agency external to the text." (tei-c.org)
        self.quote = None

    def __del__(self):
        """! @brief Destructor.
        Release citation instance.
        """
        del self.cit

class docTitle():
    """! TEI text front / document title class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(document title) contains the title of a document, including all its constituents, as given on a title page" (tei-c.org).
        @return A TEI text front / document title instance.
        """
        # "(title part) contains a subsection or division of the title of a work, as indicated on a title page." (tei-c.org)
        self.titlePart = titlePart(type="principal")

        ## Not TEI-compliant
        self.bibl = bibl()
        self.dedicace = None
        self.epigraph = epigraph()

    def __del__(self):
        """! @brief Destructor.
        Release title part and epigraph instances.
        """
        del self.titlePart
        del self.bibl
        del self.epigraph

class titlePage():
    """! TEI text front / title page class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(title page) contains the title page of a text, appearing within the front or back matter" (tei-c.org).
        @return A TEI text front / title page instance.
        """
        # "(note) contains a note or annotation." (tei-c.org)
        self.note = None
        # "(byline) contains the primary statement of responsibility given for a work on its title page or at the head or end of the work." (tei-c.org)
        self.byline = None
        # "(document author) contains the name of the author of the document, as given on the title page (often but not always contained in a byline)." (tei-c.org)
        self.docAuthor = None
        # "(document date) contains the date of a document, as given on a title page or in a dateline." (tei-c.org)
        self.docDate = None
        # "(document edition) contains an edition statement as presented on a title page of a document." (tei-c.org)
        self.docEdition = None
        # "(document imprint) contains the imprint statement (place and date of publication, publisher name), as given (usually) at the foot of a title page." (tei-c.org)
        self.docImprint = None
        # "(document title) contains the title of a document, including all its constituents, as given on a title page." (tei-c.org)
        self.docTitle = None
        # "(epigraph) contains a quotation, anonymous or attributed, appearing at the start or end of a section or on a title page." (tei-c.org)
        self.epigraph = epigraph()
        # "(title part) contains a subsection or division of the title of a work, as indicated on a title page." (tei-c.org)
        self.titlePart = None

        ## Not TEI-compliant
        self.p = []
        self.div = []

    def __del__(self):
        """! @brief Destructor.
        Release epigraph instance.
        """
        del self.epigraph
        for p in self.p:
            del p

class prologue():
    """! TEI text front / prologue class.
    """
    def __init__(self, text=None):
        """! @brief Constructor.
        "(prologue) contains the prologue to a drama, typically spoken by an actor out of character, possibly in association with a particular performance or venue" (tei-c.org)
        @param text Contents.
        @return A TEI text front / prologue instance.
        """
        # "(paragraph) marks paragraphs in prose." (tei-c.org)
        self.p = []

        ## Not TEI-compliant
        self.text = text

    def __del__(self):
        """! @brief Destructor.
        Release paragraphs instance.
        """
        for p in self.p:
            del p

class front():
    """! TEI text front class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(front matter) contains any prefatory matter (headers, abstracts, title page, prefaces, dedications, etc.) found at the start of a document, before the main body" (tei-c.org)
        @return A TEI text front instance.
        """
        # "(document title) contains the title of a document, including all its constituents, as given on a title page." (tei-c.org)
        self.docTitle = docTitle()
        # "(title page) contains the title page of a text, appearing within the front or back matter." (tei-c.org)
        self.titlePage = titlePage()
        # "(prologue) contains the prologue to a drama, typically spoken by an actor out of character, possibly in association with a particular performance or venue." (tei-c.org)
        self.prologue = prologue()
        # "(text division) contains a subdivision of the front, body, or back of a text." (tei-c.org)
        self.div = []

    def __del__(self):
        """! @brief Destructor.
        Release document title, title page, divisions and prologue instances.
        """
        del self.docTitle
        del self.titlePage
        del self.prologue
        for div in self.div:
            del div

## Handle BaTelÒc XML TEI text back: 'epilogue'

class epilogue():
    """! TEI text back / epilogue class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(epilogue) contains the epilogue to a drama, typically spoken by an actor out of character, possibly in association with a particular performance or venue" (tei-c.org)
        @return A TEI text back / epilogue instance.
        """
        ## Not TEI-compliant
        self.div = []

    def __del__(self):
        """! @brief Destructor.
        Release divisions instance.
        """
        for div in self.div:
            del div

class back():
    """! TEI text back class.
    """
    def __init__(self):
        """! @brief Constructor.
        "(back matter) contains any appendixes, etc. following the main part of a text" (tei-c.org)
        @return A TEI text back instance.
        """
        # "(epilogue) contains the epilogue to a drama, typically spoken by an actor out of character, possibly in association with a particular performance or venue." (tei-c.org)
        self.epilogue = epilogue()
        # "(text division) contains a subdivision of the front, body, or back of a text." (tei-c.org)
        self.div = []

        ## Not TEI-compliant
        self.p = None # used only in BTO

    def __del__(self):
        """! @brief Destructor.
        Release epilogue and divisions instances.
        """
        del self.epilogue
        for div in self.div:
            del div

## For BaTelÒc XML TEI text body

class div4(div):
    """! TEI text body / division class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        TEI text body / division instance.
        @return A TEI text body / division instance.
        """
        div.__init__(self, type, text)

    def __del__(self):
        """! @brief Destructor.
        """
        div.__del__(self)

class div3(div):
    """! TEI text body / division class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        TEI text body / division instance.
        @return A TEI text body / division instance.
        """
        div.__init__(self, type, text)

    def __del__(self):
        """! @brief Destructor.
        """
        div.__del__(self)

class div2(div):
    """! TEI text body / division class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        TEI text body / division instance.
        @return A TEI text body / division instance.
        """
        div.__init__(self, type, text)

    def __del__(self):
        """! @brief Destructor.
        """
        div.__del__(self)

class div1(div):
    """! TEI text body / division class.
    """
    def __init__(self, type=None, text=None):
        """! @brief Constructor.
        TEI text body / division instance.
        @return A TEI text body / division instance.
        """
        div.__init__(self, type, text)

    def __del__(self):
        """! @brief Destructor.
        """
        div.__del__(self)

class body():
    """! TEI text body class.
    """
    def __init__(self):
        """! @brief Constructor.
        TEI text body instance.
        @return A TEI text body instance.
        """
        self.__full_text = ""
        self.div = []

    def __del__(self):
        """! @brief Destructor.
        Release divisions instance.
        """
        for div in self.div:
            del div

    def add_text(self, some_text, new_line=False):
        """! @brief Add some text to text body.
        @param some_text A string containing some text.
        @param new_line Indicates if a new line has to be inserted. If not provided, default value is False.
        @return None.
        """
        if some_text is not None:
            if len(self.__full_text) > 0 and self.__full_text[-1] != '\n':
                if new_line:
                    self.__full_text += '\n'
                else:
                    self.__full_text += ' '
            self.__full_text += some_text

    def get_text(self):
        """! @brief Get full text.
        @return A string containing full text body.
        """
        return self.__full_text

class text():
    """! TEI text class.
    """
    def __init__(self):
        """! @brief Constructor.
        TEI text instance.
        @return A TEI text instance.
        """
        self.front = None # for BTO
        self.body = body()
        self.back = None # for BTO

    def __del__(self):
        """! @brief Destructor.
        Release body instance.
        """
        del self.body

### TEI

class TEI():
    """! TEI class.
    """
    def __init__(self, id='0'):
        """! @brief Constructor.
        TEI instance.
        @param id IDentifier. If not provided, default value is '0'.
        @return A TEI instance.
        """
        self.__filename = None
        self.id = id

        # "(TEI header) supplies descriptive and declarative metadata associated with a digital resource or set of resources." (tei-c.org)
        self.teiHeader = teiHeader()

        self.text = text()

    def __del__(self):
        """! @brief Destructor.
        Release TEI header and text instances.
        """
        del self.teiHeader
        del self.text

    def set_filename(self, filename):
        """! @brief Set filename.
        @param filename The name of the XML file linked to this TEI instance, for instance 'example.xml'.
        @return None.
        """
        self.__filename = filename

    def get_filename(self):
        """! @brief Get filename.
        @return A string containing the name of the XML file linked to this TEI instance, for instance 'example.xml'.
        """
        return self.__filename

### TEI corpus

class teiCorpus():
    """! TEI corpus class.
    """
    def __init__(self):
        """! @brief Constructor.
        TEI corpus instance.
        @return A TEI corpus instance.
        """
        self.__filename = None
        self.TEI = TEI()

    def __del__(self):
        """! @brief Destructor.
        Release TEI instance.
        """
        del self.TEI

    def set_filename(self, filename):
        """! @brief Set filename.
        @param filename The name of the XML file linked to this TEI corpus instance, for instance 'example.xml'.
        @return None.
        """
        self.__filename = filename

    def get_filename(self):
        """! @brief Get filename.
        @return A string containing the name of the XML file linked to this TEI corpus instance, for instance 'example.xml'.
        """
        return self.__filename

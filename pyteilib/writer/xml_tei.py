#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package writer
"""

from utils.xml_format import write_result, Element, SubElement
from utils.io import ENCODING

def xml_tei_write(object, filename, xml_type='TEI'):
    """! @brief Write an XML TEI file.
    @param object The TEI instance to write as XML.
    @param filename The name of the XML TEI file to write with full path, for instance 'user/output/example.xml'.
    @param xml_type The type of the XML TEI file to write: 'BTO', 'PCLv8', 'PCLv9'.
    """
    print("Write " + object.__class__.__name__ + " to XML file " + filename)
    # Create the root XML element
    if (object.__class__.__base__.__name__ == "TEI"):
        object.set_filename(filename)
        root = Element(object.__class__.__base__.__name__)
    else:
        root = Element(object.__class__.__name__)
    # Create all XML sub-elements
    build_sub_elements(object, root, xml_type)
    # Write all created XML elements in the output file
    write_result(root, filename)

def build_sub_elements(object, element, xml_type='TEI'):
    """! @brief Create XML sub-elements to an existing XML element by parsing a TEI object instance.
    @param object A TEI object instance.
    @param element XML element for which sub-elements have to be created according to TEI object attributes.
    @param xml_type The type of the TEI object instance: 'BTO', 'PCLv8', 'PCLv9'.
    """
    from xml.sax.saxutils import unescape
    # Parse instance attributes
    for item in object.__dict__.items():
        # Handle BaTelÒc XML
#        if xml_type == 'BTO':
#            if element.tag == "author":
#                if object.name.forename is None:
#                    element.text = object.name.surname
#                elif object.name.surname is None:
#                    element.text = object.name.forename
#                else:
#                    element.text = ' '.join([object.name.forename, object.name.surname]).strip()
#                continue
        attr_name = item[0]
        attr_value = item[1]
        if type(attr_value) is str:
            attr_value = unescape(attr_value)
        # For each defined public attribute, create an XML sub-element
        if not attr_name.startswith('_'):
            if attr_value is not None:
                # Handle boolean values
                if type(attr_value) is bool:
                    attr_value = unicode(attr_value)
                # Check if the attribute is itself a class instance
                if type(attr_value) is list:
                    # We suppose that a list always contains objects
                    for item in attr_value:
                        sub_element = SubElement(element, item.__class__.__name__)
                        if item is not None:
                            build_sub_elements(item, sub_element, xml_type)
                elif type(attr_value) not in [int, str]:
                    # If this is the case, create an XML element and restart the same operation recursively on this object
                    sub_element = SubElement(element, attr_value.__class__.__name__)
                    build_sub_elements(attr_value, sub_element, xml_type)
                elif attr_name in ["id", "type", "unit", "quantity", "status", "ident", "langOri", "variant", "variantOri", "script", "scriptOri", "when", "who", "lang", "n", "place"]:
                    # Handle 'xml:lang' attribute
                    if attr_name == "lang":
                        attr_name = "xml:lang"
                    # If this is a specical attribute (e.g. "id"), it must be inserted as an XML element attribute
                    if type(attr_value) is int:
                        attr_value = str(attr_value)
                    element.attrib.update({attr_name: attr_value})
                elif attr_name == "text":
                    element.text = attr_value
                else:
                    # In all other cases, an XML sub-element must be created
                    sub_element = SubElement(element, attr_name)
                    sub_element.text = attr_value

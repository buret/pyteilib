#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package reader
"""

from utils.xml_format import parse_xml, fromstring, tostring
from utils.error_handling import InputError

def factory(object_name, attributes):
    """! @brief This function is an object factory. Indeed, from an object name and its attributes, it creates a Python object and sets its attributes.
    @param object_name A Python string containing the object name, for instance 'teiHeader'.
    @param attributes A Python dictionary containing pairs of attribute name (as a Python string) and value, for instance {'title': 'This is the title'}.
    """
    # Set module name
    module_name = "tei_p5"
    # Find the package in which the object class is defined, in order to be able to import the correct Python module
    import sys, os, glob
    running_path = sys.path[0]
    if os.name == 'posix':
        # Unix-style path
        separator = '/'
    else:
        # Windows-style path
        separator = '\\'
    full_path = glob.glob(running_path + separator + ".." + separator + "pyteilib" + separator + "*" + separator + module_name + ".py")
    if len(full_path) < 1:
        # No file with this name exists
        raise InputError(module_name + ".py", "No file named '%s' exists in the library. It is not allowed, so please solve this issue by renaming files correctly." % (module_name + ".py"))
    elif len(full_path) > 1:
        # Several files with this name exist
        raise InputError(module_name + ".py", "Several files named '%s' exist in the library. It is not allowed, so please solve this issue by renaming files correctly. Here is the list of found files with this name: %s" % ((module_name + ".py"), str(full_path)))
    # Retrieve package name from full path
    package_name = full_path[0].split(separator)[-2]
    # Import object module: "package.module"
    object_module = __import__(package_name + "." + module_name)
    try:
        # Retrieve object class from module
        object_class = getattr(object_module, object_name)
        # Create an instance of it
        instance = object_class()
        # Set class attributes
        for attribute in list(attributes.items()):
            if '}' in attribute[0]:
                # Handle 'xml:lang' attribute
                setattr(instance, attribute[0].split('}')[-1], attribute[1])
            else:
                setattr(instance, attribute[0], attribute[1])
    except AttributeError:
        instance = None
    return instance

def xml_tei_read(filename, xml_type='TEI', keep_highlighted=False):
    """! @brief Read an XML TEI file.
    @param filename The name of the XML TEI file to read with full path, for instance 'user/input.xml'.
    @param xml_type The type of the XML TEI file to read: 'BTO', 'PCLv8', 'PCLv9'.
    @param keep_highlighted Boolean to keep the <hi> tags or not.
    @return A TEI instance.
    """
    root = parse_xml(filename)
    # Create an object instance corresponding to the XML root element
    if root.tag == 'TEI':
        root.tag = xml_type
    root_instance = factory(root.tag, root.attrib)
    root_instance.set_filename(filename)
    # Parse XML sub-elements and create instance childs
    get_sub_elements(root_instance, root, xml_type, keep_highlighted)
    return root_instance

def get_sub_elements(instance, element, xml_type='TEI', keep_highlighted=False):
    """! @brief This function recursively parses the given XML element and creates corresponding TEI instances with their attributes.
    @param instance A TEI object instance.
    @param element An XML element.
    @param xml_type The type of the TEI object instance: 'BTO', 'PCLv8', 'PCLv9'.
    @param keep_highlighted Boolean to keep the <hi> tags or not.
    """
    for sub_element in element:
        if xml_type == 'BTO': # TODO: add letter ('opener', 'closer') + 'dateline', 'salute', 'formula', 'correction'
            # Fix BaTelÒc naming errors
            if sub_element.tag == "respstmt":
                sub_element.tag = "respStmt"
            elif sub_element.tag == "projetDesc":
                sub_element.tag = "projectDesc"
            elif sub_element.tag == "seriesStmt" and element.tag == "imprint":
                sub_element.tag = "series"
            # Clean BaTelÒc XML
            if sub_element.text is not None and sub_element.tag != "p" and sub_element.tag != "foreign" and sub_element.tag != "place" and sub_element.tag != "date" and sub_element.tag != "name":
                sub_element.text = sub_element.text.strip()
            # Handle BaTelÒc XML TEI text body: 'q', 'hi', 'foreign', 'lg', 'l', 'signed', 'place', 'date', 'name', 'list', 'item', 'address'?
            if sub_element.tag == "q":
                # 'q' elements indicate a dialog => directly get sub-elements
                get_sub_elements(instance, sub_element, xml_type, keep_highlighted)
                continue
            elif sub_element.tag == "hi":
                # 'hi' elements indicate rendering => ignore them
                if element.tag == "p":
                    if keep_highlighted:
                        instance.text = tostring(element, encoding='unicode', method='xml').strip().replace("<p>", '').replace("</p>", '')
                    else:
                        instance.text = tostring(element, encoding='unicode', method='text').strip()
                continue
            elif sub_element.tag == "head" and element.tag.startswith("div"):
                if keep_highlighted:
                    # Do not keep 'foreign' tags
                    instance.head = tostring(sub_element, encoding='unicode', method='xml').strip().replace("<head>", '').replace("<head rend=\"I\">", '').replace("<head rend=\"G\">", '').replace("<head rend=\"M\">", '').replace("</head>", '').replace("<foreign xml:lang=\"fr\">", '').replace("</foreign>", '')
                else:
                    instance.head = tostring(sub_element, encoding='unicode', method='text').strip()
                continue
            elif sub_element.tag == "foreign":
                # 'foreign' elements indicate lang => ignore them or directly get sub-elements
                if element.tag == "p" or element.tag == "s":
                    if keep_highlighted:
                        instance.text = tostring(element, encoding='unicode', method='xml').strip().replace("<p>", '').replace("</p>", '').replace("<s>", '').replace("</s>", '').replace("<foreign xml:lang=\"fr\">", '').replace("</foreign>", '')
                    else:
                        instance.text = tostring(element, encoding='unicode', method='text').strip()
                else:
                    get_sub_elements(instance, sub_element, xml_type, keep_highlighted)
                continue
            elif sub_element.tag == "signed":
                # 'signed' elements indicate a signature => replace by 'p'
                sub_element.tag = "p"
            elif (sub_element.tag == "place" or sub_element.tag == "date" or sub_element.tag == "name") and element.tag == "p":
                instance.text = tostring(element, encoding='unicode', method='text').strip()
                continue
            elif sub_element.tag == "lg" and element.tag == "address":
                # Do not keep 'lg' => set address
                instance.address = sub_element.text
                continue
            elif sub_element.tag == "lg" and element.tag.startswith("div"):
                # Do not keep 'lg' => replace by 'p'
                sub_element.tag = "p"
                try:
                    del sub_element.attrib["rend"]
                    del sub_element.attrib["type"]
                except KeyError:
                    pass
            elif sub_element.tag == "head" and element.tag == "p":
                # Do not keep 'head' => replace by 's'
                sub_element.tag = "s"
                try:
                    del sub_element.attrib["rend"]
                except KeyError:
                    pass
            elif sub_element.tag == "l" and element.tag == "p":
                # Do not keep 'l' => replace by 's'
                sub_element.tag = "s"
            elif sub_element.tag == "list":
                # Do not keep 'list' => replace by 'p'
                sub_element.tag = "p"
            elif sub_element.tag == "item":
                # Do not keep 'item' => replace by 's'
                sub_element.tag = "s"
            # Handle BaTelÒc XML TEI header
            elif sub_element.tag == "extent" and element.tag == "fileDesc":
                # Simply set the value
                instance.extent = sub_element.text
                continue
            elif element.tag == "author" and instance.id is not None:
                # An 'author' object has already been created => simply set its attributes
                setattr(instance, sub_element.tag, sub_element.text)
                continue
            elif sub_element.tag == "name" and element.tag == "respStmt" and instance.resp is not None:
                # A 'respStmt' object has already been created => simply set its name
                instance.name = sub_element.text
                continue
        # Create TEI sub-instance corresponding to XML sub-element
        sub_instance = factory(sub_element.tag, sub_element.attrib)
        try:
            # If instance owns a 'text' attribute, set it
            if sub_instance.text is None:
                sub_instance.text = sub_element.text
        except AttributeError:
            pass
        # Root TEI object must own the child objects
        attr_name = sub_element.tag
        if attr_name.startswith("div"):
            attr_name = "div"
        attr_value = getattr(instance, attr_name)
        if type(attr_value) is list and sub_instance is not None:
            # If this attribute is a list, append the new value to the list
            attr_value.append(sub_instance)
        elif type(attr_value) is str or sub_instance is None:
            # Simply set the value
            setattr(instance, attr_name, sub_element.text)
        elif sub_instance is not None:
            # Attach sub-instance to instance
            setattr(instance, attr_name, sub_instance)
        # Repeat the same operation recursively
        if sub_instance is None:
            sub_instance = instance
        get_sub_elements(sub_instance, sub_element, xml_type, keep_highlighted)

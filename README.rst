========
pyteilib
========

Latest version: 1.0

Date: October 12, 2025

Author: Céline Buret

Maintainer: Céline Buret

Documentation: -

Home page: https://github.com/buret/pyteilib

License: gpl-3.0

Platform: Unix, Linux, MAC

Package index owner: Céline Buret

Introduction
=============

What is pyteilib?
___________________

The Python TEI library is a suite of open-source Python modules for XML format conversion. It performs automatic tasks for multi-languages texts, such as conversion between different formats used to represent texts.

The main idea of ``pyteilib`` is to provide a software package which integrates conversion functions from and to several formats: XML BaTelÒc, XML ParCoLab (version 8 and 9), CSV, TXT, DOC, DOCX, etc.

``pyteilib`` implements the TEI guidelines. For more details, please see https://tei-c.org/release/doc/tei-p5-doc/en/html/index.html. TEI tools are available at https://teigarage.tei-c.org.

What can be done with pyteilib?
__________________________________

With the help of ``pyteilib``, users can:
 - convert a BaTelÒc XML file to a ParCoLab XML file (version 8 or 9),
 - convert a ParCoLab XML file (version 8 or 9) to a BaTelÒc XML file,
 - convert a TXT, DOC or DOCX file to a ParCoLab XML file (version 8 or 9),
 - convert a TXT, DOC or DOCX file to a BaTelÒc XML file,
 - read metatada from a CSV file (version 8 or 9),
 - write metadata to a CSV file (version 8 or 9).

How can pyteilib be used?
_____________________________

``pyteilib`` is a library written in the Python programming language. It can be used directly in the Python interpreter or imported into Python scripts.
For more information about Python, see http://www.python.org.

How to cite pyteilib?
________________________

If you are using ``pyteilib`` for non-commercial, scientific projects, please cite the library in its current state along with the version that you used:

Buret, Céline (2025): pyteilib. Python Library for Automatic Tasks in Multi-Languages Texts. Version 1.0 (Uploaded on 2025-10-12). URL: https://github.com/buret/pyteilib.

Installation
=============

Basic setup
______________

Download ``pyteilib`` repository. Please visit https://docs.github.com/fr/repositories/working-with-files/using-files/downloading-source-code-archives for more details.

Usage
____________

In order to use the library, open Python3 in your terminal and import ``pyteilib`` as follows:
::

	>>> from pyteilib import *

Dependencies
___________________

Indispensable third party libraries
++++++++++++++++++++++++++++++++++++++

Here is the list of the libraries without which ``pyteilib`` won't work.

Regex: http://pypi.python.org/pypi/regex

Recommended third party libraries
++++++++++++++++++++++++++++++++++++++++

Here is a list of the libraries without which ``pyteilib`` core functions will work, but which are anyway used quite frequently.

Docx: https://pypi.python.org/pypi/python-docx

ODF: https://pypi.python.org/pypi/odfpy

Setup for development version
__________________________________

Prerequisite
+++++++++++++++

Install git.

Setup with git
++++++++++++++++++

If you want to regularly work on ``pyteilib``, open a (git) terminal and type in the following:
::

	$ git clone https://github.com/buret/pylmflib

Instructions for a basic installation on Linux and Mac
_______________________________________________________

Prerequisites on Linux and Mac
+++++++++++++++++++++++++++++++++++++++

Before being able to run ``pyteilib``, you will need to follow these steps:

1. git
::

	$ sudo apt-get install git
	$ git clone https://github.com/buret/pyteilib pyteilib

2. setuptools
::

	$ wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python

3. python-docx

Download ``python-docx-0.8.5.tar.gz`` : https://pypi.python.org/pypi/python-docx
::

	$ tar xvzf python-docx-0.8.5.tar.gz
	$ cd python-docx-0.8.5/
	$ sudo python setup.py install

4. xsltproc
::

	$ sudo apt-get install xsltproc

pylmflib installation on Linux and Mac
+++++++++++++++++++++++++++++++++++++++++++++++++++++

We recommend to use the stable version of ``pyteilib`` (1.0). Make sure that ``regex`` is installed on you system prior to installing ``pyteilib``. In order to install this version, simply download it from https://github.com/buret/pyteilib, unpack the directory, then ``cd`` into it, and type in the prompt:
::

	$ python setup.py install

You may need sudo-rights to carry out these command.

At this stage, you can run the tests:
::

	$ python test/scenario1.py

And you could run all provided examples:
::

	$ user/...

Workarounds
___________________

To use the library without installing it, i.e. without running the setup-command, a simple way to use ``pyteilib`` is to include it in your sys-path just before you call the library:
::

	>>> import sys
	>>> sys.path.append("path_to_pyteilib)

Code
======

Source code is available at: https://github.com/buret/pyteilib

``pyteilib`` has been developed in Python 3.12.7.

It is under GPL licence.

Basic modules
_____________________

The library in its current state consists of the following modules:
 * reader
 * tei
 * transformer
 * writer
 * utils

Basic formats
____________________

In the following, we list some of the formats that are frequently used by ``pyteilib``, be it that they are taken as input formats, or that they are produced as output from the classes and methods provided by ``pyteilib``:

* TXT
* XML TEI
* CSV

Here is a list of formats that can be used, but need to be further developed, i.e. integration has been done but implementation has to be completed:

* DOC
* DOCX
* ODT

Formats that have to be added to the library in the future:

* XLS

Coding conventions
_________________________

Please respect the coding rules used in the library.

Test
======

All tests are in a directory ``test/`` within the main directory. To run the tests, just enter the main directory and call the scenarii located in ``test/`` on the command line. Please do not commit any changes without all tests running without failure or error.

Documentation
=============

If you contribute to ``pyteilib``, you should document your code.
The first step for documentation is the documentation within the code.

Currently, documentation is created using the following steps:

- Whenever code is added to ``pyteilib``, the contributors add documentation inline in their code, following the style used in the project.
- Then, they run ``Doxygen`` using the ``Doxyfile`` provided under ``doc/Doxygen``.
- The general website structure is added around the code. You can find its content by browsing the ``doc/Doxygen/html/`` directory.

Examples
==========

Workflow example
_______________________

This is an example workflow that illustrates some of the functionalities of ``pyteilib``.

Getting started
+++++++++++++++++++++++++++++

First, make sure to have the Python TEI library downloaded, extracted and installed properly. The dataset that will be used is located under ``test/``.

This folder includes a Python script that runs the whole code from the beginning to the end. In order to start the conversion, go under the main directory and run this script:
::

	$ python test/scenario1.py

As a result, the following files will appear in the output directory:

* ``example1_bto.xml``, ... ;
* ``example1_bto_hi.xml``, ... ;
* ``example1_pcl_v8.xml``, ... ;
* ``example1_pcl_v8_hi.xml``, ... ;
* ``example1_pcl_v9.xml``, ... ;
* ``example1_pcl_v9_hi.xml``, ... ;
* ``example1_metadata_v8.csv``, ... ;
* ``example1_metadata_v9.csv``, ... .

You can also directly run the conversion by running ``scenario1.sh``.

Python scripts
++++++++++++++++++++++++++++++

* ``scenario1.py``

It is the main script, the one which calls ``pyteilib`` functions:

1. ``tei_read``
2. ``tei_write``
3. ``transform``
4. ``export_header``

All available output formats are generated:

 * XML BaTelÒc
 * XML ParCoLab
 * CSV

So the basic steps are:

1. to read the XML BaTelÒc file ``input/example1_bto.xml`` ;
2. to convert the XML BaTelÒc file into a structured XML format, based on TEI recommendations ;
3. to generate an output XML BaTelÒc file ;
4. to transform XML BaTelÒc into XML ParCoLab (version 8 and 9) ;
5. to generate an output XML ParCoLab file (version 8 and 9) ;
6. to export the TEI header into a CSV file (version 8 and 9).

In this script, user also has access to all ``pyteilib`` objects methods.

* ``startup.py``

This file is needed to define working path and path to the library. Normally, you should not have to modify it.

Basic example
__________________

Simple examples are presented under ``user/``.

Note that conversion scripts from different XML formats are here as examples to show what is possible to do. They have to be reworked to generate needed outputs.

Tutorial
==========

Library options
______________________

The library provides several options. There are all described in the help menu, that you can display by running for instance:
::

	$ python test/scenario1.py -h

Execution errors
______________________

Any error will raise a Python exception, giving some details about the cause.

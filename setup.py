#! /usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import pyteilib

setup(name='pyteilib',
    version=pyteilib.wrapper.__version__,
    description='Python TEI library',
    long_description=open('README.rst').read(),
    author='Céline Buret',
    author_email='buret.celine@gmail.com',
    #install_requires=["docx", "odf"],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'Intended Audience :: End Users/Desktop',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.12.7',
                 'Topic :: Scientific/Engineering'],
    url='https://github.com/buret/pyteilib',
    py_modules=['pyteilib.wrapper'],
    package_dir={'' : '.'},
    packages=['pyteilib', 'pyteilib.reader', 'pyteilib.tei', 'pyteilib.transformer', 'pyteilib.utils', 'pyteilib.writer'],
    package_data={},
    data_files=[],
    scripts=[]
)

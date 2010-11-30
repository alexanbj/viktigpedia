##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""RML to PDF Converter

$Id: rml2pdf.py 74160 2007-04-15 22:04:24Z srichter $
"""
__docformat__ = "reStructuredText"
import cStringIO
import os
import sys
import zope.interface
from lxml import etree
from z3c.rml import document, interfaces

zope.interface.moduleProvides(interfaces.IRML2PDF)


def parseString(xml, removeEncodingLine=True, filename=None):
    if isinstance(xml, unicode) and removeEncodingLine:
        # RML is a unicode string, but oftentimes documents declare their
        # encoding using <?xml ...>. Unfortuantely, I cannot tell lxml to
        # ignore that directive. Thus we remove it.
        if xml.startswith('<?xml'):
            xml = xml.split('\n', 1)[-1]
    root = etree.fromstring(xml)
    doc = document.Document(root)
    if filename:
        doc.filename = filename
    output = cStringIO.StringIO()
    doc.process(output)
    output.seek(0)
    return output


def go(xmlInput, outputFileName=None, outDir=None, dtdDir=None):
    if dtdDir is not None:
        sys.stderr.write('The ``dtdDir`` option is not yet supported.')

    # Allows both streams and filenames as input
    if isinstance(xmlInput, str):
        xmlInput = open(xmlInput, 'r')
    root = etree.parse(xmlInput).getroot()
    doc = document.Document(root)
    #doc.filename = xmlInputName

    outputFile = None

    # If an output filename is specified, create an output filepointer for it
    if outputFileName is not None and isinstance(outputFileName, str):
        if outDir is not None:
            outputFileName = os.path.join(outDir, outputFileName)
        outputFile = open(outputFileName, 'wb')

    else: outputFile = outputFileName

    # Create a Reportlab canvas by processing the document
    doc.process(outputFile)


if __name__ == '__main__':
    canvas = go(sys.argv[1])

import StringIO

from django.conf import settings

from easymode.xslt import prepare_string_param
from easymode.utils.xmlutils import XmlPrinter

def xslt_param_builder(arg):
    """
    Returns the supplied arg ready for parameter injection to the XSLT processor
    """
    stream = StringIO.StringIO()
    xml = XmlPrinter(stream, settings.DEFAULT_CHARSET)
    xml.characters(arg)

    byte_string = stream.getvalue()
    return prepare_string_param(byte_string.decode('utf-8'))

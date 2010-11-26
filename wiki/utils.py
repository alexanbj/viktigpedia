# -*- coding: utf-8 -*-

import StringIO
import re

from django.conf import settings

from easymode.xslt import prepare_string_param
from easymode.utils.xmlutils import XmlPrinter
from easymode.xslt.response import render_to_response as xslt_render_to_response

def xslt_param_builder(arg):
    """
    Returns the supplied arg ready for parameter injection to the XSLT processor
    """
    stream = StringIO.StringIO()
    xml = XmlPrinter(stream, settings.DEFAULT_CHARSET)
    xml.characters(arg)

    byte_string = stream.getvalue()
    return prepare_string_param(byte_string.decode('utf-8'))

def slugify(txt):
    """A custom version of slugify since Django's isn't very wikilinks friendly"""

    txt = txt.strip() # remove trailing whitespace
    txt = re.sub('\s*-\s*','-', txt, re.UNICODE) # remove spaces before and after dashes
    txt = re.sub('[\s/]', '_', txt, re.UNICODE) # replace remaining spaces with underscores
    txt = re.sub('(\d):(\d)', r'\1-\2', txt, re.UNICODE) # replace colons between numbers with dashes
    txt = re.sub('"', "'", txt, re.UNICODE) # replace double quotes with single quotes
    txt = re.sub(r'[?,:!@#~`+=$%^&\\*()\[\]{}<>]','',txt, re.UNICODE) # remove some characters altogether
    return txt

def split_keywords(query):
    """Split a query into keywords. Supports double quoted words as a single
    keyword."""

    keywords = []

    while '"' in query:
        first = query.find('"')
        second = query.find('"', first + 1)
        quoted = query[first:second + 1]
        keywords.append(quoted.strip('"'))
        query = query.replace(quoted, ' ')

    keywords.extend(query.split())
    return keywords

def render_to_response(request, template, object, params=None):
    """Wrapper function for rendering correct template based on mobile user
    agent or not."""

    if request.mobile:
        template = settings.MOBILE_TEMPLATE_PREFIX + '/' + template
        print template
    return xslt_render_to_response(template, object, params)

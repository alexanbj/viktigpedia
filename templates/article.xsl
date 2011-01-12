<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output encoding="UTF-8" indent="yes" method="xml"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
    doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="django-objects/object">
<html xmlns="http://www.w3.org/1999/xhtml"> 
  <head>
    <title><xsl:value-of select="field[@name='title']"/> - Viktigpedia</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" href="/media/css/screen.css" type="text/css" />
    <link rel="stylesheet" href="/media/css/viktigpedia.css" type="text/css" />
    <link href='http://fonts.googleapis.com/css?family=Crimson+Text' rel='stylesheet' type='text/css' />

    <link rel="alternate" type="application/rss+xml" title="RSS" href="/feed/" />


    <!-- Using jQuery to move the table of contents generated by markdown to
         the proper location -->
    <script type="text/javascript" src="/media/js/jquery-1.4.4.min.js"></script>
    <script type="text/javascript">
      $(document).ready(function() {
        $('#sidebarmenu').append($('div.pagecontent div.toc'));
      });
    </script>
  </head>

  <body>
    <div class="container">
      <div id="top" class="span-24">
        <div class="menu">
          <ul>
            <li><a href="{$editurl}" title="You can edit this page.">Edit</a></li>
            <li><a href="pdf" title="Download as PDF.">PDF</a></li>
            <li><a href="/" title="Home">Home</a></li>
          </ul>
        </div>
      </div>

      <!-- Hack since empty divs aren't allowed and will ruin layout -->
      <div id="contenttop" class="span-24">&#160;</div>

        <div id="contentwrapper" class="span-24">
          <div id="header" class="span-22 prepend-1 append-1">
            <div id="title" class="span-15">
              <h1>ViktigpediA</h1>
            </div>
            <div id="searchwrapper" class="span-5 append-1 last">
              <form action="/search/" method="post">
                <input type="text" class="searchbox" name="query"/>
                <input type="image" src="/media/img/searchbox_submit.png" class="searchbox_submit" alt="Search" name="search"/>
              </form>
            </div>
          </div>

          <div id="main" class="span-16 prepend-1">

            <div class="page">
              <div class="pagetitle">
                <h2><xsl:value-of select="field[@name='title']"/></h2>
              </div>

              <div class="pagecontent">
                <xsl:value-of select="field[@name='rendered']" disable-output-escaping="yes" />
              </div>
            </div>
          </div>

          <div id="sidebar" class="span-6 append-1 last">
            <div id="wrapbox">
              <div id="sidebarmenu" class="section">
                <h3>Contents</h3>
                <!-- jQuery populates this one -->
              </div>
            </div>
          </div>
        </div>

        <div id="footer" class="span-24 prepend-1">
          This page was last modified <xsl:value-of select="field[@name='last_update']"/>
        </div>
      </div>
   </body>
</html>
</xsl:template>
</xsl:stylesheet>

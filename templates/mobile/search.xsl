<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output encoding="UTF-8" indent="yes" method="xml"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
    doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="django-objects">
<html dir='tr' lang='en' xml:lang='en' xmlns="http://www.w3.org/1999/xhtml"> 
  <head>
    <title>Viktigpedia</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;" />
    <link rel="stylesheet" href="/media/css/mobile.css" type="text/css" />
  </head>

  <body>
    <div id="wrapper">
      <div id="innerwrapper">

        <div id="header">
          <div id="searchwrapper">
            <form action="/search/" method="post">
              <label for="id_search" id="search_label">Search</label>
              <input type="text" class="searchbox" name="query" id="id_search"/>
              <input type="image" src="/media/img/search.png" class="searchbox_submit" alt="Search" name="search"/>
            </form>
            <div id="nav">
              <form method="get" action="/"><button type="submit">Home</button></form>
            </div>
          </div>
        </div>
        <h1 id="headline">Search results</h1>
        <div id="content">
          <ul>
            <xsl:for-each select="object">
              <li><a href="/wiki/{field[@name='slug']}"><xsl:value-of select="field[@name='title']"/></a></li>
            </xsl:for-each>
          </ul>
        </div>

        <div id="footer">
          <a href="http://localhost:8000">View this page on regular Viktigpedia</a><br />
          Will disable mobile site for the rest of this session.
        </div>
      </div> <!-- end innerwrapper -->
    </div> <!-- end wrapper -->
 </body>
</html>
</xsl:template>
</xsl:stylesheet>

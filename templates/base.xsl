<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output encoding="UTF-8" indent="yes" method="xml"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
    doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="/django-objects">
<html xmlns="http://www.w3.org/1999/xhtml"> 
  <head>
    <title>Viktigpedia</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" href="/media/css/screen.css" type="text/css" />
    <link rel="stylesheet" href="/media/css/viktigpedia.css" type="text/css" />
    <link href='http://fonts.googleapis.com/css?family=Crimson+Text' rel='stylesheet' type='text/css' />

    <link rel="alternate" type="application/rss+xml" title="RSS" href="/feed/" />
  </head>

  <body>
    <div class="container">
      <div id="top" class="span-24">
        <div class="menu">
          <ul>
            <li><a href="/" title="Home">Home</a></li>
          </ul>
        </div>
      </div>

      <!-- Hack since empty divs aren't allowed and will ruin layout -->
      <div id="contenttop" class="span-24">&#160;</div>

        <div id="contentwrapper" class="span-24">
          <div id="header" class="span-22 prepend-1 append-1">
            <div id="title" class="span-15">
              <a href="/"><h1>ViktigpediA</h1></a>
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
                <h1>Welcome to Viktigpedia!</h1>
              </div>

              <div class="pagecontent">
              <p>
                Welcome to Viktigpedia!
                You can start navigating this page by viewing one of the latest
                articles added in the menu to the right, or by using the search
                functionality.
                </p>

                <p>
                Viktigpedia is the end result of a project in the course <a href="http://www.hedin.mobi/TNM065/">TNM065
                Document Structures</a> at <a href="http://www.liu.se">Linköping University.</a>
                The code is open source and is available at <a
                href="https://github.com/alexanbj/viktigpedia">GitHub.</a>
                </p>

                This website is written in Python using the Django web framework.
              </div>
            </div>
          </div>

          <div id="sidebar" class="span-6 append-1 last">
            <div id="wrapbox">
              <div id="sidebarmenu" class="section">
                <h3>Latest articles</h3>
                <ul>
                  <xsl:for-each select="object">
                    <li><a href="/wiki/{field[@name='slug']}"><xsl:value-of select="field[@name='title']"/></a></li>
                  </xsl:for-each>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div id="footer" class="span-24 prepend-1">
          Powered by Django
        </div>
      </div>
   </body>
</html>
</xsl:template>
</xsl:stylesheet>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output encoding="UTF-8" indent="yes" method="xml"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
    doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="django-objects/object">
<html xmlns="http://www.w3.org/1999/xhtml"> 
  <head>
    <title>Editing <xsl:value-of select="field[@name='title']"/> - Viktigpedia</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" href="/media/css/screen.css" type="text/css" />
    <link rel="stylesheet" href="/media/css/viktigpedia.css" type="text/css" />
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
              <a href="/"><img src="/media/img/logo.png"/></a>
            </div>
            <div id="login" class="span-5 append-1 last">
              <a href="url django.contrib.auth.views.logout_then_login">Logout</a>
            </div>
          </div>

          <div id="main" class="span-16 prepend-1">

            <div class="page">
              <div class="pagetitle">
                <h2>Editing <xsl:value-of select="field[@name='title']"/></h2>
              </div>

              <div class="pagecontent">
                 <form method="post">
                  <input type="text" name="title" value="{field[@name='title']}" />
                  <textarea name="content">
                    <xsl:value-of select="field[@name='content']" />
                  </textarea>
                  <input type="submit" value="Save page" title="Save your changes" />
                 </form>
              </div>
            </div>
          </div>

          <div id="sidebar" class="span-6 append-1 last">
            <div id="wrapbox">
              <div id="sidebarmenu" class="section">
                <h3>Contents</h3>
                <ul>
                  <li><a href="/" title="Home">Home</a></li>
                  <li><a href="/" title="Empty">Empty</a></li>
                  <li><a href="/" title="Empty">Empty</a></li>
                </ul>
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

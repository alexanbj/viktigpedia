<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output encoding="UTF-8" indent="yes" method="xml"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
    doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<!-- Hacking tiem!
  Referring to a parameter when it does not exist creates errors in the
  template. By declaring it as a global empty parameter we can bypass this and
  perform an exists check on it using the xsl:choose element. 
-->
<xsl:param name="locked"/>

<xsl:template match="django-objects/object">
<html xmlns="http://www.w3.org/1999/xhtml"> 
  <head>
    <title>Editing <xsl:value-of select="field[@name='title']"/> - Viktigpedia</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" href="/media/css/screen.css" type="text/css" />
    <link rel="stylesheet" href="/media/css/viktigpedia.css" type="text/css" />
    <link href='http://fonts.googleapis.com/css?family=Crimson+Text' rel='stylesheet' type='text/css' />

    <link rel="alternate" type="application/rss+xml" title="RSS" href="/feed/" />


    <xsl:choose>
      <xsl:when test="not($locked)">
      </xsl:when>
      <xsl:otherwise>
    <script type="text/javascript" src="/media/js/jquery-1.4.4.min.js"></script>
    <script type="text/javascript" src="/media/js/easy.notification.js"></script>
    <script type="text/javascript">
        $(function(){
            $.easyNotification({
                parent: '.pagecontent',
                text: "Possible conflict! Another user started editing at <xsl:value-of select='$lock_created'/>"
            });
        });
    </script>
      </xsl:otherwise>
    </xsl:choose>
  </head>

  <body>
    <div class="container">
      <div id="top" class="span-24">
        <div class="menu">
          <ul>
            <li><a href="{$viewurl}">View</a></li>
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
                <h1>Editing <xsl:value-of select="field[@name='title']"/></h1>
              </div>

              <div class="pagecontent" id="pagecontentt">
                 <form method="post">
                  <p>
                  Title: <input type="text" name="title" value="{field[@name='title']}" />
                  </p>
                  Content:
                  <br />
                  <textarea name="content" rows="10" cols="40">
                    <xsl:value-of select="field[@name='content']" />
                  </textarea>
                  <br />
                  <input type="submit" value="Save page" title="Save your changes" />
                  <a href="{$viewurl}" style="float: right">Cancel</a>
                 </form>
              </div>
            </div>
          </div>

          <div id="sidebar" class="span-6 append-1 last">
            <div id="wrapbox">
              <div id="sidebarmenu" class="section">
                <h3>Editing</h3>
                <p>
                See <a href="http://daringfireball.net/projects/markdown/syntax">Daring Fireball</a> for a reference on how
                to use Markdown.
                </p>

                Please remember to include '[TOC]' in the content to properly
                generate a table of contents for the article.
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

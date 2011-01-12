<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output encoding="UTF-8" indent="yes" method="xml"
    doctype-system="rml.dtd" />

<xsl:template match="article">

<document filename="example_01.pdf">

  <template showBoundary="0"> <!-- For debugging, set to 1, shows outlines of frames -->

  <!--this section contains elements of the document -->
  <!--which are FIXED into position. -->
    
    <pageTemplate id="frontpage">
      <pageGraphics>
        <setFont name="Times-Roman" size="48"/>
        <drawString x="65" y="700"><xsl:value-of select="/article/title"/></drawString>
        <lineMode width="1"/>
          <!--<lines> 50 800 545 800</lines>-->
          <lines> 50 40 545 40</lines>
        <lineMode width="1"/>
      <setFont name="Times-Roman" size="8"/>
        <drawCenteredString x="300" y="25">
          PDF generated using the open source z3c.RML implementation and the ReportLab Toolkit.
        </drawCenteredString>
        <drawCenteredString x="300" y="12.5">
          PDF generated at: <xsl:value-of select="$timestamp"/> <pageNumber/>
        </drawCenteredString>
      </pageGraphics>
      
      <!-- Dummy frame of size 0, so frontpage compiles -->
      <frame id="dummy" x1="50" y1="340" width="0" height="0"/>
    </pageTemplate>

    <pageTemplate id="main">
      <pageGraphics>
        <setFont name="Times-Roman" size="8"/>
        <drawString x="50" y="805"><xsl:value-of select="/article/title"/></drawString>
        <lineMode width="1"/>
          <lines> 50 800 545 800</lines>
          <lines> 50 40 545 40</lines>
        <lineMode width="1"/>
        <setFont name="Times-Roman" size="24"/>
        <drawString x="100" y="700">
          <xsl:value-of select="field[@name='title']"/>
        </drawString>
      </pageGraphics>
      <frame id="content" x1="65" y1="75" width="465" height="700"/>
    </pageTemplate>
  </template>

  <stylesheet>
    <!--this section contains the STYLE information for the document
    -->

    <paraStyle name="normal" spaceAfter="10"/>
  </stylesheet>

  <story firstPageTemplate="frontpage">

    <!--this section contains the FLOWABLE elements of the -->
    <!--document. These elements will fill up the frames -->
    <!--defined in the <template> section above.
    -->

    <!-- We don't want content on our frontpage -->
    <setNextTemplate name="main"/>
    
    <xsl:apply-templates select="content/*" />

  </story>
</document>
</xsl:template>

<xsl:template match="p">
  <para style="normal">
    <xsl:apply-templates/>
  </para>
</xsl:template>

<xsl:template match="h1">
  <h1>
    <xsl:value-of select="."/>
  </h1>
</xsl:template>

<xsl:template match="h2">
  <h2>
    <xsl:value-of select="."/>
  </h2>
</xsl:template>

<xsl:template match="h3|h4|h5">
  <h3>
    <xsl:value-of select="."/>
  </h3>
</xsl:template>

<xsl:template match="strong">
  <b><xsl:value-of select="node()"/></b>
</xsl:template>

<xsl:template match="em">
  <i><xsl:value-of select="node()"/></i>
</xsl:template>

<xsl:template match="*">
  <xsl:value-of select="."/>
</xsl:template>

</xsl:stylesheet>

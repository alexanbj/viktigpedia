<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output encoding="UTF-8" indent="yes" method="xml"
    doctype-system="rml.dtd" />

<xsl:template match="django-objects/object">

  <document filename="example_01.pdf">
    <template>
    <!--this section contains elements of the document -->
    <!--which are FIXED into position. -->
      <pageTemplate id="main">
        <frame id="first" x1="100" y1="400" width="150" height="200"/>
      </pageTemplate>
    </template>

    <stylesheet>
      <!--this section contains the STYLE information for
      -->
      <!--the document, but there isn't any yet. The tags still
      -->
      <!--have to be present, however, or the document won't compile.-->
    </stylesheet>

    <story>
      <!--this section contains the FLOWABLE elements of the -->
      <!--document. These elements will fill up the frames -->
      <!--defined in the <template> section above.
      -->

      <para>
        Welcome to RML!
      </para>
      <para>
        This is the "story". This is the part of the RML document where
        your text is placed.
      </para>
      <para>
        It should be enclosed in "para" and "/para" tags to turn it into
        paragraphs.
      </para>
    </story>
  </document>
</xsl:template>
</xsl:stylesheet>

<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output encoding="UTF-8" indent="yes" method="xml" />

  <!-- Parse the root node of the serialized xml -->
  <xsl:template match="django-objects/object">
    <article>
      <title><xsl:value-of select="field[@name='title']"/></title>
      <content><xsl:value-of select="field[@name='rendered']" disable-output-escaping="yes" /></content>
    </article>
  </xsl:template>

</xsl:stylesheet>

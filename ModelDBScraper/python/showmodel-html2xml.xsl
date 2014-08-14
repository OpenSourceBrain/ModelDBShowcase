<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!-- XSL to transform http://senselab.med.yale.edu/ModelDB/ShowModel.asp page into XML -->
<!-- Author: Suresh Jois dasneuro [at] gmail.com  http://www.opensourcebrain.org/users/361 -->

<!-- NOTE: This XSL handles all of ShowModel.asp's HTML, EXCEPT the Model Files section. See comment at end of this file re. the model files section-->

<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="no" />

<xsl:template match="/">

<modeldb-showmodel xmlns="http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=45539">
<!-- Neither ModelDB nor any of its ASP pages have a *canonical* XML namespace definition page. So above is a *nominal* xmlns for showmodel.asp using a typical model page -->

  <modelid>
    <xsl:value-of select="//*[@id='modelid']"/>
  </modelid>  
  <modelname>
    <xsl:value-of select="//*[@id='modelname']"/>
  </modelname>

<!-- NOTE: Ideally, all XPaths in this XSL should select off semantic info like element ids of the incoming HTML. However, some elements like the below, which enclose important model info, do not have IDs. Hence the need for page-structure or page-text based absolute XPATH select. Many more situations like this further below. Due to these, this XSL will break if Showmodel.asp page layout changes. -->

  <modelintro>
    <xsl:value-of select="//table[@id='Table1']/descendant::tr[3]/td/text()"/>
  </modelintro>
  
  <modelreferencelist>
  <xsl:for-each select="//*[@id='reference']">
    <reference>
      <title>
	<xsl:value-of select="text()"/>
      </title>
      <xsl:for-each select="descendant::a">
      <source>
	<name>
	  <xsl:value-of select="text()"/>
	</name>
	<url>
	  <xsl:value-of select="attribute::href"/>
	</url>
      </source>
      </xsl:for-each>
    </reference>
  </xsl:for-each>
  </modelreferencelist>
  
  <modelcitationpage>
    <text>
      <xsl:value-of select="//a[text()='Citation Browser']/text()"/>
    </text>
    <url>
      <xsl:value-of select="//a[text()='Citation Browser']/@href"/>
    </url>
  </modelcitationpage>

  <modelinformation>
    <xsl:for-each select="//*[@id='Table2']/descendant::td[@id]">
    <category>
      <name>
	<xsl:value-of select="../td[1]/text()"/>
      </name>
      <idtext>
	<xsl:value-of select="@id"/>
      </idtext>
      <xsl:for-each select="a">
      <subcategory>
	<name>
	  <xsl:value-of select="text()"/>
	</name>
	<url>
	  <xsl:value-of select="@href"/>
	</url>
      </subcategory>
      </xsl:for-each>
    </category>      
    </xsl:for-each>
  </modelinformation>
  
  <modelmoreinformation>
    <xsl:for-each select="//table[@id='Table1']/descendant::td[child::strong[text()='Search NeuronDB ']]/a">
    <category>
      <name>
	<xsl:value-of select="text()"/>
      </name>
      <url>
	<xsl:value-of select="@href"/>
      </url>
    </category>
    </xsl:for-each>
  </modelmoreinformation>
  
  <modelsimulationenv>
    <xsl:value-of select="//*[@id='sel1']/option[@selected]/text()"/>    
  </modelsimulationenv>
  
  <modelsimulationenvvariants>
    <xsl:for-each select="//*[@id='sel1']/option[count(@selected)=0]">
    <variant>
      <name>
        <xsl:value-of select="text()"/>
      </name>
      <modelid>
        <xsl:value-of select="@value"/>
      </modelid>
    </variant>
    </xsl:for-each>
  </modelsimulationenvvariants>
  
  <modelfiledownloadoptions>
    <xsl:for-each select="//table[@id='Table3']/descendant::span[@id='buttons']/a[@id and @href]">
    <option>
      <name>
        <xsl:value-of select="text()"/>
      </name>
      <idtext>
        <xsl:value-of select="@id"/>
      </idtext>
      <url>
        <xsl:value-of select="@href"/>
      </url>
    </option>
    </xsl:for-each>    
  </modelfiledownloadoptions>
  
<!-- NOTE: On model pages rendered by ShowModel.asp, the above Download Options section is followed by a Model Files section that lists the model's folders, files and file contents. However, the model's entire file-set is available as a single zip in the download options section. So as of now the files listing will not be parsed by this XSL. -->

</modeldb-showmodel>
</xsl:template>
</xsl:stylesheet>
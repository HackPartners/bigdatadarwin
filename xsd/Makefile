all: links
	xsltproc --stringparam searchImportedSchemas true --stringparam searchIncludedSchemas true --stringparam linksFile links.xml xs3p.xsl rtti*.xsd > doc.html

links: links.xml
	xsltproc -o links.xml xs3p_links.xsl rttiPPTSchema_v12.xsd

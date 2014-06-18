# Python Class to transform an HTML page into an XML file using XSL transformation
# Accepts inputs: A web page URL, corresponding XSL as string
# Performs the transformation using LXML's XSLT function
# Returns the original html cleaned up, and/or the html transformed to XML as string. 
# Author: Suresh Jois Email: dasneuro [at] gmail.com http://www.opensourcebrain.org/users/361

from lxml import etree, html

#---------------------------------------------------------

class HTML2XML:

  _xml_str = ""
  _xml_tree = None

  _clean_html_str = ""
  _html_with_xml_header_str = ""
  _html_with_xml_header_tree = None
  _html_tree = None
  _html_tree_root = None

  _xsl_tree = None


  def __init__(self, html_url, xsl_str):
    xsl_transformer = etree.XSLT(etree.XML(xsl_str))
        
    self._html_tree = html.parse(html_url)
    self._html_tree.getroot().make_links_absolute()
    self._clean_html_str = etree.tostring(self._html_tree, pretty_print=True, method="xml")
    
    self._html_with_xml_header_str = '<?xml version="1.0"?>'+self._clean_html_str
    self._html_with_xml_header_tree = etree.XML(self._html_with_xml_header_str)
    
    self._xml_tree = xsl_transformer(self._html_with_xml_header_tree)
    self._xml_str = str(self._xml_tree)
  
  def get_xml(self):
    return(self._xml_str)        


  def get_clean_html(self):
    return(self._clean_html_str)
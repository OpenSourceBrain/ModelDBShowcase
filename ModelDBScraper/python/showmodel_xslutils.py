# Python Class to transform an HTML page into an XML file using XSL transformation
# Accepts inputs: A web page URL, corresponding XSL as string
# Performs the transformation using LXML's XSLT function
# Can Return: 
# The original html cleaned up, 
# The html transformed to XML as string.
# A Python object representing the XML heirarchy of the model
# that can be accessed in the usual pattern object.attribute[index_if_list].nested_attribute ...
#
# Author: Suresh Jois Email: dasneuro [at] gmail.com
#  http://www.opensourcebrain.org/users/361 or http://www.ojasi.org


from lxml import etree, html, objectify
import inspect

#---------------------------------------------------------

class Xform:

  _xml_str = ""
  _xml_tree = None

  _xml_pyobject = None
  _xml_pyclasssource = None

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
        
    self._xml_pyobject = objectify.XML(self._xml_str)
    objectify.deannotate(self._xml_pyobject)
    # print(objectify.dump(self._xml_pyobject))    
    
  def get_clean_html(self):
    return(self._clean_html_str)
    
  def get_xml_str(self):
    return(self._xml_str)

  def get_xml_tree(self):
    return(self._xml_tree)
    
  def get_xml_pyobject(self):
    return(self._xml_pyobject)
    
  def get_xml_pyclasssource(self):
    return(self._xml_pyclasssource)
    
    
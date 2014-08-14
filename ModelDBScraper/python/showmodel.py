#---------------------------------------------------------

# Python Script to web-scrape model pages in the Computational Neuroscience models repository ModelDB http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=<valid_model_id>

# Author: Suresh Jois dasneuro [at] gmail.com 
#  http://www.opensourcebrain.org/users/361 or http://www.ojasi.org

# Usage:  python showmodel.py <valid_modeldb_model_id>
#
# It accepts a ModelDB model_id as command line argument
# Gets the HTML from the corresponding model page URL
# Gets the XSL from showmodel_html2xml.xsl
# Calls showmodel_xslutils to apply the XSL transform using the lxml package
# showmodel_xslutils can return the result XMl as string or as a Python object that can be accessed in the usual pattern object.attribute[index_if_list].nested_attribute ...
# Either of the above can be printed, or written to an XML database, etc.

#---------------------------------------------------------

import os
import sys
sys.path.append(os.getcwd())
import showmodel_xslutils

#---------------------------------------------------------

# CONSTANTS

# Base URL of ModelDB's ShowModel.asp
showmodel_base_url = "http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model="

#---------------------------------------------------------

# Get model id from command line

modelid = str(sys.argv[1])

#---------------------------------------------------------

# Get the xsl
with open ("showmodel-html2xml.xsl", "r") as xsl_file:
  xsl_string=xsl_file.read()
  
# Instantiate the transformer

xform = showmodel_xslutils.Xform(showmodel_base_url+modelid, xsl_string)

# Get a cleaned up XHTML string of the original HTML
# print(xform.get_clean_html())


# Get the XML as string
xml_string = xform.get_xml_str()

# Print the entire XML
print(xml_string)

# Get a Python-esque object representing the XMl
xml_pyobject = xform.get_xml_pyobject()

# This can be used in the Python-esque object.attribute[index_if_list].nested_attribute ... pattern
# Print some sample information in the XML

print(xml_pyobject.modelreferencelist.reference[0].source[1].name)
print(xml_pyobject.modelreferencelist.reference[0].source[1].url)

print(xml_pyobject.modelinformation.category[0].name)
print(xml_pyobject.modelinformation.category[1].subcategory[0].name)
print(xml_pyobject.modelinformation.category[1].subcategory[0].url)


#---------------------------------------------------------
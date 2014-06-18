#---------------------------------------------------------

# Python Script to web-scrape model pages in the Computational Neuroscience models repository ModelDB http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=<valid_model_id>

# Author: Suresh Jois dasneuro [at] gmail.com http://www.opensourcebrain.org/users/361

# Usage:  python showmodel.py <valid_modeldb_model_id>
#
# It accepts a ModelDB model_id as command line argument
# Gets the HTML from the corresponding model page URL
# Gets the XSL from showmodel.xsl
# Calls HTML2XML to apply the XSL transform using the lxml package
# Prints the resulting XML string to stdout

#---------------------------------------------------------

import os
import sys
sys.path.append(os.getcwd())
import html2xml

#---------------------------------------------------------

# CONSTANTS

# Base URL of ModelDB's ShowModel.asp
showmodel_base_url = "http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model="

#---------------------------------------------------------

# Get model id from command line

modelid = str(sys.argv[1])

#---------------------------------------------------------

# Get the xsl
with open ("showmodel.xsl", "r") as xsl_file:
  xsl_string=xsl_file.read()
  
# Instantiate the transformer

xform = html2xml.HTML2XML(showmodel_base_url+modelid, xsl_string)

# Produce the XML
xml_string = xform.get_xml()

#print(xform.get_clean_html())

print(xml_string)

#---------------------------------------------------------
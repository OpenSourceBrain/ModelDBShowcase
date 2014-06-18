showmodel.py

Python Script to web-scrape model pages in the Computational Neuroscience models repository ModelDB http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=<valid_model_id>

Author: Suresh Jois dasneuro [at] gmail.com http://www.opensourcebrain.org/users/361

*  The script accepts a ModelDB model_id as command line argument
*  Gets the HTML from the corresponding model page URL
*  Gets the XSL from ShowModel.xsl
*  Calls HTML2XML to apply the XSL transform using the lxml package
*  Prints the resulting XML string to stdout

Installation:

*  pip or easy_install the python package lxml
*  Copy the files showmodel.py and showmodel.xsl into a folder

Usage:  python showmodel.py <valid_modeldb_model_id>


NOTES:

*  Currently works when spot-checked against a few model pages. 
*  Still under development and testing. 
*  Not prettified (with exception handling etc.)
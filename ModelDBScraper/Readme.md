showmodel.py

Python Script to web-scrape model pages in the Computational Neuroscience models repository ModelDB (Example page http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=45539)

Author: Suresh Jois dasneuro [at] gmail.com 
  http://www.opensourcebrain.org/users/361  or http://www.ojasi.org

*  It accepts a ModelDB model_id as command line argument
*  Gets the HTML from the corresponding model page URL
*  Gets the XSL from showmodel-html2xml.xsl
*  Calls showmodel_xslutils to apply the XSL transform using the lxml package
*  showmodel_xslutils can return the result XMl as string or as a Python object that can be accessed in the usual pattern object.attribute[index_if_list].nested_attribute ...
*  Either of the above can be printed, or written to an XML/NoSQL database, etc.

Installation:

*  pip or easy_install the python package lxml
*  Put files (python/) showmodel.py, showmodel_xslutils.py and showmodel-html2xml.xsl into (the same local) folder

Usage:  python showmodel.py <valid_modeldb_model_id>


NOTES:

*  Currently works when spot-checked against a few model pages. 
*  Still under development and testing. 
*  Not prettified (with exception handling etc.)
*  Currently it does not scrape the individual model files, since they are all available via the zip download link.
*  The output XML contains model page's section headers and URLs therein, NOT the actual contents of the pages or files pointed to by the URLs. Of course the script can be easily modified to download actual contents.
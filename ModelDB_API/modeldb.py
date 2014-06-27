import utils

from bs4 import BeautifulSoup


show_entry_base_url = "http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=%s"

def get_entry(id):
    
    contents = utils.get_page(show_entry_base_url%id)
    
    soup = BeautifulSoup(contents)
    
    print soup.title.string
    
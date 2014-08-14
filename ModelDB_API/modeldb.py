import utils
from entry import Entry

from bs4 import BeautifulSoup


show_entry_base_url = "http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=%s"

def get_entry(id):
    
    contents = utils.get_page(show_entry_base_url%id)
    
    soup = BeautifulSoup(contents)
    
    
    for th in soup.find_all('th'):
        if th.has_attr('id') and th['id'] == "modelname":
            entry = Entry(id, th.string)
    
    return entry
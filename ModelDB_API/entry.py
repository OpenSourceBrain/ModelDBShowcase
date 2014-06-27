
class Entry():
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __str__(self):
        return "ModelDB entry: %s\n%s"%(self.id, self.name)
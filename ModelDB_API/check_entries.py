## Example file using API

import modeldb

ids = [45539, 127996, 39948]

for id in ids:
    
    entry = modeldb.get_entry(id)
    print("----------")
    print(entry)



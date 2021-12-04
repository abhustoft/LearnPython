import pandas as pd
import os
from pathlib import Path
from columnNameToIndex import column_to_number
import string

# def getDNColumnsString():
#     p = Path(os.getcwd() + "/Importfiles/from-supplier/" + "column-map-datanova.json")

#     # read and fix the file
#     with p.open('r+') as f:
#         file = f.read()  # reads the file in as a long string
#         file = '[' + file + ']'  # adds brackets to the start and end of the string

#     newmap = pd.read_json(file)
#     print("Mpping:")
#     print(newmap)
#     framestring = newmap.to_string(header=False,index=False,index_names=False).split('\n')
#     print("som string:")
#     print(framestring)

#     vals = [','.join(ele.split()) for ele in framestring]
#     columns = ' '.join(vals)
#     return columns

def getDNColumns():
    p = Path(os.getcwd() + "/Importfiles/from-supplier/" + "column-map-datanova.json")

    # read and fix the file
    with p.open('r+') as f:
        file = f.read()  # reads the file in as a long string
        file = '[' + file + ']'  # adds brackets to the start and end of the string

    DNcolumns = pd.read_json(file)

    for name, values in DNcolumns.iteritems():
        index = column_to_number(values[0])
        DNcolumns[name] = index

    return DNcolumns

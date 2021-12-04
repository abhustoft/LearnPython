import pandas as pd
import os
from mappings import getDNColumns
from fileUtils import get_files
from columnNameToIndex import column_to_number

DNcolumns = getDNColumns()
csvFiles, excelFiles = get_files()
#print(csvFiles)
#print(excelFiles)

#junior = pd.read_excel(os.getcwd() + "/Importfiles/from-supplier/" + "junior.xlsx", dtype={'EAN/UPC': str}, usecols=columns)
#junior = pd.read_excel(os.getcwd() + "/Importfiles/from-supplier/" + "junior.xlsx", usecols=columns)

def nye(oldColumnName):   
    if oldColumnName in DNcolumns:
        return "noe nytt"
    else:
        return oldColumnName

print("  ")
print("I hoved: skriver ut kolonnemapping")
for name, values in DNcolumns.iteritems():
    print('{name}: {value}'.format(name=name, value=values[0]))

print("  ")
print("Looper csv fil:")

for csvFile in csvFiles:
    print("Reading ",csvFile)
    csvDF = pd.read_csv(os.getcwd() + "/Importfiles/from-supplier/" + csvFile, delimiter=";")

    print("  ")
    # The columns in the csv file
    for ind, column in enumerate(csvDF.columns):
        print(ind, column)

    csvDF.rename(columns={"Payer": "x"}, inplace=True)
    csvDF.rename(mapper=nye, axis=1, inplace=True)

# for excelFile in excelFiles:
#     print("Reading ",excelFile)
#     excelDF = pd.read_excel(os.getcwd() + "/Importfiles/from-supplier/" + excelFile)

print('Read csv:')
print(csvDF.head())
# print(excelDF.info())
# print(csvDF.head())
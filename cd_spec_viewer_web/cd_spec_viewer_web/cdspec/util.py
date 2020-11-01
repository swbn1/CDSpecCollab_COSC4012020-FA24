import csv
from enum import Enum
from itertools import islice

class Units(str, Enum):
    XUNIT = "NANOMETERS"
    VOLTAGE = "HT [V]"
    ABSORBANCE = "ABSORBANCE"
    DEGREES = "CD [mdeg]"

def handle_file_upload(f):
    input = f.read().decode("utf-8") 
    reader = csv.reader(input.splitlines(), dialect='excel')
    
    headerdict = {}
    header_count = 0
    for rows in reader:
        # print(rows)
        if rows[0]  == "XYDATA":
            break
        header_count+=1
        headerdict[rows[0]] = rows[1]
    
    indicies = {}
    #If we are missing the XUNITS or YUNITS we cannot do any graphing and the file is invalid.
    if "XUNITS" in headerdict:
        indicies[headerdict['XUNITS']] = 0
    #else: return False
    if 'YUNITS' in headerdict:
        indicies[headerdict['YUNITS']] = 1
    #else: return False
    if "Y2UNITS" in headerdict:
        indicies[headerdict['Y2UNITS']] = 2
    if "Y3UNITS" in headerdict:
        indicies[headerdict['Y3UNITS']] = 3
    
    #Checking we have the required data points
    if not (Units.DEGREES in indicies and Units.VOLTAGE in indicies):
        return False

    data = []
    for rows in islice(reader, int(headerdict['NPOINTS'])):
        data.append(rows)
    
    extended_dict = {}
    for rows in reader:
        if rows:
            extended_dict[rows[0]] = rows[1:]
    
    return {"header" : headerdict, "data":data, "extended":extended_dict, "indicies":indicies}

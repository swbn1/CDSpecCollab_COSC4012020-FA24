import csv
from enum import Enum
from itertools import islice

#Units enum
class Units(str, Enum):
    XUNIT = "NANOMETERS"
    VOLTAGE = "HT [V]"
    ABSORBANCE = "ABSORBANCE"
    DEGREES = "CD [mdeg]"



# def molar_ellipticity_calculation(data, path_length, concentration, molecular_weight, degrees_index):
#     for array in data:
#         array.append((float(array[degrees_index])*float(concentration)*float(path_length)*10)/float(molecular_weight))
#     return data


def handle_file_upload(file):
    #Read and decode the csv, this is somewhat dangerous because if the file is
    #really large it can overwhelm memory, we can limit upload size though to preven this.
    input = file.read().decode("utf-8") 
    reader = csv.reader(input.splitlines(), dialect='excel')

    #Read all the rows until the XYDATA line into dictionary, the first column is the key, the second the definition    
    headerdict = {}
    header_count = 0
    for rows in reader:
        # print(rows)
        if rows[0]  == "XYDATA":
            break
        header_count+=1
        headerdict[rows[0]] = rows[1]
    
    #Set the indicies variables based on the headerdict.
    indicies = {}
    #If missing the XUNITS or YUNITS, cannot graph and the file is invalid.
    if "XUNITS" in headerdict:
        indicies[headerdict['XUNITS']] = 0
    if 'YUNITS' in headerdict:
        indicies[headerdict['YUNITS']] = 1
    if "Y2UNITS" in headerdict:
        indicies[headerdict['Y2UNITS']] = 2
    if "Y3UNITS" in headerdict:
        indicies[headerdict['Y3UNITS']] = 3
    
    #Checking for the required data points
    #TODO add error checking in views.py
    if not (Units.DEGREES in indicies and Units.XUNIT in indicies):
        return False

    #Use the npoints in the header to read in all our datapoints. 
    data = []
    for rows in islice(reader, int(headerdict['NPOINTS'])):
        data.append(rows)
    
    #Read the rest of the file into a dictionary, for now only temp is pertinent
    extended_dict = {}
    for rows in reader:
        if rows:
            extended_dict[rows[0]] = rows[1:]
    
    #Return a combined dictionary of all the subdictionaries.
    return {"header" : headerdict, "data":data, "extended":extended_dict, "indicies":indicies}

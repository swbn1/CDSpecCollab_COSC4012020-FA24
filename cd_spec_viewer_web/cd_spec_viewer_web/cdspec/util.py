import csv
from itertools import islice


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
    data = []

    for rows in islice(reader, int(headerdict['NPOINTS'])):
        data.append(rows)
    
    extended_dict = {}
    for rows in reader:
        if rows:
            extended_dict[rows[0]] = rows[1:]
    
    return {"header" : headerdict, "data":data, "extended":extended_dict}

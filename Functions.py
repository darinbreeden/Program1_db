import csv

def readCSV(file, mstr_list):
    print('Reading CSV File...')
    with open(file) as csvFile:
        for row in csv.reader(csvFile):
            temp_list = []
            for i in row:
                temp_list.append(i)
            mstr_list.append(temp_list)
    print('Reading Complete...\n')

def readTXT(file, mstr_dict):
    print('Reading TXT File...')
    with open(file) as txtFile:
        for i in txtFile.readlines():
            temp_list = []
            j, k = i.split()
            temp_list.append(j)
            temp_list.append(k)
            temp_list
            if temp_list[0] not in mstr_dict:
                mstr_dict[j] = [k]
            else:
                mstr_dict[j].append(k)
    print('Reading Complete...\n')
import csv

def getModel(motor,conf, speed):
    csvFile = open(f'models/{motor}/{motor}-{conf}-{str(speed)}Sp.csv').readlines()
    content = csv.reader(csvFile)
    return content

def rawDataList(model):
    filteredContent = list()
    for row in model:
        if row[0] == '':
            continue
        if row[0].startswith('Ang'):
            filteredContent.append(row)
            continue
        row = [float(i) for i in row]
        filteredContent.append(row)
    return filteredContent

def buildMatrix(model):

    # TODO - Implement the mapping function to the nominal frequencies { freq_array -> nomFreq_array}
    
    # Initialize the lists 
    frequencies = list()
    angles = list()
    matrix = list()

    first = True # Its the first time that the program pass by a angle set
    for i in range(len(model) - 1):

        if type(model[i][0]) is str: # If the pointer is on a "Angle XX"

            first2 = False # Tells the program that he's not in the first angle set
            if first: # If it is the first time that it pass by a angle set
                first2 = True # Says that actually it is the first angle set
                first = False # Now on, it will be not the first time it passes by a angle set
            j = 0 # index for iterating by the matrix, reset on each pass by a "Angle XX"

            angles.append(model[i][0]) # Add the angle to the angle list

        else: # If the ponter is on a Frequencie:Data pair
            # If it is the first angle set, initialize the rows of the matrix 
            if first2: 
                matrix.append([])
            # Add the frequencies to the frequencies list and the data to the new column on the matrix 
            frequencies.append(model[i][0])
            matrix[j].append(model[i][1]) 

            j += 1

    return matrix, frequencies, angles
        
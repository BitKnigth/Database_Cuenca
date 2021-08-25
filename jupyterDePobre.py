import os
from posix import listdir 
import biblio
import csv


def getModel(motor,conf, speed):
    csvFile = open(f'models/{motor}/{motor}-{conf}-{str(speed)}Sp.csv').readlines()
    content = csv.reader(csvFile)
    return content

filteredContent = list()
outputMatrix = list()
frequencies = ['']

def rawDataList(model):
    for row in model:
        if row[0] == '':
            continue
        if row[0].startswith('Ang'):
            tmp = list()
            filteredContent.append(row)
            continue
        row = [float(i) for i in row]
        filteredContent.append(row)
    return filteredContent

for row in rawDataList(getModel("FanA", "Conf203", 60)):
    print(row)
import os
import csv

def listDirectory(relative_path):
    '''list the content of directory'''
    datModels = os.listdir(f'{os.getcwd()}/{relative_path}')
    return datModels

def createModelsFolders(datModelsFolderName):
    os.mkdir(f'{os.getcwd()}/models')
    for f in newMotorsList(datModelsFolderName, dat=True):
        os.mkdir(f'{os.getcwd()}/models/{f}')
    return

def newMotorsList(datModelsFolderName=None, dat=False):
    '''Generate a list containing the avaliable models'''
    if dat:
        motorsFolders = listDirectory(datModelsFolderName)
        motorsFolders = [f.split("-") for f in motorsFolders]
        for i in range(len(motorsFolders)):
            if len(motorsFolders[i]) == 3:
                motorsFolders[i] = motorsFolders[i][0]
            elif len(motorsFolders[i]) == 4:
                motorsFolders[i] = motorsFolders[i][0] + '-' + motorsFolders[i][1]
            # TO DO -> Implement a raiseException("Invalid dat file.")
    else:
        motorsFolders = listDirectory("models/")

    motorsFolders = list( set(motorsFolders) )

    return motorsFolders

def createSpeedsCSVs(datModelsFolderName):
    '''Create the individual speeds "*".csv for each motor'''
    models = listDirectory(datModelsFolderName)
    motors = newMotorsList(datModelsFolderName, dat=True)

    for m in models:
        tempHandler = open(f'{os.getcwd()}/{datModelsFolderName}/{m}').readlines()
        del(tempHandler[0])
        for motor in motors:
            if m.startswith(motor):
                aux = m.split('-')
                if len(aux) == 4:
                    path = f'{os.getcwd()}/models/{motor}/{aux[0] +"-"+ aux[1] +"-"+ aux[3][:-4].lower()}'
                elif len(aux) == 3:
                    path = f'{os.getcwd()}/models/{motor}/{aux[0] +"-"+ aux[2][:-4].lower()}'
                else:
                    raise Exception("invalid model: " + m)
                with open(path + '.csv', 'w', newline='') as handler:
                    writer = csv.writer(handler)
                    for row in tempHandler:
                        row = row.strip().split(',')
                        writer.writerow(row)
                break
    return



        

        


        




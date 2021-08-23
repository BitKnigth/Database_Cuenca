from genericpath import exists
import pandas as pd
import os
import pathlib
import csv

def list_directory(relative_path):
    '''list the content of directory'''
    datModels = os.listdir(f'{os.getcwd()}/{relative_path}')
    return datModels

def createModelsFolders():
    os.mkdir(f'{os.getcwd()}/models')
    for f in newMotorsList(dat=True):
        os.mkdir(f'{os.getcwd()}/models/{f}')
    return

def newMotorsList(dat=False):
    '''Generate a list containing the avaliable models'''
    if dat:
        motorsFolders = list_directory("datModels/")
        motorsFolders = [f.split("-") for f in motorsFolders]
        for i in range(len(motorsFolders)):
            if len(motorsFolders[i]) == 3:
                motorsFolders[i] = motorsFolders[i][0]
            elif len(motorsFolders[i]) == 4:
                motorsFolders[i] = motorsFolders[i][0] + '-' + motorsFolders[i][1]
            # TO DO -> Implement a raiseException("Invalid dat file.")
    else:
        motorsFolders = list_directory("models/")

    motorsFolders = list( set(motorsFolders) )

    return motorsFolders

def createSpeedsCSVs():
    '''Create the individual speeds "*".csv for each motor'''
    models = list_directory("datModels")
    motors = newMotorsList(dat=True)

    for m in models:
        tempHandler = open(f'{os.getcwd()}/datModels/{m}').read()
        for motor in motors:
            if m.startswith(motor):
                with open(f'{os.getcwd()}/models/{motor}/{m[:-4]}.csv', 'w') as handler:
                    writer = csv.writer(handler)
                    writer.writerows(tempHandler)
                break
    return



        

        


        




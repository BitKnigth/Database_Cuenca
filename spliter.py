import pandas as pd
import os
import pathlib


def newModelsList():
    '''Generate a list containing the avaliable models'''
    path = f'{os.getcwd()}/datModels/'
    modelsFolders = os.listdir(path)
    modelsFolders = [f.split("-") for f in modelsFolders]
    
    for i in range(len(modelsFolders)):
        if len(modelsFolders[i]) == 3:
            modelsFolders[i] = modelsFolders[i][0]
        elif len(modelsFolders[i]) == 4:
            modelsFolders[i] = modelsFolders[i][0] + '-' + modelsFolders[i][1]
    
    modelsFolders = list( set(modelsFolders) )
    return modelsFolders

def createModelsFolders(models):

    for f in newModelsList():
        path = f'{os.getcwd()}/models/{f}'
        os.makedirs(path, exist_ok=True)
    return

def createSpeedsCSVs(models):
    pass

print(newModelsList())
modelFolder = newModelsList()
createModelsFolders(modelFolder)



import os
import csv

def listDirectory(relative_path):
    '''list the content of directory'''
    datModels = os.listdir(f'{os.getcwd()}/{relative_path}')
    return datModels

def newMotorsList(datModelsFolderName=None, dat=False):
    '''Generate a list containing the avaliable models'''
    motorsFolders = listDirectory("/HeidmannDataHandler/models/")
    motorsFolders = list( set(motorsFolders) )
    return motorsFolders


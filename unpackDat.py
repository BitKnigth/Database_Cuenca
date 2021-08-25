import os
import csv
import biblio


def unpack(datModelsFolder = "datModels"):

    print("-> Creating models folders")
    try:
        biblio.createModelsFolders(datModelsFolder)
        print("-> Done.")
    except FileExistsError:
        print("\n-X error -> Models Folder already exists, unpacking .dat models.")
    
    print("\n-> Unpacking .dat models.")
    biblio.createSpeedsCSVs(datModelsFolder)
    print("\n-> All .dat models succesfuly unpacked.")

    return 

unpack("generic")
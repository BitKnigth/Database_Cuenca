import os
import csv
import biblio


def unpack():

    print("-> Creating models folders")
    try:
        biblio.createModelsFolders()
        print("-> Done.")
    except FileExistsError:
        print("\n-X error -> Models Folder already exists, unpacking .dat models.")
    
    print("\n-> Unpacking .dat models.")
    biblio.createSpeedsCSVs()
    print("\n-> All .dat models succesfuly unpacked.")

    return 

unpack()
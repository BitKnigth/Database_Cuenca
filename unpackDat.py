from . import unpackUtils


def unpack(datModelsFolder = "datModels"):

    print("-> Creating models folders")
    try:
        unpackUtils.createModelsFolders(datModelsFolder)
        print("-> Done.")
    except FileExistsError:
        print("\n-X error -> Models Folder already exists, unpacking .dat models.")
    
    print("\n-> Unpacking .dat models.")
    unpackUtils.createSpeedsCSVs(datModelsFolder)
    print("\n-> All .dat models succesfuly unpacked.")

    return 

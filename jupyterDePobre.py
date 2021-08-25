import os 
import biblio
import csv

content = csv.reader(f'{os.getcwd()}/models/FanA/{biblio.list_directory("/models/FanA")[0]}')

for row in content:
    print(row)

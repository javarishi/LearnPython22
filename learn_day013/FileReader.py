import csv

file_path = "/RISHI/H2K/FileIO/CSVTest.csv"
'''
mode
'r' - read only - file must exists
'a' - append new data to existing data - file will be created if not exists
'w' - remove existing and write new - file will be created if not exists
'x' - create

't' - text file - readable (strings)
'b' - binary mode 
'''
file = open(file_path, 'rt')

for eachRow in file:
    print(eachRow.split(",")[0])

file.close()

# CSV Reading example with 'with command'
csv_file_path = "/RISHI/H2K/FileIO/CSVFilesteachers.csv"

with open(csv_file_path, "rt") as csvfile:
    csv_rows = csv.reader(csvfile)
    for eachRow in csv_rows:
        print(eachRow[0])


import os

file_path = "/RISHI/H2K/FileIO/test_feb22.txt"
#os.remove(file_path)
#print("File is removed")

if os.path.exists(file_path):
    print("File Exists")
    os.remove(file_path)
else:
    open(file_path, 'x')
    print("File was not there , hence created")

dir_file = "/RISHI/H2K/FileIO/newFeb22"
if os.path.exists(dir_file):
    print("Directory Exists")
    os.rmdir(dir_file)
else:
    os.mkdir(dir_file)
    print("Directory created")


root_dir = "/RISHI/H2K/FileIO"
file_list = os.listdir(root_dir)
for eachFileName in file_list:
    if eachFileName.count(".csv") > 0:
        print(eachFileName)

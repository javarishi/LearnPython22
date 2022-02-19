file_path = "/RISHI/H2K/FileIO/test_feb22.txt"

file = open(file_path, 'w')
for i in range(10):
    file.write("This is Line Number {} \n ".format(i))

file.write("End of File \n")
file.close()
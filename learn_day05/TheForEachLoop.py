'''
for eachItem in dataStructure:
    block of code for every Item in data structure

range - start, end, step

Research HW - What if I want to stop the loop after 5th iteration
Research HW - What if I want to skip 5thh iteration and continue to 6th
'''
from setuptools.command.easy_install import easy_install

total = 0
for eachNum in range(11, 0, -2):
    total = total + eachNum
    print(eachNum)

print("Total :: ", total)

marks = [90,92,94,95,96,99]
total_marks = 0
for eachMarks in marks:
    total_marks = total_marks + eachMarks

print("Total Marks for Student is ", total_marks)


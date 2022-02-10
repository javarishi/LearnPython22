sampleList = ["Niel", 101, "3305 Spring Hill Pwky", 99.75]

# accessing
print(sampleList)
print(sampleList[0])
print(sampleList[3])
#print(sampleList[30])
# adding element
sampleList.insert(1, "Armstrong")
print(sampleList)
sampleList.insert(1, "NASA")
sampleList.append("NASA")
print(sampleList)
# remove - 1 occurrence of provided data
sampleList.remove("NASA")
print(sampleList)
# pop - remove element at index
# len for all countable objects in Python
end_index = len(sampleList) - 1
sampleList.pop(end_index)
print(sampleList)
# delete - operates on all Python objects
#del sampleList[0]
print(sampleList)

# membership
if 101 in sampleList:
    print("Roll Number is " , 101)

# not member
if 102 not in sampleList:
    print("Roll number is not ", 102)

# for loop
for eachItem in sampleList:
    print(eachItem)

roll_numbers = [90,91,56,67,78,98]
print(roll_numbers)
roll_numbers.sort()
print(roll_numbers)
sampleList.reverse()
print(sampleList)
# clear
sampleList.clear()
# del sampleList
print(sampleList)

# reverse

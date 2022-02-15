def say_hello(name, state="GA"):
    print("Hello", name, state)
    return "This is Brand new day {}".format(name)


def total_marks(marks):
    total = 0
    for eachMarks in marks:
        total = total + eachMarks
    return total


def tri_recurrsion(count):
    if count > 0:
        result = count + tri_recurrsion(count - 1)
        print("Count ", count, "Result ", result)
    else:
        result = 0
    return result


total_rec = tri_recurrsion(5)
print("Final Total ", total_rec)

message = say_hello("Neil")
print(message)
message = say_hello("Neil", "FL")

marks = [90,99,96,87,73,95]
sum_of_marks = total_marks(marks)
print("Total Marks Obtained ", sum_of_marks)
'''
1. ANy number of arguments
2. Default Parameter

'''

def print_values(paramOne, paramTwo):
    print(paramOne)
    print(paramTwo)


print_values(paramTwo="121", paramOne="3435")
print(type(print_values)) # <class 'function'>

another_variable_name = print_values
another_variable_name("111", "222")
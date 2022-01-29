print("Hello ")
print("Students")

# Single Line Comment starts with hash

'''
this is multi line comment
starts and ends with three single qoutes
'''
explain = """ 
this is mis-represented as comment
this is called as docString
you can assign a variable to it
"""

print(explain)

age = 21
_age = 22
_ = 23
age25 = 25
# 26age = 26
Age = 26
AGE = 27
print(age, Age, AGE)
percentage = 99.14
complex_var = 3 + 5j
isValid = True
name = "niel armstrong"

print(name, type(name), id(name))

quantity = 5.65
qty = int(quantity)
print(qty, type(qty), id(qty))

price = int("100")
print(price)

tax = float(12)
print(tax, type(tax), id(tax))

complex_tax = complex(quantity);
print(complex_tax, type(complex_tax), id(complex_tax))


# variableName = variable Value

age1 = 21
age2 = 21
age3 = 21

print(id(age1), id(age2), id(age3))
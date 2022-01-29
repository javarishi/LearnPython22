greet = 'Hello, World !'
space_greet = "    Hello    "

print(greet)
print(greet[0])
print(greet[10])
print(greet[0:5])# startIndex to EndIndex-1
print(space_greet)
print(space_greet.strip()) # removes any whitespace from the beginning or the end!"
print(len(greet)) #returns the length of a string
print("greet.lower() :: ", greet.lower()) # returns the string in lower case
print("greet.upper() :: ", greet.upper()) #returns the string in upper case
print("greet.title() :: ", greet.title())
print("greet.capitalize() :: ", greet.capitalize())
print(greet.replace("H", "J")) # replaces a string with another string
print(greet.split(",")) # returns ['Hello', ' World!']
print(greet.find('W'))# First occurance
print(greet.count('l'))
age = "100A"
a = "PYTHON"
print("greet.isalpha() :: ", greet.isalpha())
print("a.isalpha() :: ", a.isalpha())
print("greet.isnumeric() :: ", greet.isnumeric())
print("age.isnumeric() :: ", age.isnumeric())
print("age.isalnum() :: ", age.isalnum())
print("age.istitle() :: ", age.istitle())

result = "Thank You Mr. {}, Your result is {}"
print(result.format("RISHI", "PASS"))
print(result.format("VENKAT", "FAIL"))
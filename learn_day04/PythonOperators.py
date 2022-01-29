# Arithmatic Operators

one = 100
two = 2

print("Addition ", (one+two))
print("Subtraction ", (one - two))
print("Multiplication ", (one * two))
print("Division ", (one / two))
print("Modulus ", (one % two))
print("Exponential ", (one ** two))
print("Floor Division ", (one // two))

# Assignment Operators =

# Comparision Operators < <= > >= != ==
# Comparision op always generates boolean result
print("Less than", (one < two))
print("Less than or equals", (one <= two))
print("Greater than", (one > two))
print("Greater than or equals", (one >= two))
print("Not equals", (one != two))
print("Equals ", (one == two))

# •	Logical operators - AND
three = 50
'''
Truth Table
S1  S2  R(S1&S2)
T   T   T
T   F   F
F   T   F
F   F   F
'''
print(False and True)
'''
Truth Table for OR
S1  S2  R(S1 | S2)
T   T   T
T   F   T
F   T   T
F   F   F
'''
print(False or True)
'''
Truth Table for NOT
S R(!S)
T   F
F   T
'''
print(not True)
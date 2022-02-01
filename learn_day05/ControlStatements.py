'''
if condition:
    block of code executes when condition is true
else:
    block of code executes when condition is false
'''

age = 15
state = "FL"
if age >= 18:
    print("Alcohol Purchase is Permitted")
elif state == "FL" and age >= 15:
    print("Alcohol Purchase is Permitted because of State permissions")
else:
    print("Alcohol Purchase is not permitted")

print("End of If Statement")
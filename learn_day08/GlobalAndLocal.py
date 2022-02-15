age = 15

def validate_age():
    global age
    age = 19
    print("Inside method Age :: ", age)
    if age > 18:
        print("Age is Valid")


validate_age()
print("Outer Age :: ", age)
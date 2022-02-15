def shout(text_message):
    return str(text_message).upper()

def smile(text_message):
    return str(text_message).lower()

def greet_me(function_name):
    print(function_name("Hello This is Siri"))

greet_me(shout)

def calculator(num, function_name):
    # Local functions
    def addition():
        return num + num

    def substraction():
        return num - 1

    def multiplication():
        return num * num

    if function_name == "add":
        return addition
    elif function_name == "minus":
        return substraction
    else:
        return multiplication


operation = calculator(5, "multiply")
value = operation()
print(value)
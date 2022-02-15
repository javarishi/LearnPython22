def sample_function_args(name, age, *args, **kwargs):
    print(name)
    print(age)
    print("*** Args Starts ***")
    company = args[0]
    email = args[1]
    print(company, email)
    company = "NASA.com"
    print(company, email)
    print("*** KWArgs Starts ***")
    for key, value in kwargs.items():
        print(key, value)


'''
normal args - 1
args - tuple for un-named arguments
kwargs = named parameters 
'''
sample_function_args("Niel","27", "NASA", "niel@nasa.com", address="2278 SpaceHill Blvd")
'''
def validate_customer(fname, lname):
    if str(fname).isalpha() and str(lname).isalpha():
        print("Name is Valid")
        return True
    else:
        return False


def validate_customer(*args):
    print(type(args))
    flag = True
    for eachData in args:
        if not str(eachData).isalpha():
            flag = False
    return flag
'''

def validate_customer(**kwargs):
    print(type(kwargs))
    flag = True
    zipcode_val = kwargs.get("zipcode")
    if str(zipcode_val).isnumeric() and len(str(zipcode_val)) == 5:
        print("Valid Zip Code")

validity = validate_customer(fname="Niel", lname="Armstrong", company="NASA",state="FL", zipcode = "33080")
print("Validity ", validity)
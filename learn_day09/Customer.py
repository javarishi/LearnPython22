class Customer:
    '''
    Parameterised Constructor
    '''
    def __init__(self, age, gender, attire):
        print("This is Customer Constructor")
        self.age = age
        self.gender = gender
        self.attire = attire

    def browse(self, interested_products):
        print("In browse function:: ", self.attire)
        for eachProduct in interested_products:
            print(eachProduct)

femaleCust = Customer("27", "F", "Business") # this is instance of Customer class
print(femaleCust.age, femaleCust.gender, femaleCust.attire)
femaleCust.age = 30
femaleCust.attire = 'Casual'

print(femaleCust.age, femaleCust.gender, femaleCust.attire)
femaleCust.browse(["Deodorant", "Wine", "Chips"])
# self is object on which the function is being called
anotherCust = femaleCust
print(anotherCust.age, anotherCust.gender, anotherCust.attire)


print(type(femaleCust.browse)) # <class 'method'>
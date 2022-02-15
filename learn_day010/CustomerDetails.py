
class Customer:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.discount = "0"
        print("Customer Instance ", self.name, self.gender, self.age)

    def process_discount(self):
        self.discount = "2.5%"
        print("Discount for new customer {}".format(self.discount))


class PreferredCustomer(Customer):

    def __init__(self,name, gender, age, email):
        Customer.__init__(self, name, gender, age)
        self.email = email
        print("Preferred Customer Instance " , self.email)

    def send_offers(self):
        print("Sending Offer to {}".format(self.email))

    def process_discount(self):
        self.discount = "3.5%"
        print("Discount for Preferred customer {}".format(self.discount))


class LoyaltyCardCustomer(PreferredCustomer):

    def __init__(self,name, gender, age, email, ssn, address):
        PreferredCustomer.__init__(self,name, gender, age, email)
        self.ssn = ssn
        self.address = address

    def send_offers(self):
        super().send_offers()
        print("Sending Offer to {}".format(self.address))


    def process_discount(self):
        self.discount = "4%"
        print("Discount for Loyalty Card customer {}".format(self.discount))


loyalCust = LoyaltyCardCustomer("Bob", 40, "M", "Bob@bestbuy.com", "3902324324", "654 Hills Ave")
loyalCust.send_offers()
loyalCust.process_discount()

'''
custOne = PreferredCustomer(name="Niel", age="38", gender="M", email="neil@nasa.com")
custOne.send_offers()
custOne.process_discount()

custOrigin = Customer("Bob", 40, "M")
custOrigin.process_discount()
'''
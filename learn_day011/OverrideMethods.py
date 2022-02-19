class Simple:
    def __init__(self):
        print("Simple Parent Class")

    def simple_method(self):
        print("Method from Simple Class")


class SuperSimple(Simple):
    def __init__(self):
        super().__init__()
        print("SuperSimple Child Class")

    def simple_method(self):
        super(SuperSimple, self).simple_method()
        print("Method from SuperSimple Class")

obj = SuperSimple()
obj.simple_method()

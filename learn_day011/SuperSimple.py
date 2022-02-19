class Simple:
    def __init__(self):
        print("Simple Parent Class")


class SuperSimple(Simple):
    def __init__(self):
        super(SuperSimple, self).__init__()
        print("SuperSimple Child Class")


simple = SuperSimple()
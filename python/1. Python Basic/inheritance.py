class Person:
    def general_description(self):
        print("In general: I'm just a person.")


class Man(Person):
    def __init__(self):
        print("I'm a man")
        self.sex = "M"
        self.type = "Male"

    def description(self):
        self.general_description()
        print("presentation: I'm a man oh")


class Woman(Person):
    def __init__(self):
        print("I'm a woman")
        self.sex = "F"
        self.type = "Female"

    def description(self):
        self.general_description()
        print("presentation: I'm a Female oh")


alpha = Man()
alpha.description()

print(".........")
andrea = Woman()
andrea.description()

print(".........")


class MixedPerson(Man, Woman):
    def showme(self):
        self.description()
        print("im mixed")


arnold = MixedPerson()
arnold.showme()

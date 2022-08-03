class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "web developer":
            print(self.name, " is a web developer")
        elif self.occupation == "mobile developer":
            print(self.name, " is a mobile developer")
        elif self.occupation == "designer":
            print(self.name, " is a designer")
        else:
            print(self.name, "has not registered job")

    def say_hello(self):
        print(self.name, "says Hello!")


alpha = Human("alpha", "24", "web developer")
alpha.do_work()
alpha.say_hello()

andrea = Human("andrea", "22", "raggae man")
andrea.say_hello()
andrea.do_work()


class Trouble:
    def __init__(self, level, typetrouble, result):
        self.level = level
        self.typetrouble = typetrouble
        self.result = result

    def create_trouble(self):
        if self.typetrouble == "aggressive":
            print("ggrrrrrrrrrr.......")
        elif self.typetrouble == "normal":
            print("grerr.......")
        elif self.typetrouble == "low":
            print("grr.......")
        else:
            print("You should define the type of the trouble you want to create")


newTrouble = Trouble(level="10", typetrouble="aggressive", result="none")
newTrouble.create_trouble()

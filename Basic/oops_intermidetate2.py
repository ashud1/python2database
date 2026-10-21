class Animal():

    def __init__(self):
        print("Animal created")

    def whoAMI(self):
        print("Animal")

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def eat(self):
        print("Dog eating")

# mya=Animal()
# mya.whoAMI()
# mya.eat()

myd=Dog()

myd.whoAMI()
myd.eat()



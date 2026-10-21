class Dog():
#self is referring to the class
# Class object attribute 
    species="mammal"
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name


mydog=Dog(breed="Lab",name="Sammy")

# otherdog=Dog( breed="husky")
print(mydog.breed,mydog.name,mydog.species)
# print(otherdog.breed)
class Circle():
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.radius*self.radius*self.pi

    def set_radius(self,new_r):
        self.radius=new_r

myCircle=Circle(3)

myCircle.set_radius(10)

print(myCircle.area())
        
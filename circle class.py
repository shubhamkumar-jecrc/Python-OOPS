class Circle():

    #Class object attribute
    pi=3.14
   
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*self.pi
        #self.area=radius*radius*Circle.pi
        #referencing class object attributes

    #method
    def get_circumferece(self):
        return self.radius*self.pi*2

#changing the default value of r and we are overriding it
my_circle=Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumferece())
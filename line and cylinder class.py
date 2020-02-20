class Line:
    def __init__(self,coor1,coor2):
        self.x1=coor1[0]
        self.x2=coor2[0]
        self.y1=coor1[1]
        self.y2=coor2[1]

    def distance(self):
        return (((self.x2-self.x1)**2)+((self.y2-self.y1)**2))**0.5
    def slope(self):
        return ((self.y2-self.y1)/(self.x2-self.x1))

class Cylinder:
    def __init__(self,height,radius):
        self.h=height
        self.r=radius
    def volume(self):
        return 3.14*((self.r)**2)*self.h
    def surface_area(self):
        return (2*3.14*self.r*self.h)+(2*3.14*(self.r)**2)


coordinate1=(3,2)
coordinate2=(8,10)
li=Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

c=Cylinder(2,3)
print(c.volume())
print(c.surface_area())
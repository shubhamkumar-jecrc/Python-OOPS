

#Base Class
class Animal():

    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print('I am an animal.')
    def eat(self):
        print("I am eating.")


#Derived Class
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    def who_am_i(self):
        print('I am a Dog')
    def bark(self):
        print("Woof!")
    def eat(self):
        print("I am a dog and eating.")

#mydog created of Dog() class
mydog=Dog()

#who_am_i() & bark() method is created which is in both base and derived class
#here deerived class method override base class.
mydog.who_am_i()
mydog.bark()


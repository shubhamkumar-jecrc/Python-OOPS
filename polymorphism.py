class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says woof!"
class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says meow!"

niko=Dog("Niko")
felix=Cat("Felix")

print(niko.speak())
print(felix.speak())

#Each of them has speak() method 
#example of polymorphism
for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak))

#second way to show polymorphism
def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))
print(pet_speak(felix))

class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Sub class must implement this abstarct method")

myanimal=Animal('fred')
myanimal.speak()
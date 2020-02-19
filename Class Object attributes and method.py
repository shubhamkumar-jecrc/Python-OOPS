class Dog():
    
    #Class object attribute
    #same for any instance of a class
    species ='mammal'

    def __init__(self,breed,name,spot):
        self.breed = breed
        self.name = name         
        self.spot =spot

    #operations/Actions ---> Methods
    def bark(self,number):
        print('WOOF! my name is {} and the no. is:{}'.format(self.name,number))

my_dog=Dog(breed='lab',name='Sam',spot=False)

#these are attributes which are being executeed
print(my_dog.species)
print(my_dog.spot)
print(my_dog.breed)
print(my_dog.name)

#these are methods which are being called
#methods are the function  which are inside class
my_dog.bark(10)
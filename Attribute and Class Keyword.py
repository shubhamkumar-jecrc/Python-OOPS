class Dog():
    
    #init can basically be though as constructur
    #automatically called 
    #self keyword represents instances of the object itself.
    #most oo language pass this as a hidden parameter to method defined.
    #but in python we have to declare explicitly
    #and by convention we use word self you can use anyhting.

    def __init__(self,breed,name,spots):
        
        #attributes
        #we taken in the argument
        #assign it using self.attribute_name 
        
        self.breed = breed
        self.name = name         
        self.spot =spots
        
        #self.mybreed =breed
        #print(my_dog.mybreed)

my_dog=Dog(breed='Lab',name='Sammy',spots=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spot)
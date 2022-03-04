import math

class Circle:

    PI = math.pi # class attribute 

    def __init__(self, radius):
        self.__radius = 1       # a _ before the name tells other programmers this method shoudl nt be changed outside of the class
        self.radius = radius    # a __ before the name python performs name mangling
                                # to call the __radius attribute outside of the class now, its full name is _Circle__radius
    @property # this is a decorator 
    def radius(self): # this is a getter method
        return self.__radius 
    
    @radius.setter #this is a setter method so the radius can now be changed
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius 
        else:
            print(f"Radius must be greater than zero. Default radius (1) set")
            self.radius = 1
            
    @property
    def area(self):
        return Circle.PI * self.__radius ** 2 
    
    def circ(self):
        circum = 2 * Circle.PI * self.__radius
        return circum

    def __str__(self):
        return f"Circle instance of radius : {self.__radius}"

c1 = Circle(10)
print(c1.radius) # this will return the self.__radius attribute value for the c1 instance of teh Circle class
# if i wanted to change the radius i would now need a setter method. 

# now that I have the setter method, the value of self.__radius can now be changed 
c1.radius = 20
print(c1.radius) 
print(f"Area is : {c1.area}")
#from math import pi
import math

class Circle:

    PI = math.pi # class attribute 
    Instances = 0

    def __init__(self, radius):
        self.radius = radius 
        Circle.Instances += 1

    def area(self):
        return Circle.PI * self.radius**2 
        

    def circ(self):
        circum = 2 * Circle.PI * self.radius
        return circum

    @classmethod
    def sphere_vol(cls, radius): #cls needed as first reference for a class method - class method, class attributes not required, doesnt need an instance of teh class for the method to be used 
        vol = (4/3) * Circle.PI * radius**3 
        return vol 

radius = 10
print(f" Sphere of radius {radius} has volume {Circle.sphere_vol(radius)}") #instance of the class not required, no attributes of the class are required for the calculation in sphere_vol

# print(Circle.Instances)

# circle_1 = Circle(10)
# circle_2 = Circle(15)
# circle_3 = Circle(5)

# print(Circle.Instances)

# print(f"Area = {circle_1.area()}")
# print(f"Circumference = {circle_1.circ()}")
# print(f"Area of circle with radius {circle_1.radius} is {circle_1.area()}")
    
# print(Circle.PI) # can access class attributes like this, without creating an instance of the class
# print(f"pi from instance : {circle_1.PI}") 

#print(Circle.__dict__)


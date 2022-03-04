#from math import pi
import math

class Circle:

    PI = math.pi # class attribute 

    def __init__(self, radius=1): #default value of 1
        self.radius = radius 

    def area(self):
        return Circle.PI * self.radius ** 2 
    

    def circ(self):
        circum = 2 * Circle.PI * self.radius
        return circum

    def __gt__(self, other):
        return self.radius > other.radius
           
    def __str__(self):
        return f"Circle object of radius : {self.radius}"

    def __repr__(self):
        return f"Circle(radius = {self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

c1= Circle(radius = 10)
c2= Circle(15)
c3= Circle(20)
c4= Circle(25)

#print(dir(c4)) # returns the methods and dunder methods available for the object passed in 

print(c1 < c2) # Circle.__gt__(c1, c2) - this is what python is doing under the hood 

lst = [c3, c4, c2, c1]
# for c in lst:
#     print(c.radius)

# lst.sort()

# print("\n After sorting \n")
# for c in lst:
#     print(c.radius)


print(c1)
c3 = c1 + c2
print(c3.radius)
print(c1 + c2)
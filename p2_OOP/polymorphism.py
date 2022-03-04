import math

class Circle:

    PI = math.pi # class attribute 

    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return Circle.PI * self.radius ** 2 
    
    def circ(self):
        circum = 2 * Circle.PI * self.radius
        return circum

    def __str__(self):
        return f"Circle({self.radius})"

class Triangle:

    def __init__(self, height, base):
        self.height = height 
        self.base = base
    
    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle({self.height}, {self.base})"

class Square:

    def __init__(self, dim):
        self.dim = dim

    def area(self):
        return self.dim**2

    def __str__(self):
        return f"Square({self.dim})"
        
c1 = Circle(1)
c2 = Circle(2)
t1 = Triangle(1,2)
t2 = Triangle(2,4)
sq1 = Square(1)
sq2 = Square(2)

shapes = [c1, t1, t2, sq1, sq2, c2]

for shape in shapes:
    #print(shape)
    print(shape.area()) # common interface 'area' method present in all classes - this is known as polymorphism through duck typing 

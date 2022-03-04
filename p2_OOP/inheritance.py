class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle({self.length}, {self.width})"

class Square(Rectangle):
    # inherits all of the attributes and methods from Rectangle for new class square
    def __init__(self, dim, colour='Red'): 
        self.colour = colour        # we can add new attributes like colour
        super().__init__(dim, dim)  # we need to overwrite init of parent class as we only need 1 measurement for a square
                                    # super calls the _init_ method from the parent class, so we can use dim as the length and width as these will be the same for a square 
        #Rectangle.__init__(self, dim, dim) - same as what the super does

    # we dont need to declare the area as it is inherited 

    # we need to overwrite the __str__ method as it is not suitable for our Sqaure class

    def __str__(self):
        return f"Square({self.length}, {self.colour})"

    def perim(self):
        return 2 * (self.length + self.width) 

sq1 = Square(dim = 10, colour="Blue")
r1 = Rectangle(10,5)

print(f"Area of {r1} is {r1.area()}")
print(f"Area of {sq1} is {sq1.area()}")
print(f"The perimeter of the Square is {sq1.perim()}")
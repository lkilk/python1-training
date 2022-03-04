from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    def __init__(self, name):
        self.name = name
        self.dims = {}

    @abstractmethod
    def area(self):
        ...                  #unimplimented abstract method

    def __str__(self):
        desc = f"{self.name} of dimensions : {self.dims} and area : {self.area()}"
        return desc 

class Circle(Shape):


    def __init__(self, name, radius):
        super().__init__(name)
        self.dims['radius'] = radius
        
    def area(self):
        return pi * self.dims['radius']**2 

class Rectangle(Shape):

    def __init__(self, name, length, width):
        super().__init__(name)
        self.dims['length'] = length
        self.dims['width'] = width

    def area(self):
        return self.dims['length'] * self.dims['width']

c1 = Circle('Circle', 10)
print(c1)

r1 = Rectangle('Rectangle', 10, 20)
print(r1)
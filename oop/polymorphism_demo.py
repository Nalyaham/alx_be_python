import math 
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)

    def area(self):
        return self.length * self.width

class Circle(Shape):
    constant = 3.14159

    def __init__(self, radius):
        self.radius = int(radius)

    def area(self):
        return self.radius * self.radius * self.constant 

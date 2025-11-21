import math

# Base class
class Shape:
    def area(self):
        pass  # This method will be overridden in derived classes

# Derived class for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
triangle = Triangle(10, 5)
rectangle = Rectangle(8, 4)
circle = Circle(7)

print("Area of Triangle:", triangle.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", round(circle.area(), 2))

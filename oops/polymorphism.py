# Polymorphism: Greek word that means "many forms"
# Poly = Many, Morphe = Form

# Achieved in two ways in Python:
# 1. Inheritance: An object is treated as a type of its parent
# 2. Duck Typing: "If it walks like a duck and quacks like a duck..."

from abc import ABC, abstractmethod  # For creating abstract base classes

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Each shape must implement its own area calculation

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # Fixed to 3.14 instead of 3.4

# Square class inheriting from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2  # Correct formula for square area

# Triangle class inheriting from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  # Correct triangle area formula

# List of different shape objects
shapes = [Circle(4), Square(5), Triangle(6, 7)]

# Demonstrating polymorphism — same interface, different behavior
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")

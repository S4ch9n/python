# super() : Function used in a child class to call methods from a parent class (superclass).
# Allow you to extend the functionality of the inherited methods

class Shape:
    def __init__(self , color , is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape) :
    def __init__(self, color, is_filled , radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {3.14 * self.width * self.width}cm2")



class Triangle(Shape):
    def __init__(self, color, is_filled, width , height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {3.14 * self.width * self.height / 2}cm")

circle = Circle("red" , True , 5)
square = Square("blue" , False , 6)
triangle= Triangle("yellow" , True , 7 , 8)

circle.describe()
square.describe()
triangle.describe()


print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")


print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

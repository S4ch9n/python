#In Python, a constructor is a special method used to initialize the attributes of a class when an object is created. The constructor method is defined using the __init__ method.
#constructor is a special function that gets automatically called when object of class created
from copyreg import constructor

from tuples import names


class A:
    age = 10
    def __init__(self):
        self.name = "John"  # Define name as an instance attribute
        print("name is ", self.name, "and age is ", self.age)

obj = A()
print(obj.age)  # Accessible
print(obj.name)  # Accessible

#
class Point:
    def __init__(self, x, y):  # Corrected the typo here
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point = Point(10, 20)  # Now this will work
print(point.x)  # Outputs: 10
print(point.y)  # Outputs: 20


#
class Person:
    def __init__(self, name):  # Constructor to initialize the name
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')  # Use the instance's name attribute


# Creating an instance
john = Person("John Smith")
print(john.name)  # Outputs: John Smith
john.talk()  # Outputs: Hi, I am John Smith

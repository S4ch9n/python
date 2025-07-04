#object is an instance of class , a class simply define the blueprint or the template for creating objects , and objects are the actual instances on that blue print
#In Python, a class is a blueprint for creating objects, providing initial values for state (attributes) and implementations of behavior (methods). You define a class using the class keyword. Here's the general syntax:
# class = (blueprint) used to design the structure and layout of an object
from membershipOperators import student


# Define a class named Point
class Point:
    # Define a method 'move' within the class
    def move(self):
        print("move")

    # Define a method 'draw' within the class
    def draw(self):
        print("draw")


# Create an object (instance) of the Point class
point1 = Point()

# Call the 'draw' method on the object 'point1'
point1.draw()  # Output: draw



class Car:
    def __init__(self , model , year , color , for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

#     methods : are action that objects can perform
    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("VW" , 2024,"BLACK" , True)
car2 = Car("Mustang" , 20220 , "Red" , True )
car3 = Car("Charger" , 2026 , "Yellow" , True)

# the . here represent attribute access operator
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)


car1.drive()
car1.stop()

car2.drive()
car2.stop()


car1.describe()



# class variable = Shared among all instance of a class
# defined outside the constructor
# Allow you to share among all objects created from that class
class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student('Nick', 30)
student2 = Student('John', 40)
student3 = Student("Fury" , 55)
student4 = Student('Bob' , 87)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)



# print(Student.num_students)

# print(student1.name)        # Prints 'Nick'
# print(student1.age)         # Prints 30
# print(student1.class_year)  # Prints 2024
#
#
# print(student2.name)
# print(student2.age)
# print(Student.class_year)


# Define the class
class Students:
    # Class variable shared by all instances of the class
    section = 'A'

    # Constructor to initialize instance variables
    def __init__(self, name, age):
        # Instance variables unique to each object
        self.name = name
        self.age = age

# Create an object (instance) of the class
student1 = Students("Akash", 16)

# Access and print class and instance variables
print(student1.section)  # Output: A (class variable)
print(student1.name)     # Output: Akash (instance variable)
print(student1.age)      # Output: 16 (instance variable)

# Modify instance variable 'name' for student1 only
student1.name = "Rahul"
print(student1.name)     # Output: Rahul (only student1's name changed)

# Modify class variable 'section' for all instances of the class
Students.section = "B"
print(student1.section)  # Output: B (class variable changed for all instances)













#inheritance : when we define a class that inherit all properties of parent class
#Inheritance in Python
# Inheritance is a mechanism in Python (and object-oriented programming in general) where a new class (called the child class or subclass) can inherit attributes and methods from an existing class (called the parent class or superclass). This allows the child class to reuse code from the parent class and, if needed, override or extend its functionality.
# Parent class (also called base class or superclass)
from tuples import names


# Base class representing a generic color
class Color:
    def __init__(self, color_name):
        """
        Initialize the color with a name.

        :param color_name: The name of the color (e.g., "white", "black").
        """
        self.color_name = color_name
    def display_color(self):
        """
        Print a message displaying the color's name.
        """
        print(f"The color is {self.color_name}.")
# Derived class representing a specific color (black)
class Black(Color):
    def display_black_message(self):
        """
        Print a specific message about the color black.
        """
        print("This is the black color.")


# Example usage of the classes
if __name__ == "__main__":
    # Create an instance of the base Color class with the color "white"
    white_color = Color("white")
    print(white_color.color_name)  # Output the name of the color
    white_color.display_color()  # Call the method to display the color

    # Create an instance of the Black class with a specific color name
    black_color = Black("Black")
    black_color.display_color()  # Call the method from the base class
    black_color.display_black_message()  # Call the method specific to the Black class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")
# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the parent class constructor
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} barks!")
# Create an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing methods and attributes
print(my_dog.name)  # Inherited from Animal
print(my_dog.breed)  # Defined in Dog
my_dog.speak()  # Overridden method in Dog

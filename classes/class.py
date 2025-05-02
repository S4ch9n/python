#object is an instance of class , a class simply define the blueprint or the template for creating objects , and objects are the actual instances on that blue print
#In Python, a class is a blueprint for creating objects, providing initial values for state (attributes) and implementations of behavior (methods). You define a class using the class keyword. Here's the general syntax:

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

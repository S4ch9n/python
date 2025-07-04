#inheritance : when we define a class that inherit all properties of parent class
#Inheritance in Python
# Inheritance is a mechanism in Python (and object-oriented programming in general) where a new class (called the child class or subclass)
# can inherit attributes and methods from an existing class (called the parent class or superclass).
# This allows the child class to reuse code from the parent class and, if needed, override or extend its functionality.
# Parent class (also called base class or superclass)
from tuples import names

#simple example
# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

# Another child class
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

# Create instances
dog1 = Dog("Buddy", 5)
cat1 = Cat("Whiskers", 3)

# Call methods
dog1.speak()   # Inherited from Animal
dog1.bark()    # Defined in Dog

cat1.speak()   # Inherited from Animal
cat1.meow()    # Defined in Cat




#multiple inheritance : inherit from more than one parent class
# Base class: Animal
class Animal:
    def __init__(self, name):
        self.name = name  # common attribute

    def eat(self):
        print(f"{self.name} is eating")  # common method for all animals

    def sleep(self):
            print(f"{self.name} is sleeping")

# Prey class inherits from Animal
class Prey(Animal):
    def flee(self):  # behavior specific to prey
        print(f"{self.name} is fleeing")


# Predator class also inherits from Animal
class Predator(Animal):
    def hunt(self):  # behavior specific to predators
        print(f"{self.name} is hunting")


# Rabbit is a type of Prey
class Rabbit(Prey):
    pass  # no extra behavior — inherits everything from Prey and Animal


# Hawk is a type of Predator
class Hawk(Predator):
    pass  # no extra behavior — inherits from Predator and Animal


# Fish is both a Prey and a Predator (Multiple Inheritance)
class Fish(Prey, Predator):
    pass  # inherits from both Prey and Predator — and Animal


# Create instances of the animals
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Mist")

# Call methods on rabbit (inherits from Prey → Animal)
rabbit.flee()  # From Prey
rabbit.eat()   # From Animal

# Call method on hawk (inherits from Predator → Animal)
hawk.eat()     # From Animal





#multilevel inheritance = inherit from a parent which inherits from another parent.

#duck typing : Another way tot achieve polymorphism besides Inheritance object must have the minimum necessary attributes/methods
#If it looks like a duck and quacks like a duck , it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    def horn(self):
        print("HONK !")

animals = [Dog() , Cat() , Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
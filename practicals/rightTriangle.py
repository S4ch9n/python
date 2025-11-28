# Program to check if a triangle is right-angled

# Accept three sides from the user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Sort the sides so the largest becomes the hypotenuse
sides = sorted([a, b, c])

# Pythagoras theorem: a² + b² = c²
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("It is a right-angled triangle.")
else:
    print("It is NOT a right-angled triangle.")

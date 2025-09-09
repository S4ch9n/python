# Get user input
number = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#eligible for vote
# Input the age of the user
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")



#nested condition
gender = input("Enter your gender: ")
if gender == 'M':
    print("Male")
elif gender == 'F':
    print("Female")
else:
    print("Invalid input")


#calucaltor using nested condition
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operation = input("enter operation you want to be perform : + , - , / , * : ")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    if num2 == 0 :
        print("num2 should not be zero")
    else:
        print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
else:
    print("invalid operation")


#wap number is even and off
number = int(input("enter a number : "));
if number % 2 != 0:
    print("number is even")


#wap to check if number is positive , negative or zero




#find the largest element among three number
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if a > b:
    if a > c :
        print("a is greater ")
    else:
        print("c is greater")
elif b > a:
    if b > c:
        print("b is greater")
    else:
        print("c is grater")
else:
    print("c is greater")


#name greater than 5 and less than 10 , and name should start with "a"
name = input("Enter a username: ")

if 5 < len(name) < 10:
    if name.startswith("a"):
        print(name)
    else:
        print("Invalid")
else:
    print("Invalid name length must be greater than 5 and less than 10")




#or
users = input("Enter usernames separated by commas: ").split(",")

# strip spaces and filter
printNames = [name.strip() for name in users if name.strip().startswith("a") and 5 < len(name.strip()) < 10]

print("Valid names:", printNames)


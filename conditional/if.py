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
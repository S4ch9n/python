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





#
# Practical 3: Student Management Program
# Input student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")

# Input marks for 3 subjects directly
m1 = float(input("Enter marks for Subject 1 (out of 100): "))
m2 = float(input("Enter marks for Subject 2 (out of 100): "))
m3 = float(input("Enter marks for Subject 3 (out of 100): "))

attendance = float(input("Enter attendance percentage: "))

# Processing results
total = m1 + m2 + m3
percentage = total / 3

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"

# Reward eligibility
if percentage >= 85 and attendance >= 90:
    reward = "Eligible for Scholarship"
elif percentage >= 75 and attendance >= 80:
    reward = "Eligible for Certificate of Merit"
elif percentage >= 60 and attendance >= 75:
    reward = "Eligible for Participation Certificate"
else:
    reward = "Not eligible for extra benefits"

# Display result
print(f"Roll No: {roll}")
print(f"Marks: {m1}, {m2}, {m3}")
print(f"Average Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Attendance: {attendance}%")
print(f"Reward Eligibility: {reward}")

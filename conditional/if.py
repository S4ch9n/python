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


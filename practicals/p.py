# Basic Python Data Types

# 1. int (Integer)
# Whole numbers
x = 10
print("Integer (int):", x)

# 2. float
# Decimal numbers
y = 3.14
print("Float (float):", y)

# 3. str (String)
# Text
name = "ChatGPT"
print("String (str):", name)

# 4. bool (Boolean)
# True/False values
is_active = True
print("Boolean (bool):", is_active)


#Sequence Types
# 5. list
# Ordered, changeable collection
fruits = ["apple", "banana", "mango"]
print("List (list):", fruits)

# 6. tuple
# Ordered, unchangeable collection
point = (3, 4)
print("Tuple (tuple):", point)

# 7. range
# Sequence of numbers
nums = range(5)  # 0 to 4
print("Range (range):", list(nums))  # convert to list for display


# Mapping Type
# 8. dict (Dictionary)
# Key–value pairs
person = {"name": "Alice", "age": 25}
print("Dictionary (dict):", person)


# Set Types
# 9. set
# Unordered collection of unique values
numbers = {1, 2, 3}
print("Set (set):", numbers)






#2
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



#3
# ----------------------------------------------------------
# Student Management System
# Calculates Result, Attendance Status, Rewards & Eligibility
# ----------------------------------------------------------

# Input details from the user
name = input("Enter student name: ")

marks = float(input("Enter total marks obtained (out of 100): "))
attendance = float(input("Enter attendance percentage: "))
activities = input("Did student participate in extra activities? (yes/no): ").lower()

# Calculate Result (Pass/Fail)
if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Attendance Status
if attendance >= 75:
    attendance_status = "Good Attendance"
else:
    attendance_status = "Poor Attendance"

# Rewards based on performance
if marks >= 85 and attendance >= 90:
    reward = "Gold Star Award"
elif marks >= 70 and attendance >= 80:
    reward = "Silver Star Award"
elif marks >= 50 and attendance >= 75:
    reward = "Bronze Star Award"
else:
    reward = "No Reward"

# Equal Benefit Eligibility:
# Condition – student must PASS + attendance >= 75
if result == "PASS" and attendance >= 75:
    equal_benefit = "Eligible for Equal Benefit"
else:
    equal_benefit = "Not Eligible for Equal Benefit"

# Activity Bonus
if activities == "yes":
    activity_bonus = "Activity Bonus Granted"
else:
    activity_bonus = "No Activity Bonus"

# Final Output
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Marks:", marks)
print("Attendance:", attendance, "%")
print("Result:", result)
print("Attendance Status:", attendance_status)
print("Reward:", reward)
print("Extra Activity:", activity_bonus)
print("Equal Benefit:", equal_benefit)
print("----------------------------")




#4
# Program to check if a number is prime and show its factors
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print(num, "is NOT a prime number.")
else:
    factors = []
    # Find all factors from 1 to num
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            print("Factors:", factors)

    # Check if number is prime
    if len(factors) == 2:
        print(num, "is a PRIME number.")
    else:
        print(num, "is NOT a prime number.")
        print("Factors:", factors)





#5
# Program to check if a number is palindrome or not

num = int(input("Enter a number: "))

# Convert number to string for easy reversal
num_str = str(num)

# Check palindrome
if num_str == num_str[::-1]:
    print(num, "is a Palindrome number.")
else:
    print(num, "is NOT a Palindrome number.")


#6
# Program to print Pascal's Triangle

rows = int(input("Enter number of rows: "))

for i in range(rows):
    # Print leading spaces
    print(" " * (rows - i), end="")

    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        # Update value using nCr relation
        num = num * (i - j) // (j + 1)

    print()  # Move to next line







#7
# (a) Given a string, create a dictionary where keys are words & values are word lengths
# (a) Create dictionary of word : length

sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Dictionary with word length
word_lengths = {word: len(word) for word in words}

print("Word Length Dictionary:", word_lengths)

# (b) Given a list of integers, find all pairs whose sum = target


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target sum: "))

pairs = []

# Check all pairs
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("Pairs with sum", target, ":", pairs)


# (c) Rotate tuple by n positions

t = tuple(input("Enter tuple elements separated by space: ").split())
n = int(input("Enter number of positions to rotate: "))

# Left rotation
left_rotated = t[n:] + t[:n]

# Right rotation
right_rotated = t[-n:] + t[:-n]

print("Original Tuple:", t)
print("Left Rotated :", left_rotated)
print("Right Rotated:", right_rotated)





#8
# ------------------------------------------------------------
# Practical 8:
# Power set using recursion
# a) Keep only groups with even sum
# b) Arrange groups so the smallest groups come last
# ------------------------------------------------------------

# Recursive function to generate power set
def power_set_recursive(nums, index=0):
    # Base case: when index reaches end
    if index == len(nums):
        return [[]]

    # Recursive call for remaining elements
    subsets = power_set_recursive(nums, index + 1)

    # Add current element to each subset generated
    element = nums[index]
    new_subsets = []

    for subset in subsets:
        new_subsets.append([element] + subset)

    return subsets + new_subsets


# -----------------------------
# Main Program
# -----------------------------
numbers = list(map(int, input("Enter integers separated by space: ").split()))

# Generate power set
power_set = power_set_recursive(numbers)

# (a) Keep only subsets with even sum
even_sum_subsets = [subset for subset in power_set if sum(subset) % 2 == 0]

# (b) Arrange groups so that smallest groups come LAST
# Largest length first → smallest last
sorted_subsets = sorted(even_sum_subsets, key=lambda x: len(x), reverse=True)

# Output
print("\nPower Set (Recursively Generated):")
print(power_set)

print("\nSubsets with Even Sum:")
print(even_sum_subsets)

print("\nFinal Ordered Subsets (Smallest Last):")
print(sorted_subsets)





# ---------------------------------------------------------
# Shopping Cart using Recursion and Lambda Function
# ---------------------------------------------------------

cart = []   # Stores items as (name, price)


# -------------------------------------------
# 1. Recursive Menu
# -------------------------------------------
def menu():
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Items (minimum 2)")
    print("2. View Cart")
    print("3. Calculate Total Bill")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_items()
        menu()   # recursion
    elif choice == 2:
        view_cart()
        menu()   # recursion
    elif choice == 3:
        calculate_total()
        menu()   # recursion
    elif choice == 4:
        print("Thank you for shopping!")
    else:
        print("Invalid choice! Try again.")
        menu()   # recursion


# -------------------------------------------
# 2. Add at least two items
# -------------------------------------------
def add_items():
    print("\nAdd at least 2 items:")
    for i in range(2):  # ensures minimum 2 items
        name = input(f"Enter item {i+1} name: ")
        price = float(input(f"Enter item {i+1} price: "))
        cart.append((name, price))
    print("Items added successfully!")

    # Ask user if they want to add more
    more = input("Add more items? (yes/no): ").lower()
    if more == "yes":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.append((name, price))
        add_items()   # recursion to keep adding


# -------------------------------------------
# 3. View Cart using Recursion
# -------------------------------------------
def view_cart(index=0):
    if len(cart) == 0:
        print("Cart is empty.")
        return

    if index == len(cart):
        return

    print(f"{index+1}. {cart[index][0]} - Rs.{cart[index][1]}")
    view_cart(index + 1)  # recursive call


# -------------------------------------------
# 4. Calculate Total using Lambda + Recursion
# -------------------------------------------
def calculate_total():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    # Lambda to get price from tuple (name, price)
    get_price = lambda item: item[1]

    # Recursive summation
    def recursive_sum(i):
        if i == len(cart):
            return 0
        return get_price(cart[i]) + recursive_sum(i + 1)

    total = recursive_sum(0)
    print("Total Bill = Rs.", total)


# Start program
menu()


#10
# Solid Diamond Pattern

n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Hollow Diamond Pattern

n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")

# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")




#11
#wap to demonstrate multiple exception


list1 = [1,2,3,4,5]
try:
    num = int(input("enter index value : "))
    print(list1[num])
except IndexError:
    print("out of reach")
except ValueError:
    print("enter valid numer")
else:
    print(list1[num])
finally:
    print("done")



#2
dict1 = {
    1 : "abc",
    2 : "cde"
}
try:
    num = int(input("enter the value you want to print : "))
    print(dict1[num])
except KeyError:
    print("value didn't exist")
else:
    print(dict1[num])
finally:
    print("done")


#
try:
    file = open("data.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file didn't exist")
finally:
    print("done")

#
try:
    import pandas
except ImportError:
    print("doesnt have panda installed")
finally:
    print("done")

#
try:
    result = "5" + 5
except TypeError:
    print("character and integer value cant be add")
finally:
    print("done")
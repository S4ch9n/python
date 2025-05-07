# List in Python
# A list is a collection that is ordered and mutable (changeable).
#
# It allows duplicate elements.
#
# Lists are defined using square brackets [].
#
#
# Creating a list
fruits = ["apple", "banana", "cherry", "apple"]

# Accessing elements
print(fruits[0])  # Output: apple

# Modifying an element
fruits[1] = "blueberry"

# Adding an element
fruits.append("orange")

# Removing an element
fruits.remove("cherry")

# Iterating through a list
for fruit in fruits:
    print(fruit)


## append() - Adds an item at the end of the list.
numbers1 = [1, 2, 3]
numbers1.append(4)
print(numbers1)  # Output: [1, 2, 3, 4]

# insert() - Inserts an item at a specific position.
numbers2 = [1, 2, 3, 4]
numbers2.insert(1, 99)  # Insert 99 at index 1
print(numbers2)  # Output: [1, 99, 2, 3, 4]

# insert() - Inserts an item at a specific position.
numbers3 = [1, 2, 3, 4]
numbers3.insert(1, 99)  # Insert 99 at index 1
print(numbers3)  # Output: [1, 99, 2, 3, 4]

# pop() - Removes and returns an element at a given index (default is the last item).
numbers4 = [1, 2, 3, 4]
last_item = numbers4.pop()
print(last_item)  # Output: 4
print(numbers4)   # Output: [1, 2, 3]

# sort() - Sorts the list in ascending order.
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]

# reverse() - Reverses the list.
numbers.reverse()
print(numbers)  # Output: [9, 5, 2, 1]

# len() - Returns the number of elements in the list.
print(len(numbers))  # Output: 4

# count() - Returns the number of occurrences of a specified element.
fruits = ["apple", "banana", "apple", "cherry"]
print(fruits.count("apple"))  # Output: 2

# extend() - Extends a list by appending elements from another list.
numbers.extend([10, 11])
print(numbers)  # Output: [9, 5, 2, 1, 10, 11]

# index() - Returns the index of the first occurrence of an element.
print(numbers.index(5))  # Output: 1


#find the largest element in list
numbers = [1, 10, 2, 3, 5, 2]  # List of numbers
max_number = numbers[0]  # Initialize max_number with the first element of the list

# Loop through each number in the list
for number in numbers:
    if number > max_number:  # Check if the current number is greater than max_number
        max_number = number  # Update max_number if the condition is true

# Print the maximum number found in the list
print(f"maximum number in list is : {max_number}")


#2D list : A 2D list in Python is essentially a list of lists, where each element of the main list is itself a list. It can be used to represent tabular data, such as a grid, matrix, or spreadsheet.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for rows in matrix:
    for item in rows:
        print(f"items present in matrix are : {item}") 
        
        
        
        
        
        
#write a program to remove the duplicates in list
numbers = [2,3,4,2,12,3,1,32,6,6,7]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)


#even number in list using loop
num = [1,2,3,4,5,6,7,8,9,10]
even_number = [nums for nums in num if nums % 2 == 0]
print(f"even number are : {even_number}")


#odds number in list using loop
num2 = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = [nums for nums in num2 if nums % 2 != 0]
print(f"odd number are : {odd_numbers}")
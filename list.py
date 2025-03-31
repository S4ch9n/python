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

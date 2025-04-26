# Tuples in Python
# A tuple is an immutable sequence in Python that can hold a collection of items.
# Tuples are similar to lists but have a few key differences, the most notable being their immutability—
# once a tuple is created, its contents cannot be changed.

# Key Characteristics of Tuples:
# 1. Immutable: You cannot modify, add, or remove elements after the tuple is created.
# 2. Ordered: The elements in a tuple have a defined order that does not change.
# 3. Heterogeneous: A tuple can contain elements of different types (e.g., integers, strings, lists).
# 4. Hashable: Tuples can be used as keys in dictionaries if they contain only hashable elements.

# Creating Tuples:
# Using parentheses:
my_tuple = (1, 2, 3)

# Without parentheses (tuple packing):
my_tuple = 1, 2, 3

# For single-element tuples, include a trailing comma:
single_element_tuple = (1,)

# Accessing Elements:
# Tuples support indexing and slicing.
my_tuple = (10, 20, 30, 40)
print(my_tuple[1])    # Output: 20
print(my_tuple[:2])   # Output: (10, 20)

# Common Tuple Methods:
# count(): Returns the number of times a specified value occurs in the tuple.
my_tuple = (1, 2, 3, 2, 2)
print(my_tuple.count(2))  # Output: 3

# index(): Returns the index of the first occurrence of a specified value.
my_tuple = (10, 20, 30, 20)
print(my_tuple.index(20))  # Output: 1

# Tuple Functions:
# len(): Returns the number of elements in the tuple.
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

# max() and min(): Return the largest and smallest element in the tuple (works with comparable types).
my_tuple = (5, 10, 15)
print(max(my_tuple))  # Output: 15
print(min(my_tuple))  # Output: 5

# sum(): Returns the sum of all numeric elements in the tuple.
my_tuple = (1, 2, 3)
print(sum(my_tuple))  # Output: 6

# sorted(): Returns a sorted list of the tuple's elements.
my_tuple = (3, 1, 2)
print(sorted(my_tuple))  # Output: [1, 2, 3]

# zip(): Combines multiple iterables into tuples.
names = ('Alice', 'Bob')
scores = (85, 90)
print(list(zip(names, scores)))  # Output: [('Alice', 85), ('Bob', 90)]

# Use Cases of Tuples:
# Immutable data storage: Use tuples for data that should not change, such as coordinates (x, y) or RGB color values.

# Returning multiple values from a function:
def calculate(a, b):
    return a + b, a * b

result = calculate(3, 4)
print(result)  # Output: (7, 12)

# Dictionary keys: Tuples can be used as keys because they are immutable.
my_dict = {('x', 'y'): 10}
print(my_dict[('x', 'y')])  # Output: 10

# Tuples are a simple and efficient way to organize and use collections of data when mutability is not needed.

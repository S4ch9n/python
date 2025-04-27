# Sets in Python are a collection type used to store multiple items in a single variable, similar to lists or dictionaries. However, sets have unique properties that distinguish them:
#
# Key Features of Sets
# Unordered: Sets do not maintain the order of elements.
#
# Unique Elements: A set does not allow duplicate elements.
#
# Mutable: You can add or remove elements from a set.
#
# Heterogeneous: A set can contain elements of different data types.
#
# Creating Sets
# You can create a set using curly braces {} or the set() constructor.

# Using curly braces
my_set = {1, 2, 3, 4}

# Using set() constructor
another_set = set([4, 5, 6])

# Creating an empty set
empty_set = set()


# Basic Operations
# Adding and Removing Elements

# Adding an element
my_set.add(5)

# Adding multiple elements
my_set.update([6, 7, 8])

# Removing an element
my_set.remove(2)  # Raises KeyError if the element is not found
my_set.discard(3)  # Does not raise an error if the element is not found

# Removing all elements
my_set.clear()


# Membership Testing
print(4 in my_set)  # True
print(10 in my_set)  # False


# Set Operations
# Python sets support standard mathematical set operations like union, intersection, and difference.
#
# Union
# Combines elements from both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5}


# Intersection
# Returns elements common to both sets.
print(set1 & set2)  # {3}


# Difference
# Returns elements in the first set but not in the second.
print(set1 - set2)  # {1, 2}


#
# Symmetric Difference
# Returns elements in either set but not in both.
print(set1 ^ set2)  # {1, 2, 4, 5}



# Useful Methods
# len(set): Returns the number of elements in the set.
#
# set.copy(): Returns a shallow copy of the set.
#
# set.pop(): Removes and returns an arbitrary element.
#
# set.isdisjoint(other_set): Checks if two sets have no elements in common.
#
# set.issubset(other_set): Checks if the set is a subset of another set.
#
# set.issuperset(other_set): Checks if the set is a superset of another set.

# Example Code

fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "banana", "mango"}

# Union
print(fruits | tropical)  # {'apple', 'banana', 'cherry', 'pineapple', 'mango'}

# Intersection
print(fruits & tropical)  # {'banana'}

# Difference
print(fruits - tropical)  # {'apple', 'cherry'}
# Sets are powerful tools for tasks involving unique elements and set-based logic in Python.
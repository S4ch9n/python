# In Python, a string is a sequence of characters enclosed within single quotes ('), double quotes ("), or triple quotes (''' or """). Strings are widely used to represent text and are immutable, meaning their contents cannot be changed after creation.
# Single quotes
single_quote_string = 'Hello, World!'

# Double quotes
double_quote_string = "Hello, World!"

# Triple quotes (useful for multiline strings)
triple_quote_string = '''This is
a multiline
string.'''


# Common String Operations
# Concatenation:

s1 = "Hello"
s2 = "World"
result = s1 + " " + s2  # Output: "Hello World"



# Repetition:

repeated = "Hi! " * 3  # Output: "Hi! Hi! Hi! "


# Accessing Characters:
my_string = "Python"
first_char = my_string[0]  # Output: 'P'
last_char = my_string[-1]  # Output: 'n'




# Slicing:
substring = my_string[1:4]  # Output: 'yth' (from index 1 to 3)


# String Methods:

# lower() – Converts to lowercase.
#
# upper() – Converts to uppercase.
#
# strip() – Removes leading/trailing spaces.
#
# replace("old", "new") – Replaces a substring.
#
# split("delimiter") – Splits the string into a list.
#
# join(iterable) – Joins elements of an iterable into a string.

text = " Hello, Python! "
print(text.lower())       # Output: " hello, python! "
print(text.strip())       # Output: "Hello, Python!"
print(text.replace("Python", "World"))  # Output: " Hello, World! "


# Checking Substrings:
my_string = "Python programming"
print("Python" in my_string)  # Output: True
print("Java" not in my_string)  # Output: True


# Length of a String:

length = len(my_string)  # Output: 18
#
# f-Strings (String Interpolation)
# Introduced in Python 3.6, f-strings allow for embedding expressions inside string literals:

name = "Alice"
age = 25
greeting = f"My name is {name} and I am {age} years old."  # Output: "My name is Alice and I am 2
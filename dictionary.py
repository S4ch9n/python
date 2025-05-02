# A dictionary in Python is a built-in data structure that allows you to store and retrieve data using key-value pairs.
# Dictionaries are mutable, meaning you can modify them after creation.
# They are unordered in versions of Python before 3.7, but starting with Python 3.7, dictionaries maintain the insertion order.
from email import message_from_string

# Creating a Dictionary
# You can create a dictionary using curly braces {} or the dict() constructor.

# Using curly braces
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using the dict() constructor
my_dict2 = dict(name="Bob", age=30, city="Los Angeles")

# Accessing Values
# You access dictionary values using keys.
print(my_dict["name"])  # Output: Alice

# Modifying a Dictionary
# You can add, update, or remove key-value pairs.

# Add a new key-value pair
my_dict["job"] = "Engineer"

# Update an existing key
my_dict["age"] = 26

# Remove a key-value pair
del my_dict["city"]

# Common Methods
# Here are some commonly used dictionary methods:

# .keys(): Returns all the keys in the dictionary.
# .values(): Returns all the values in the dictionary.
# .items(): Returns all key-value pairs as tuples.
# .get(key): Returns the value for a key, or None if the key is not found.
# .pop(key): Removes and returns the value for the given key.

# Example of dictionary methods
keys = my_dict.keys()  # Returns dict_keys(['name', 'age', 'job'])
values = my_dict.values()  # Returns dict_values(['Alice', 26, 'Engineer'])
items = my_dict.items()  # Returns dict_items([('name', 'Alice'), ('age', 26), ('job', 'Engineer')])

value = my_dict.get("name")  # Output: Alice
removed_value = my_dict.pop("age")  # Removes and returns 26

# Iterating Through a Dictionary
# You can iterate through a dictionary's keys, values, or both:

# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])  # Prints each key and its corresponding value

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Prints key-value pairs in the format "key: value"

# Dictionaries are incredibly versatile and widely used in Python
# for tasks like counting items, organizing data, and implementing mappings.






#digit game
# Prompt the user to enter a phone number
phone = input("Phone : ")
# Dictionary to map digits to their word equivalents
digit_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
# Initialize an empty string to build the output
output = ""
# Loop through each character in the user-provided phone number
for ch in phone:
    # Get the word equivalent of the digit from the dictionary
    # If the digit is not found in the dictionary, default to '!'
    output += digit_mapping.get(ch, '!') + " "
# Print the final output string
print(output)




#emoji game
message = input(">")
words = message.split(" ")
emojis = {
    ":)" : "😊",
    ":(" : "😔"
}
output2 = ""
for char in words:
    output2 += emojis.get(char, char) + " "

print(output2)

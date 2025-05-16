#maximum and minimum in tuples
tuples = (1,2,3,4,5)
print(max(tuples))
print(min(tuples))

#reverse a string using loop
string = 'Python'
reverseChar = ""
for char in string:
    reverseChar = char + reverseChar
print(reverseChar)


#Python program to interchange first and last elements in a list
list1 = [1,2,3,4,5]
list1[0],list1[4] = list1[4],list1[0]
print(list1)

#sum of tuples elements
#using sum function
tuples = (1,2,3,4,5)
total = sum(tuples)
print(total)

#without using function
tuples2 = (1,2,3,4,5)
total2 = 0
for element in tuples2:
    total2 += element
print(total2)

#Write a Python code to check if a number is even or odd
def checkNum(n):
    if n % 2 == 0:
        return "Number is even"
    return "Number is odd"
result = checkNum(5)
print(result)

# Write a Python code to concatenate two strings
str1 = "Hello"
str2 = "World"
concat = str1 + " " +  str2
print(concat)

#Write a Python program to find the maximum of three numbers
def findGreatest(a,b,c):
    return max(a,b,c)

greatest_num = findGreatest(1,2,3)
print(f"greatest number are {greatest_num}")

#Write a Python program to count the number of vowels in a string
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowels("Python hello"))

#Write a Python program to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call
print(factorial(5))  # Should print 120


# Write a Python code to convert a string to an integer
str3 = '12345'  # A string containing numeric characters
print(str3)  # Prints the string
print(type(str3))  # Prints the type of str3 (should be <class 'str'>)

toInt = int(str3)  # Converts the string to an integer
print(toInt)  # Prints the converted integer
print(type(toInt))  # Prints the type of toInt (should be <class 'int'>)



#find the smallest positive number in list
list1 = [1,-2,4,-5,-9,10,3,4,6,7]
positive_num = min([num for num in list1 if num > 0 ])
print(positive_num)



#find the  positive number in list without using function
list2 = [1,-2,4,-5,-9,10,3,4,6,7]
positive_num = []
for char in list2:
    if char > 0:
        positive_num = positive_num + [char]
print(positive_num)



##find the smallest positive number in list without using minimum function
list3 = [1, -2, 4, -5, -9, 10, 3, 4, 6, 7]  # Initialize the list with both positive and negative numbers
# Step 1: Filter out positive numbers
positive_num2 = []  # Create an empty list to store positive numbers
for char in list3:  # Iterate over each number in the original list
    if char > 0:  # Check if the current number is positive
        # Add the positive number to the positive_num2 list
        # Use concatenation to create a new list with the current number
        positive_num2 = positive_num2 + [char]
# At this point, positive_num2 contains all positive numbers from list3

# Step 2: Find the smallest positive number manually
if positive_num2:  # Check if there are any positive numbers in the positive_num2 list
    smallest_positive = positive_num2[0]  # Assume the first positive number is the smallest initially
    for num in positive_num2:  # Iterate through the list of positive numbers
        if num < smallest_positive:  # Compare each number with the current smallest
            smallest_positive = num  # Update smallest_positive if a smaller number is found
    # After the loop ends, smallest_positive contains the smallest positive number
    print("The smallest positive number is:", smallest_positive)  # Print the result
else:
    # If positive_num2 is empty, it means there are no positive numbers in the original list
    print("No positive numbers in the list.")

#Write a Python program to calculate the area of a rectangle
def rectangle(length,width):
    return length * width
print(rectangle(2,3))



# Write a Python code to merge two dictionaries# Define the first dictionary
dict1 = {
    'a': 1,  # Key 'a' with value 1
    'b': 2,  # Key 'b' with value 2
    'c': 3   # Key 'c' with value 3
}

# Define the second dictionary
dict2 = {
    'd': 4,  # Key 'd' with value 4
    'e': 5,  # Key 'e' with value 5
    'f': 6   # Key 'f' with value 6
}

# Merge the two dictionaries using dictionary unpacking
concat = {**dict1, **dict2}
print(concat)  # Output the merged dictionary

# # Explanation of {**dict1, **dict2}:
# # - **dict1 expands the key-value pairs of dict1: 'a': 1, 'b': 2, 'c': 3
# # - **dict2 expands the key-value pairs of dict2: 'd': 4, 'e': 5, 'f': 6
# # - The resulting dictionary combines all key-value pairs from dict1 and dict2 into a new dictionary
# # - If there are duplicate keys, values from dict2 will overwrite the ones from dict1
#




#Write a Python program to find common elements in two lists
# Define the first list
newList = [1, 2, 3, 4, 5]  # A list of integers

# Define the second list
newList2 = [2, 4, 5, 6, 5]  # Another list of integers (note the duplicate 5)

# Find the common elements between the two lists
# Step 1: Convert newList to a set using set(newList)
#         This removes duplicates (if any) and allows set operations like intersection.
#         The set from newList is: {1, 2, 3, 4, 5}

# Step 2: Convert newList2 to a set using set(newList2)
#         This removes duplicates (if any) from newList2.
#         The set from newList2 is: {2, 4, 5, 6}

# Step 3: Find the intersection of the two sets using '&' operator
#         The intersection gives elements that are present in both sets.
#         Resulting set: {2, 4, 5}

# Step 4: Convert the resulting set back to a list using list().
#         This creates a list of common elements: [2, 4, 5]

common_list = list(set(newList) & set(newList2))

# Print the list of common elements
print(common_list)  # Output: [2, 4, 5]




# Write a Python code to remove duplicates from a list
# Define a list with duplicate elements
newList3 = [1, 2, 3, 4, 3, 1, 2, 3, 4, 5, 4, 3, 2]

# Step 1: Convert the list to a set using set(newList3)
#         A set is an unordered collection of unique elements.
#         This operation removes all duplicate values from newList3.
#         Resulting set: {1, 2, 3, 4, 5}

unique_list = list(set(newList3))

# Step 2: Convert the set back to a list using list().
#         This creates a list of unique elements.
#         Resulting list: [1, 2, 3, 4, 5] (order may vary because sets are unordered)

print(unique_list)  # Output the list of unique elements




#Write a Python code to check if a string is a palindrome
# Define a function to check if a string is a palindrome
def isPalindrome(s):
    # Step 1: Compare the string 's' with its reverse 's[::-1]'
    #         's[::-1]' uses slicing to reverse the string:
    #         - The first ':' means we're slicing the entire string.
    #         - The '-1' means we're stepping backward, effectively reversing the string.
    #         If the string is the same as its reverse, it is a palindrome.
    return s == s[::-1]

# Test the function with the string "hello"
print(isPalindrome("hello"))  # Output: False (because "hello" is not the same as "olleh")

# Test the function with the string "radar"
print(isPalindrome("radar"))  # Output: True (because "radar" is the same as "radar" when reversed)


#Write a Python program to find the longest word in a sentence
def longest_word(sentence):
    # Step 1: Split the sentence into a list of words
    # The split() method breaks the sentence into words separated by spaces
    # Example: "The fox jumps over the lazy dog" -> ['The', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    words = sentence.split()

    # Step 2: Find the word with the maximum length using max() with key=len
    # - max() normally compares the elements in the list directly (e.g., alphabetically).
    # - key=len tells max() to compare the words based on their lengths instead of their default values.
    # - len is a built-in function that returns the length of a word.
    # For example:
    #   len('The') = 3
    #   len('fox') = 3
    #   len('jumps') = 5 (longest word)
    # max() selects the word with the largest length.
    return max(words, key=len)

# Call the function and print the longest word in the sentence
print(longest_word("The fox jumps over the lazy dog"))  # Output: jumps



#sum of elements in list
new_list = [1,2,4,5]
total = 0
for add in new_list:
    total += add
print(total)

#swap two number in list using temp variable
new_list2 = [1,2,3,4,5]
temp = 0
temp = new_list2[0]
new_list2[0] = new_list2[4]
new_list2[4] = temp
print(new_list2)

#merge two list in python
concat = new_list + new_list2
print(concat)


#remove duplicates from list using loops
listt = [1, 2, 3, 4, 2, 21, 1, 3, 22, 4, 55]
unique_list = []
for num in listt:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)  # Output the list with duplicates removed


#prime number
prime_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in prime_list:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(f"Number is prime: {num}")




#join two list
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
add_list = list1 + list2
print(add_list)

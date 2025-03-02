#operaotrs are token that triggers some computation / action when applied to variable and other object in expression
#arithmetic operator (+, - , * , / , ** , //)
# Initialize variables a and b
a = 20
b = 10

# Calculate the sum of a and b
sum = a + b
print(sum)  # Output: 30

# Calculate the difference between a and b
sub = a - b
print(sub)  # Output: 10

# Calculate the product of a and b
mult = a * b
print(mult)  # Output: 200

# Calculate the division of a by b
div = a / b
print(sum)  # Incorrect print statement, should be 'print(div)' for correct output

# Calculate a raised to the power of b
pow = a ** b
print(pow)  # Output: 10240000000000

# Calculate the integer (floor) division of a by b
res = a // b
print(res)  # Output: 2


# Comparison (Relational) Operators
a = 5
b = 10

# Greater than
print(a > b)  # Output: False

# Less than
print(a < b)  # Output: True

# Equal to
print(a == b)  # Output: False

# Not equal to
print(a != b)  # Output: True

# Greater than or equal to
print(a >= b)  # Output: False

# Less than or equal to
print(a <= b)  # Output: True


#logical operator
x = True
y = False

# Logical AND
print(x and y)  # Output: False

# Logical OR
print(x or y)  # Output: True

# Logical NOT
print(not x)  # Output: False


#bitwise operator
# Bitwise AND (&)
# 1. Bitwise AND (&)
# Compares each bit of two numbers.
# If both bits are 1, the result is 1; otherwise, it's 0.
# Example:
# a = 5 (binary: 0101)
# b = 3 (binary: 0011)
#
# Performing a & b:
#   0101
# & 0011
# ------
#   0001  (decimal: 1)
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print(a & b)  # Output: 1 (Binary: 0001)


# 2. Bitwise OR (|)
# Compares each bit of two numbers.
# If at least one of the bits is 1, the result is 1.
# Example:
# a = 5 (binary: 0101)
# b = 3 (binary: 0011)
#
# Performing a | b:
#   0101
# | 0011
# ------
#   0111  (decimal: 7)
print(a | b)  # Output: 7 (Binary: 0111)



# 3. Bitwise XOR (^)
# Compares each bit of two numbers.
# The result is 1 if the bits are different; otherwise, it's 0.
# Example:
# a = 5 (binary: 0101)
# b = 3 (binary: 0011)
#
# Performing a ^ b:
#   0101
# ^ 0011
# ------
#   0110  (decimal: 6)
print(a ^ b)  # Output: 6 (Binary: 0110)



# Bitwise NOT (~)
# Flips all the bits of a number.
# Converts 1 to 0 and 0 to 1.
# In Python, the result also includes the sign bit, making it equivalent to -(x + 1).
# Example:
# a = 5 (binary: 0101)
#
# Performing ~a:
# Original:   00000000 00000000 00000000 00000101 (binary representation of 5)
# Bitwise NOT:11111111 11111111 11111111 11111010 (flips all bits)
# Result: -6 (in two's complement form)
print(~a)  # Output: -6



# 5. Left Shift (<<)
# Shifts the bits of the number to the left by a specified number of positions.
# New bits on the right are filled with 0.
# Each left shift is equivalent to multiplying the number by
# 2
# 𝑛
# 2
# n
#   (where
# 𝑛
# n is the number of shifts).
# Example:
# a = 5 (binary: 0101)
#
# Performing a << 1:
#   0101 << 1
# = 1010  (binary: 1010, decimal: 10)
# print(a << 1)  # Output: 10 (Binary: 1010)



# 6. Right Shift (>>)
# Shifts the bits of the number to the right by a specified number of positions.
# For positive numbers, new bits on the left are filled with 0.
# Each right shift is equivalent to dividing the number by
# 2
# 𝑛
# 2
# n
#   (where
# 𝑛
# n is the number of shifts), discarding the remainder.
# Example:
# a = 5 (binary: 0101)
#
# Performing a >> 1:
#   0101 >> 1
# = 0010  (binary: 0010, decimal: 2)
print(a >> 1)  # Output: 2 (Binary: 0010)


#assignment operator
# Assign
a = 10
print(a)  # Output: 10

# Add and assign
a += 5
print(a)  # Output: 15

# Subtract and assign
a -= 3
print(a)  # Output: 12

# Multiply and assign
a *= 2
print(a)  # Output: 24

# Divide and assign
a /= 4
print(a)  # Output: 6.0

# Modulus and assign
a %= 5
print(a)  # Output: 1.0

# Exponent and assign
a **= 2
print(a)  # Output: 1.0

# Floor divide and assign
a //= 1
print(a)  # Output: 1.0


#membership operator
lst = [1, 2, 3, 4]

# In
print(2 in lst)  # Output: True

# Not in
print(5 not in lst)  # Output: True


#identify operators
a = 5
b = 5
c = [1, 2, 3]
d = [1, 2, 3]

# Is (checks for same object reference)
print(a is b)  # Output: True
print(c is d)  # Output: False

# Is not
print(c is not d)  # Output: True
# Immutable: Integers
x = 10
y = 10
print(x is y)  # True (points to the same object in memory)

# Mutable: Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # False (different objects in memory)

# Check contents instead of reference
print(list1 == list2)  # True (contents are the same)

# Assigning one list to another
list3 = list1
print(list3 is list1)  # True (same reference, both point to the same object)


#ternanry operators
a = 10
b = 20

# Ternary operation
max_value = a if a > b else b
print(max_value)  # Output: 20


#Operator Precedence
# Operator precedence example
result = 10 + 2 * 3  # Multiplication has higher precedence
print(result)  # Output: 16

# Program to check if a number is palindrome or not

num = int(input("Enter a number: "))

# Convert number to string for easy reversal
num_str = str(num)

# Check palindrome
if num_str == num_str[::-1]:
    print(num, "is a Palindrome number.")
else:
    print(num, "is NOT a Palindrome number.")

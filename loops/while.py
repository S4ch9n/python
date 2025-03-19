#count even odd
num = 10
countEven = 0
countOdd = 0
i = 1

while i <= num:
    if i % 2 == 0:
        countEven += 1
    else:
        countOdd += 1

    i += 1  # Increment i correctly in Python

print("Count of even numbers:", countEven)
print("Count of odd numbers:", countOdd)


#reverse the digit
num = 12345
num2 = 5
rev = 0
i = 1
rem = 0
while i <= num2:
    rem = num % 10
    rev = rev * 10 + rem
    num = num//10
    i+=1
print(rev)


#count digits
digits = 12345
countDigit = 0

while digits > 0:
    countDigit += 1
    digits //= 10  # Perform integer division to reduce the number

print(countDigit)


#multiplication table
# Input from the user for the number
number = int(input("Enter a number to display its multiplication table: "))
# Initialize the counter
i = 1

print(f"\nMultiplication Table for {number}:")

# While loop to generate the multiplication table
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1  # Increment the counter

#for loop
i = 1
sum = 0
for i in range (1,10):
    sum += i
print(sum)


#2 1 t to 10
for i in range(1,11):
    print(i)


#3: printing hello 10 times
for i in range(1,11):
    print("hello")

#will print odds
for i in range(1,11,2):
    print(i)


#count digit
digits = 12345
countDigit = 0

# Convert digits to a string to iterate through each digit
for digit in str(digits):
    countDigit += 1

print(countDigit)


#multiply table
number = int(input("Enter the number to generate its multiplication table: "))
limit = int(input("Enter the limit of the table: "))

print(f"Multiplication Table for {number}:")

for i in range(1, limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")

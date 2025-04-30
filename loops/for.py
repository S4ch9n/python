#for loop
i = 1
sum = 0
for i in range (1,10):
    sum += i
print(sum)


#2> 1 to 10
for i in range(1,11):
    print(i)


#3: printing hello 10 times
for i in range(1,11):
    print("hello")

#will print odds
for i in range(1,100,2):
    print(f"odd numbers are : {i}")

#even numbers are
for i in range(2,101,2):
    print(f"even numbers are : {i}")

#
#iteraton over list
#iteraton over list
list1 = [10,20,30,40,50]
total = 0
for items in list1:
    total += items
print(total)

#nested loops
for x in range(4):
    for y in range(3):
        print(f"value of x is : {x} |  value of is :  {y}  ")
#output : 0,0
# 0,1
# 0,2
# 1,0
# 1,1
# 1,20
# 2,0
# 2,1
# 2,2
# 3,0
# 3,1
# 3,2



#xxxxx
#xx
#xxxxx
#xx
#xx
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ""
    for stars in range(x_count):
        output += "x"
    print(output)




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

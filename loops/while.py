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
while(i <= num2):
    rem = num % 10
    rev = rev * 10 + rem
    num = num//10
    i+=1
print(rev)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

subtraction = a - b
addition = c + d
result = subtraction * addition

print("Result:", result)


#wap to check valid username and password
username = input("Enter a username: ")
password = input("Enter a password: ")

if username == "abc" and password == "123":
    print("Valid")
else:
    print("Not valid")



#WAP to ask the userfor two number and show their binaray fom and all bitwise result
# Ask the user for two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Show binary representation
print(f"\nBinary of {a}: {bin(a)}")
print(f"Binary of {b}: {bin(b)}")

# Perform bitwise operations
print("\nBitwise Operations:")
print(f"{a} & {b} = {a & b} (Binary: {bin(a & b)})")
print(f"{a} | {b} = {a | b} (Binary: {bin(a | b)})")
print(f"{a} ^ {b} = {a ^ b} (Binary: {bin(a ^ b)})")
print(f"~{a} = {~a} (Binary: {bin(~a)})")
print(f"~{b} = {~b} (Binary: {bin(~b)})")
print(f"{a} << 1 = {a << 1} (Binary: {bin(a << 1)})")
print(f"{b} << 1 = {b << 1} (Binary: {bin(b << 1)})")
print(f"{a} >> 1 = {a >> 1} (Binary: {bin(a >> 1)})")
print(f"{b} >> 1 = {b >> 1} (Binary: {bin(b >> 1)})")





#wap to extract and display the hundered , tens , and ones's digit of a given three-digit number
num = int(input("enter three digit num\n"))

#digit extract
ones = num % 10
tens = (num // 10) % 10
hundreds = num // 100
print(f"ones :{ones} \n")
print(f"tens :{tens} \n")
print(f"Hundreds :{hundreds} \n")



#wap to find the occurance of a specific color from the list
color_list = ['red' , 'orange' , 'red' , 'white']

color = input("Pick a color").lower()

count = color_list.count(color)
if count > 0:
    print(f"The color '{color}' occurs {count} time(s) in the list.")
else:
    print(f"The color '{color}' is not in the list.")



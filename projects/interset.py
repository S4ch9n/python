from traceback import print_tb

principal = 0
rate = 0
time = 0
while principal <= 0:
    principal = float(input("enter the principal amount : "))
    if principal <= 0:
        print("Principal cant be less than or equal to zero")
while rate <= 0:
    rate = float(input("enter the interest rate  : "))
    if rate <= 0:
        print("rate cant be less than or equal to zero")
while time <= 0:
    time = float(input("enter the time in years : "))
    if time <= 0:
        print("time cant be less than or equal to zero")

total = principal * pow((1 + rate / 100),time)
print(f"Balance after {time} year/s : ${total : .2f}")

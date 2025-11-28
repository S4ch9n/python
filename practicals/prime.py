# Program to check if a number is prime and show its factors

num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print(num, "is NOT a prime number.")
else:
    factors = []
    # Find all factors from 1 to num
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            print("Factors:", factors)

    # Check if number is prime
    if len(factors) == 2:
        print(num, "is a PRIME number.")
    else:
        print(num, "is NOT a prime number.")
        print("Factors:", factors)

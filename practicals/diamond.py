# Solid Diamond Pattern

n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))

# Lower half
for i in range(n-2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2*i + 1))


# Hollow Diamond Pattern

n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2*i - 1) + "*")

# Lower half
for i in range(n-2, -1, -1):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2*i - 1) + "*")





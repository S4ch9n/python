# Program to print Pascal's Triangle

rows = int(input("Enter number of rows: "))

for i in range(rows):
    # Print leading spaces
    print(" " * (rows - i), end="")

    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        # Update value using nCr relation
        num = num * (i - j) // (j + 1)

    print()  # Move to next line

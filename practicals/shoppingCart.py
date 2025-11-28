# ---------------------------------------------------------
# Shopping Cart using Recursion and Lambda Function
# ---------------------------------------------------------

cart = []   # Stores items as (name, price)


# -------------------------------------------
# 1. Recursive Menu
# -------------------------------------------
def menu():
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Items (minimum 2)")
    print("2. View Cart")
    print("3. Calculate Total Bill")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_items()
        menu()   # recursion
    elif choice == 2:
        view_cart()
        menu()   # recursion
    elif choice == 3:
        calculate_total()
        menu()   # recursion
    elif choice == 4:
        print("Thank you for shopping!")
    else:
        print("Invalid choice! Try again.")
        menu()   # recursion


# -------------------------------------------
# 2. Add at least two items
# -------------------------------------------
def add_items():
    print("\nAdd at least 2 items:")
    for i in range(2):  # ensures minimum 2 items
        name = input(f"Enter item {i+1} name: ")
        price = float(input(f"Enter item {i+1} price: "))
        cart.append((name, price))
    print("Items added successfully!")

    # Ask user if they want to add more
    more = input("Add more items? (yes/no): ").lower()
    if more == "yes":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.append((name, price))
        add_items()   # recursion to keep adding


# -------------------------------------------
# 3. View Cart using Recursion
# -------------------------------------------
def view_cart(index=0):
    if len(cart) == 0:
        print("Cart is empty.")
        return

    if index == len(cart):
        return

    print(f"{index+1}. {cart[index][0]} - Rs.{cart[index][1]}")
    view_cart(index + 1)  # recursive call


# -------------------------------------------
# 4. Calculate Total using Lambda + Recursion
# -------------------------------------------
def calculate_total():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    # Lambda to get price from tuple (name, price)
    get_price = lambda item: item[1]

    # Recursive summation
    def recursive_sum(i):
        if i == len(cart):
            return 0
        return get_price(cart[i]) + recursive_sum(i + 1)

    total = recursive_sum(0)
    print("Total Bill = Rs.", total)


# Start program
menu()

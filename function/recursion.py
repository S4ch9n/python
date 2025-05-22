#recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simple and more manageable parts
#function calling itself

#basic example of recursion , factorial number
def fac(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * fac(n-1)  # Recursive call to calculate factorial

result = fac(5)  # Compute the factorial of 5
print(result)  # Print the result

#base case : condition under where the recursion stops , crucial to prevent infinite loops

#recursive case :  the part of the function that include the call itself


#another example of recursion to find fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    #recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))



#type of recursion :
#tail recursion : occur when the recursive call is the last operation executed in function
#non-tail recursion : occurs when there are operation or calculation that follow the recursive call.

# Function to calculate the factorial using tail recursion
def tail_fact(n, acc=1):
    # Base case: When n is 0, return the accumulated result
    if n == 0:
        return acc
    else:
        # Recursive case: Pass the decremented n and the updated accumulator
        return tail_fact(n - 1, acc * n)

# Function to calculate the factorial using non-tail recursion
def non_tail_fact(n):
    # Base case: When n is 1, return 1
    if n == 1:
        return 1
    else:
        # Recursive case: Multiply n with the factorial of (n-1)
        return n * non_tail_fact(n - 1)

# Test the tail-recursive factorial function
print(tail_fact(5))  # Output: 120

# Test the non-tail-recursive factorial function
print(non_tail_fact(5))  # Output: 120




#inner function
#can access variables from the outer function
def fun5(msg): #outer function
    def inner_fun(): #inner function
        print(msg)
    inner_fun()
fun5("hello")


#local variable access
# Define the outer function
def outer_fun():
    # A variable defined in the outer function
    msg = "hello this is outer function"
    # Print the message from the outer function
    print(msg)

    # Define the inner function
    def inner_fun():
        # Print a message from the inner function
        print("inner function")
        # Access and use the variable from the outer function
        print(f"{msg} , inside inner function")

    # Call the inner function from within the outer function
    inner_fun()

# Call the outer function
outer_fun()


#modifying variable using nonlocal
# Define the outer function
def outer_fun2():
    # A local variable 'a' defined in the outer function
    a = 20
    print(f"The value of a inside outer function is: {a}")

    # Define the inner function
    def inner_fun2():
        nonlocal a  # Use the 'nonlocal' keyword to modify 'a' from the outer function scope
        a = 54  # Modify the value of 'a'
        print(f"The value of a inside inner function is: {a}")

    # Call the inner function
    inner_fun2()

    # Print the value of 'a' after it has been modified by the inner function
    print(f"The value of a after modifying in inner function is: {a}")

# Call the outer function
outer_fun2()


#closure in function
# Define the outer function
def closure_fun(a):  # 'a' is a parameter of the outer function
    # Define the inner function
    def closure_fun2():  # Inner function
        # Access and print the variable 'a' from the enclosing scope
        print(a)
    # Return the inner function (not called yet, just the function object)
    return closure_fun2

# Create a closure by calling the outer function with an argument
closure_func = closure_fun('hello , Closure')

# Call the returned inner function
closure_func()







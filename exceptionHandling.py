#Python Exception Handling handles errors that occur during the execution of a program.
# Exception handling allows to respond to the error, instead of crashing the running program.
# It enables you to catch and manage errors, making your code more robust and user-friendly. Let's look at an example:
# exception : An event that interrupts the flow of a program (ZeroDivisionError , TypeError , ValueError)




# Simple Exception Handling Example
try:
    number = int(input('Enter a number: '))
    print(1 / number)
except ZeroDivisionError:  # Handle division by zero
    print("Can't divide by zero")
except ValueError:         # Handle non-integer input
    print("Please enter a valid number")
except Exception: #handle all
    print("something went wrong ! ")
finally: #always executre
    print("Do some cleanup here")

n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError

except ZeroDivisionError:
    print("Can't be divided by zero!")



try:
    n = 10
    res = 100 / n
except ZeroDivisionError:
    print("Not divisible by zero")
else:
    print("Enter valid number")
finally:
    print("Execution complete")




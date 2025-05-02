try:
    # Prompt the user to enter their age and convert the input to an integer.
    age = int(input("Age : "))

    # Set a fixed income value for the calculation.
    income = 20000

    # Calculate the risk by dividing income by age.
    risk = income / age

    # Print the entered age and the calculated risk value.
    print(age)
    print(risk)

# Handle the case where the user enters 0 for age, which would cause a division by zero.
except ZeroDivisionError:
    print('Age cannot be 0')

# Handle the case where the user enters a non-numeric value that cannot be converted to an integer.
except ValueError:
    print('Invalid value')

# Initialize variables
command = ""  # Stores the user input command
started = False  # Keeps track of whether the car is started or stopped

# Start an infinite loop to continuously accept commands
while True:
    # Prompt user for input
    command = input(">  ")

    # Check if the user wants to start the car
    if command == 'start':
        if started:
            # If the car is already started, notify the user
            print("car is already started ")
        else:
            # Start the car and update the state
            started = True
            print("car has started")

    # Check if the user wants to stop the car
    elif command == 'stop':
        if not started:
            # If the car is already stopped, notify the user
            print("car is already stopped")
        else:
            # Stop the car and update the state
            started = False
            print("car has stopped")

    # Provide help information to the user
    elif command == "help":
        print('''
> start : to start the car
> stop : to stop the car 
> quit : to end
        ''')

    # Exit the loop and end the program
    elif command == 'quit':
        break

    # Handle invalid commands
    else:
        print("not catching wht you have entered")  # Notify the user of unrecognized input

# decorator : A function that extends the behavior of another function

# w/o modifying the base function

# pass the base function as an argument to the decorator

# Decorator to add sprinkles
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")          # Step 1: Print sprinkles message
        return func(*args, **kwargs)        # Step 2: Call the next function in the chain, passing all arguments
    return wrapper

# Decorator to add fudge
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")              # Step 1: Print fudge message
        return func(*args, **kwargs)        # Step 2: Call the next function in the chain, passing all arguments
    return wrapper

# Apply decorators: add_sprinkles wraps add_fudge which wraps get_ice_cream
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")  # Final step: Serve the ice cream

# Call the decorated function
get_ice_cream("vanilla")

# A module-packages is a file that contains Python code (functions, classes, or variables)
# that you can include and reuse in your own program.

# You use the 'import' statement to include modules.
# This helps organize large programs into smaller, reusable parts.

# Importing the entire math module-packages
import math  # Imports all functions and constants from the math module-packages.
              # You must use the 'math.' prefix to access them (e.g., math.sqrt(), math.pi).

# Importing the math module-packages with an alias
import math as m  # Gives the math module-packages a shorter name 'm' to make code shorter and clearer.
                  # You can now access math functions/constants using 'm.' (e.g., m.pi, m.sqrt()).

# Importing a specific item (constant) from a module-packages
from math import pi  # Imports only the 'pi' constant directly.
                     # You can now use 'pi' directly without the 'math.' prefix.

# Importing the datetime module-packages
import datetime  # Imports the entire datetime module-packages.
                 # To access the current date/time, you'd need to call datetime.datetime.now().

# Importing a specific class from the datetime module-packages
from datetime import datetime  # Imports the 'datetime' class directly from the datetime module-packages.
                               # Now you can call datetime.now() directly.

# Example: getting the current date and time
# This uses the directly imported datetime class (not the module-packages)
datetime.now()  # Returns the current local date and time.

# Printing the value of pi using different import methods:
print(math.pi)  # Accesses pi using the full 'math.' prefix.
print(m.pi)     # Accesses pi using the alias 'm.' for math.
print(pi)       # Accesses pi directly (no prefix) because we imported it with 'from math import pi'.

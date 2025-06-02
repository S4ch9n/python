# module : a file containing code you want to include in your program
# use 'import' to include a module (built-in on your own)
# useful to break up a large program reusable separates files

import math  # Imports the math module, allowing access to its functions and constants using 'math.' prefix
import math as m  # Imports the math module and assigns it an alias 'm', so you can use 'm.' instead of 'math.'

from math import pi
# Imports only the 'pi' constant directly from the math module, allowing you to use 'pi' without the 'math.' prefix

# Printing the value of pi using different methods:
print(math.pi)  # Accessing pi using the full 'math.' prefix
print(m.pi)     # Accessing pi using the alias 'm.'
print(pi)       # Accessing pi directly, without any prefix (because of the 'from math import pi' statement)

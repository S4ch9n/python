# Importing entire modules from the package
import pyPackage.math_utils as m
import pyPackage.string_utils as s

# Using functions from the imported modules
print(m.add(5, 3))         # Output: 8
print(m.multiply(4, 6))    # Output: 24
print(s.greet("Sachin"))   # Output: Hello, Sachin!
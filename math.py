
# Built-in math Module
# The math module provides advanced mathematical functions:
import math

# Trigonometric functions
math.sin(math.pi / 2)  # Sine
math.cos(0)            # Cosine
math.tan(math.pi / 4)  # Tangent

# Exponents and logarithms
math.exp(1)            # e^x
math.log(10)           # Natural logarithm
math.log10(100)        # Base-10 logarithm

# Constants
math.pi                # π
math.e                 # e

# Rounding and absolute values
math.ceil(4.3)         # Rounds up to 5
math.floor(4.7)        # Rounds down to 4
math.sqrt(16)          # Square root




# numpy for Arrays and Numerical Computations
# numpy is widely used for mathematical operations on arrays and matrices:
import numpy as np

# Arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Operations
c = a + b             # Element-wise addition
d = a * b             # Element-wise multiplication
e = np.dot(a, b)      # Dot product

# Mathematical functions
np.sin(a)             # Apply sine to each element
np.mean(a)            # Mean of elements
np.sum(a)             # Sum of elements

#
# sympy for Symbolic Math
# sympy allows symbolic calculations and solving equations:
from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(x**2 - 4, 0)
solution = solve(equation)  # Solve x^2 - 4 = 0
print(solution)            # [2, -2]

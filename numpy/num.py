import numpy as np   # Import NumPy library

# -----------------------------
# Basic Array Creation
# -----------------------------

num = np.array([1, 2, 3, 4, 5])   # Create a 1D array
print("num:", num)

num2 = np.arange(10)             # Create array from 0 to 9
print("num2:", num2)

print("Dimensions:", num.ndim)   # Number of dimensions
print("Shape:", num.shape)       # Shape of array
print("Length:", len(num))       # Length of array

# -----------------------------
# 1D Array
# -----------------------------

oneD = np.array([1, 2, 3, 4, 5])
print("\noneD:", oneD)
print("oneD ndim:", oneD.ndim)

# -----------------------------
# 2D Array (after reshape)
# -----------------------------

twoD = np.arange(10)
print("\ntwoD before reshape:", twoD)
print("twoD ndim:", twoD.ndim)

twoD_reshaped = twoD.reshape(2, 5)   # Convert 1D to 2D
print("twoD after reshape:\n", twoD_reshaped)
print("Shape:", twoD_reshaped.shape)
print("Size:", twoD_reshaped.size)

# -----------------------------
# Common Arrays
# -----------------------------

cma = np.ones((5, 2))     # Array filled with ones
print("\nOnes array:\n", cma)

dma = np.zeros((5, 5))   # Array filled with zeros
print("\nZeros array:\n", dma)

fma = np.eye(3)          # Identity matrix
print("\nIdentity matrix:\n", fma)

# -----------------------------
# Indexing & Slicing
# -----------------------------

arr = np.array([10, 20, 30, 40, 50])
print("\nIndexing:")
print(arr[0])        # First element
print(arr[-1])       # Last element
print(arr[1:4])      # Slice

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print("\n2D Indexing:")
print(arr2d[0, 1])   # Row 0, Column 1
print(arr2d[:, 1])   # All rows, column 1
print(arr2d[1, :])   # Row 1, all columns

# -----------------------------
# Mathematical Operations
# -----------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nMath Operations:")
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("\nScalar Operations:")
print(a * 2)
print(a + 10)

# -----------------------------
# Useful NumPy Functions
# -----------------------------

stats = np.array([10, 20, 30, 40])
print("\nStatistics:")
print("Sum:", stats.sum())
print("Mean:", stats.mean())
print("Max:", stats.max())
print("Min:", stats.min())

# -----------------------------
# Boolean Indexing
# -----------------------------

bool_arr = np.array([10, 15, 20, 25, 30])
print("\nBoolean Indexing (>20):")
print(bool_arr[bool_arr > 20])

# -----------------------------
# Copy vs View
# -----------------------------

orig = np.array([1, 2, 3])
view_arr = orig.view()   # Shares memory
copy_arr = orig.copy()  # Separate memory

orig[0] = 99

print("\nCopy vs View:")
print("Original:", orig)
print("View:", view_arr)
print("Copy:", copy_arr)

# -----------------------------
# Random Numbers
# -----------------------------

rand_float = np.random.rand(3, 3)   # Random floats
print("\nRandom floats:\n", rand_float)

rand_int = np.random.randint(1, 10, size=(2, 3))  # Random integers
print("\nRandom integers:\n", rand_int)

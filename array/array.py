import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Basic operations
print(arr * 2)           # [ 2  4  6  8 10]
print(np.mean(arr))      # 3.0
print(np.sqrt(arr))      # [1.         1.41421356 1.73205081 2.         2.23606798]



#
arr = np.array([])
product = 1
n = int(input("enter how many elements you want to add in array : "))
for i in range(n):
    elements = int(input("enter elements to add in array : "))
    arr = np.append(arr,elements)
print(arr)
for i in arr:
    product *= i
print("product is : " , product)
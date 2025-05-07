#the reduce function is used to apply a particular function passed in its arguments to all of the list elements mentioned inthe sequence passed along.This function is defined in "functools" modules
# syntax : reduce(fun,iterable[,initial])

# Parameters :
# fun : it is a function to execute on each element of the iterable object
#iter : it is iterable to be reduced
import functools

#define a list of numbers
numbers = [1,2,3,4]

#use reduce to compute the product of list element
product = functools.reduce(lambda x,y : x * y,numbers)
print("Product of list elements : ",product)
# output : Product of list elements :  24


#
numbers2 = [5,6,7,8,9]
product2 = functools.reduce(lambda x , y: x + y ,numbers2)
print("Product of list elements : ",product2)
# output : Product of list elements :  35


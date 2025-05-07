# map() function in python  : the map() function returns a object(which is an iterator) pf the result after applying the given function to each item of a given iterable(list,tuples,etc).
# syntax:map(fun,iter)
# Parameters
# fun : it is a function to which map passes each element of given iterable
# iter : iterable object to be mapped

#function to return double of n
def  double(n):
    return n * 2

#using map to double all numbers
numbers = [1,2,3,4,5]
result = map(double , numbers)
print(list(result))


def double(n):
   return n + 2

numbers2 = [10,20,30,40,50]
result2 = map(double,numbers2)
print(list(result2))

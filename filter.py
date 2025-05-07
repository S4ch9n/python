#the filter() method the given sequence with the help of a function that test each element in the sequence to be true or not
#syntax : filter(function, sequence)
#paramters :
#function : function that test if each element of a sequence is true or not
#sequence : sequence which need to be filtered , it can be sets , lists , tuples or container of any iterator

#define a function to check if number is even
def is_even(n):
    return n % 2 == 0

#defien the list of number
numbers = [1,2,3,4,5,6,7,8,9,10]
#use filter to filter out even numbers
even_numbers = filter(is_even,numbers)
print("Even numbers : ",list(even_numbers))
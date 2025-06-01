# List Comprehension : A concise way to create lists in Python
#  Compact and easier to read than traditional loops
# [expression for value in iterable if condition]
from filter import even_numbers
from practice_question.questions import positive_num

# normal way
doubles = []
for x in range(1,11):
    doubles.append(x)
print(doubles)

# list comprehension
doubles2 = [x for x in range(1,11)]
print(doubles2)



fruits =  ["apple" , "orange" , "banana" , "coconut"]
fruit = [fruit.upper() for fruit in fruits]
print(fruit)


numbers = [11,2,-3,4,-5]
positive_num  = [num for num in numbers if num >= 0]
negative_num =  [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(positive_num)
print(negative_num)
print(even_numbers)
print(odd_numbers)



grades = [85,34,12,90,66,78,89,20]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
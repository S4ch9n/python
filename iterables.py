#Iterables : An object / collection that can return its elements one at a time , allowing it to be iterated over in a loop


numbers = [1,2,3,4,5]
#list is iterable

for number in numbers :
    print(number , end = " ")

#can also reverse
numbers2 = [1,2,3,4,5]
for item in reversed(numbers2):
    print(item)


#tuples
tuples1 = (1,2,3,4,5)
for items in tuples1:
    print(items)

#set
fruits = ['apple' , 'orange' , 'coconut']
for fruit in fruits:
    print(fruit)


#string
name = "Hello world"
for character in name:
    print(character)


#Dictinary
my_dict = {"A" : 1 , "b" : 2 , "C" : 3}
for key, value in my_dict.items():
    print(f"{key} =  {value}")
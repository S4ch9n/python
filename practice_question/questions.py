#maximum and minimun in tuples
tuples = (1,2,3,4,5)
print(max(tuples))
print(min(tuples))

#reverse a string using loop
string = 'Python'
reverseChar = ""
for char in string:
    reverseChar = char + reverseChar
print(reverseChar)


#Python program to interchange first and last elements in a list
list1 = [1,2,3,4,5]
list1[0],list1[4] = list1[4],list1[0]
print(list1)

#sum of tuples elements
#using sum function
tuples = (1,2,3,4,5)
total = sum(tuples)
print(total)

#without using function
tuples2 = (1,2,3,4,5)
total2 = 0
for element in tuples2:
    total2 += element
print(total2)
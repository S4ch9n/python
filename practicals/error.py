#wap to demonstrate multiple exception


list1 = [1,2,3,4,5]
try:
    num = int(input("enter index value : "))
    print(list1[num])
except IndexError:
    print("out of reach")
except ValueError:
    print("enter valid numer")
else:
    print(list1[num])
finally:
    print("done")



#2
dict1 = {
    1 : "abc",
    2 : "cde"
}
try:
    num = int(input("enter the value you want to print : "))
    print(dict1[num])
except KeyError:
    print("value didn't exist")
else:
    print(dict1[num])
finally:
    print("done")


#
try:
    file = open("data.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file didn't exist")
finally:
    print("done")

#
try:
    import pandas
except ImportError:
    print("doesnt have panda installed")
finally:
    print("done")

#
try:
    result = "5" + 5
except TypeError:
    print("character and integer value cant be add")
finally:
    print("done")
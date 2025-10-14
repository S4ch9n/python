from dictionary import output
from practice_question.questions import prime_list


def sum(a , b):
    return a + b
print(sum(2,3))

#
def greet_user():
    print("hi there!")
    print("welcome aboard")

print("start")
greet_user()
print("finish")

#parameter
def greet_user2(name): #argument
    print(f"hii {name} , how are you ?")
greet_user2("John")
greet_user2("Nick")

#multiple parameter
def mult_para(fname,lname): #argument
    print(f"hello my first name is {fname} , and my last name is {lname}")
    print("Nice to meet you !")

mult_para("John" , "doe") #this called positional argument



#keyword argument : don't have to worry about the order of parameter
def greet_user3(fname , lname):
    print(f"hello {fname}  {lname}")

greet_user3(lname = "fury" , fname = "nick")

#Note : if you are using positional arguments and keywords arguments , you should use positional argument first
# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")
# # Keyword argument comes before positional (will raise a SyntaxError)
# greet(message="Good morning", "Alice")  # ❌


#return statement
#a return statement is used to end the execution of the function call and it "returns"the value of the expression following the return keyword to the caller. The statement after the return are not executed
def add(a,b):
    return a + b
def is_true(a):
    return bool(a)

res = add(2,4)
print(res)

res2 = is_true(2<4)
print(res2)

#when the return statement is executed , the function terminates and the specified values is returned to the caller.
#if no value is specified, the function return NONE by default
#reutn statement can not be used outside the function




#another examples
def square(num):
    return num * num

result = square(3)
print(result)




#retunin multiple values
# Define a function `multiple_return` that returns multiple values.
def multiple_return():
    # Assign the string 'sahil' to the variable `name`.
    name = 'sahil'
    # Assign the integer 20 to the variable `age`.
    age = 20
    # Return both `name` and `age` as a tuple.
    return name, age



# Call the `multiple_return` function and unpack its returned tuple into two variables: `name` and `age`.
name, age = multiple_return()

# Print the value of `name` to the console. This will output 'sahil'.
print(name)

# Print the value of `age` to the console. This will output 20.
print(age)





#passing function as an argument
#we can pass a function by simply referencing its name without parentheses .The passed function can then be called inside the function
def fun(func , arg):
    return func(arg)
def square(x):
    return x ** 2
#calling fun and passing square function ass an argument
res =  fun(square ,5)
print(res)




#python def keyword example with *args
#arg is used to pass a variable number of a arguments to a function .The * allow a function to accept any number of positional argument . This is useful when we are not sure how many arguments will be passed to the function
def fun2(*args):
    for arg in args:
        print(arg)
fun2(1, 2, 3, 4, 5)




#python def keyword example with **kwargs
# **kwargs is used to pass a variable number of keyword arguments to a function. The ** syntax collects the keyword arguments into a dictionary , where the keys are the argument name and the value are the corresponding values.This allow the function to accept nay number of named(keyword)arguments
def fun(**kwargs):
    for k ,val in kwargs.items():
        print(f"{k} : {val}")
fun(name = "Alice" , age = 30 , city = "New york")





#def keyword with class
#the def keyword is used to define functions , and it can also be used to define methods inside a class. A method is a function that is associated with an object using the instance of the class

class Person :
    #constructor to initialize the person's name and age
    def __init__(self,name , age):
        self.name = name #set the name attribute
        self.age = age #set the age attribute

        #method to print a greeting message
    def greet(self):
        print(f"Name - {self.name} and Age - {self.age}")

#creating an instance of the Person class
p1 = Person("Alice",30)
#call the greet method to display the greeting message
p1.greet()




#returning List
#we can also return more complex data structure such as list or dictionaries form a function
def return_list(n):
    return [n**2 , n**3]
list_print = return_list(2)
print(list_print)





#function return another function
#in python function are first class citizen , meaning we can return a function from another function
#useful for creating high order function
def return_fun(msg):
    def return_fun2():
        #using the outer function's message
        return f"Message : {msg}"
    return return_fun2()

fun3 = return_fun("hello world")
print(fun3)




def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "☺️",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output.strip()

message = input(">")
print(emoji_converter(message))



#CREATING A FUNCTION FIRST 10 PRIME NUMBERS
def fun(n):
    x = 2
    count = 0
    while count < n :
        for d in range(2 , int(x  ** 0.5) + 1):
            if x % d == 0:
                break
        else:
            print(x)
            count += 1
        x += 1
n = 10
fun(n)


def f():
    s = 'hello guys'  # Local variable
    print(s)

f()
print(s)  # Will throw a NameError because 's' is a local variable of the function 'f' and is not accessible outside of it.





#global variable
def f2():
    print("inside function < " , s)

s = "hey iam outside"
f2()
print("Outside function")


#same variable inside and outside the function
def f3():
    s = "hey iam same , but inside"
    print(s)
s = "hey iam same  , but outside"
f3()
print(s)


#what if we try to change global variable
def f4():
    str += 'world'
    print("hello from inside , ",str)
str = "hello"
f4()
#will throw UnboundLocalError :

#to make the above program work , we need to use the 'global' keyword in python


#The global keyword
#only use to change the global variable inside the function
def global_var():
    global str2
    str2 += "adding"
    print("inside from function ,")
    print(s)
str2 = "it is great"
global_var()
print(str2)


#example 2
#use global because there is no local 'a'
a = 0
def f():
    print("inside f() , a : " ,a)
def g():
    a = 1
    print("inside g() , a : " ,a)
def h():
    global a
    a = 2
    print("inside h() , a : " ,a)
print('global a : ',a)
f()
print('global a : ',a)
g()
print('global a : ',a)
h()
print('global a : ',a)




#inner function
#can access variables from the outer function
def fun5(msg): #outer function
    def inner_fun(): #inner function
        print(msg)
    inner_fun()
fun5("hello")


#local variable access
# Define the outer function
def outer_fun():
    # A variable defined in the outer function
    msg = "hello this is outer function"
    # Print the message from the outer function
    print(msg)

    # Define the inner function
    def inner_fun():
        # Print a message from the inner function
        print("inner function")
        # Access and use the variable from the outer function
        print(f"{msg} , inside inner function")

    # Call the inner function from within the outer function
    inner_fun()

# Call the outer function
outer_fun()


#modifying variable using nonlocal
# Define the outer function
def outer_fun2():
    # A local variable 'a' defined in the outer function
    a = 20
    print(f"The value of a inside outer function is: {a}")

    # Define the inner function
    def inner_fun2():
        nonlocal a  # Use the 'nonlocal' keyword to modify 'a' from the outer function scope
        a = 54  # Modify the value of 'a'
        print(f"The value of a inside inner function is: {a}")

    # Call the inner function
    inner_fun2()

    # Print the value of 'a' after it has been modified by the inner function
    print(f"The value of a after modifying in inner function is: {a}")

# Call the outer function
outer_fun2()


#closure in function
# Define the outer function
def closure_fun(a):  # 'a' is a parameter of the outer function
    # Define the inner function
    def closure_fun2():  # Inner function
        # Access and print the variable 'a' from the enclosing scope
        print(a)
    # Return the inner function (not called yet, just the function object)
    return closure_fun2

# Create a closure by calling the outer function with an argument
closure_func = closure_fun('hello , Closure')

# Call the returned inner function
closure_func()



#high order function : function that take one or more function as arguments , returns a function as a result or do both
# Define a higher-order function
def ho_fun(f, x):
    # Takes a function 'f' and a value 'x' as arguments
    return f(x)  # Applies the function 'f' to 'x' and returns the result

# Define a function to calculate the square of a number
def square(x):
    return x * x  # Return the square of 'x'

# Call the higher-order function with 'square' and the value 5
result = ho_fun(square, 5)

# Print the result
print(result)



#function as a first-class object : in python functon are first class object , meaning they can be treated like other object , such as integer m strings or lists
#assigning function to a variable
# Define a function to generate a greeting message
def greet(n):
    return f"hello {n}!"

# Assign the function 'greet' to another variable 'greet_msg'
greet_msg = greet

# Call the function using the new variable and print the result
print(greet_msg("John"))

#passing function as an argument
def apply(f,v):
    return f(v)
res2 = apply(greet_msg , "nick")
print(res2)

#returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult
dbl = make_mult(2)
print(dbl(5))


#print sum of list using function
def sumList(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum

list1 = [1,2,3,4,5]
print(sumList(list1))




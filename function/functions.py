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

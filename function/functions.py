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
def square(num):
    return num * num

result = square(3)
print(result)
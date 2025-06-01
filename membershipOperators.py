#membership operators : used to test whether a value or variable is found
#in sequence(string , list , set , or dictionary)
# 1 . in
# 2 . not in

word = 'apple'
letter = "p"
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} is not found")



#not in
word2 = 'apple'
letter2 = "q"
if letter in word:
    print(f"{letter} is not found")
else:
    print(f"There is a {letter}")




students = {"Spongebob" , "Patrick" , "John"}
student = "Patrick"
if student in students:
    print("is present")
else:
    print("not present")


grades = {"Sandy" : "A",
          "Nick" : "B",
          "John" : "C"}
student = "Nick"
if student in grades:
    print(grades[student])
else :
    print("student is not found")




email = "abc@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid email")

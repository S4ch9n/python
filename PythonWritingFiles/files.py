# Python writing files(.text, .json,.csv)
import json
import csv



txt_data  = "I like pizza"

file_path = "output.txt"


# w , create file
# with open(file_path , "w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path} was created")


txt_data2 = "I also like burger"

file_path2 = "output2.txt"

with open(file_path2 , 'w') as file:
    file.write(txt_data2)
    print(f"txt file  {file_path2} was created ")



# x : will create new file if didn't exist already
try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path} was created")
except FileExistsError:
    print("That files already exist ! ")


# a : append data
try:
    with open(file_path, "a") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path} was created")
except FileExistsError:
    print("That files already exist ! ")




employees = ["nick", "jerry" , "solana"]

emp_file_path = "employees.txt"

try:
    with open(emp_file_path, "w") as file:
        for employee in employees:
            file.write("\n" + employee)
        print(f"File has been {emp_file_path} created")
except FileExistsError:
    print("That file has aldready existed !")



employees2 = {
    "name" : "John",
    "age" : 30,
    "job" : "cook"
}
emp_file_path2 = "employees.txt2"
try:
    with open(emp_file_path2 , "w") as file:
        json.dump(employees2 , file)
        print(f"json file {emp_file_path2} was created")
except FileExistsError:
    print("already exist")




employees3 = [
    ["name","age","job"],
    ["John" , 30 , "Cook"],
    ['Sandy' , 27 , "Scientist"],
]

file_path3 = "employees3.txt"

try:33
    with open(file_path3 , "w") as file:
        writer = csv.writer(file)
        for row in employees3:
            writer.writerow(row)
        print(f"json file {emp_file_path2} was created")
except FileExistsError:
    print("already exist")
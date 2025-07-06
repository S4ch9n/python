import os

# relative file path
file_path = "stuff/test.txt"

#absolute path
# absolute_path = "C:/Users/HP/Desktop/test.txt" #widnow example

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("that is a file")
    elif os.path.isdir(file_path):
        print("That is directory")
else:
    print("That location doesn't exist")

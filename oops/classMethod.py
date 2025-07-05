#class methods : Allow operation related to the class itself
from membershipOperators import student


# Take (cls) as the first parameter, which represents the class itself.

class Student:

    count = 0

    def __init__(self ,name , gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

      #Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students : {cls.count}"

student1 = Student("John" , 3.2)
student2 = Student("Patrick" , 3.2)
student3 = Student("John" , 4.0)



print(Student.get_count())


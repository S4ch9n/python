# Static methods : A method that belongs to a class rather than any object from that class(instance) usually used for general utility functions

#Instance methods : Best for operation on instances of the class (objects)
#Static methods : Best for utility functions that do not need access to class data

class Employee:
     def __init__(self , name , position):
         self.name = name
         self.position = position

     def get_info(self):
         return f"{self.name} = {self.position}"

     @staticmethod
     def is_valid_position(position):
         valid_position = ["Manager" , "Cashier" , "Cook" , "Boss"]
         return position in valid_position

employee1 = Employee("Eugune" , "Manager")
employee2 = Employee("Nick" , "Cook")
employee3 = Employee("John" , "Boss")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee2.get_info())

# Inheritance is the capability of one class to inherit the methods and properties from another class
# Benefits of inheritance:
    # Code reusability
    # Add features to a class without modifying it
    # It is transitive in nature

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person): # - subclassing
    pass

# An Object of class Student
student = Student("John", "Smith")
print(student.get_full_name()) # John Smith


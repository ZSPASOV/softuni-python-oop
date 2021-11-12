# Create three classes named Person, Employee and Teacher.
# Person with a single public method sleep() that returns: "sleeping..."
# Employee with a single public method get_fired() that returns: "fired..."
# Teacher with a single public method teach() that returns: "teaching..."
# Teacher should inherit from Person and Employee.

class Person:
    def sleep(self):
        return "sleeping..."


class Employee:
    def get_fired(self):
        return "fired..."


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

# Attributes of a class can also be accessed using the following functions
# getattr() - Used to access the attribute of object
# hasattr() - Used to check if an attribute exist or not
# setattr() - Used to set an attribute
# delattr() - Used to delete an attribute (if you are accessing the attribute after deleting it raises error "class has no attribute")

class Employee:
    name = 'Harsh'
    salary = '25000'

    def show(self):
        print(self.name)
        print(self.salary)

employee = Employee()
print(getattr(employee, 'name'))   # Harsh
print(hasattr(employee, 'name'))   # True
setattr(employee, 'height', 152)
print(getattr(employee, 'height')) # 152
delattr(Employee, 'salary')
print(getattr(Employee, 'salary', None)) # None - taka kato polzvame None kato 3ti argument vrushta None, inache dolu vrushta greshka
#print(getattr(Employee, 'salary')) # # AttributeError: type object 'Employee' has no attribute 'salary'



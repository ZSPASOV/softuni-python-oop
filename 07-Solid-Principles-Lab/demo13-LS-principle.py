class Person:
    def say_hi(self):
        return 'Hi'


class Student(Person):
    pass



def greeter(person: Person):
    return person.say_hi()


# ideqta s LSP e funkciqta greeter spokoino da moje da priema Student vmesto Person
# i da prodalji da raboti po sushtiq na4in

def greeter(student: Student):
    return student.say_hi()


student = Student()

print(greeter(student)) # Hi

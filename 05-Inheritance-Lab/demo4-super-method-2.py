class Human:
    def __init__(self, name, birth_year, gender, eye_color):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.eye_color = eye_color

    def say_my_name(self):
        return self.name


class Student(Human):
    def __init__(self, *args, **kwargs):
        faculty_number = kwargs.pop('faculty_number')
        super().__init__(*args, **kwargs)
        self.faculty_number = faculty_number


student = Student('Ivan Ivanov', 1997, 'M', 'Brown', faculty_number='F123456')
print(student.say_my_name()) # Ivan Ivanov
print(student.eye_color) # Brown

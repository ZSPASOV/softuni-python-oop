class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Parent):
    def __init__(self, name, age, gender):
        self.gender = gender
        super().__init__(name, age)


# v2

class Parent:
    def __init__(self, name, age, eye_color='green'):
        self.name = name
        self.age = age
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, name, age, gender, eye_color='blue'):
        self.gender = gender
        super().__init__(
            eye_color=eye_color,
            name=name,
            age=age)


child = Child('test', 22, 'M')
print(child.eye_color) # blue
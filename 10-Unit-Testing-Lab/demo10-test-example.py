# If we have a class Person with methods get_full_name() and get_info():
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'

# We can test both methods using the code below:

import unittest

class PersonTests(unittest.TestCase):
    def setUp(self): # narushava PEP8 convention no taka e prieto. setUp method-a vinagi restartira instance predi sledvasht test
        self.person = Person("Luc", "Peterson", 25) # 3 A, 1. Arange

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected_result = "Luc Peterson"
        self.assertEqual(result, expected_result)

    def test_get_info(self):
        result = self.person.get_info()
        expected_result = "Luc Peterson is 25 years old"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

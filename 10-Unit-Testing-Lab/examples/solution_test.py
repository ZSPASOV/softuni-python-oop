import unittest
from solution import Person


class PersonTests(unittest.TestCase):
    def test_person_is_properly_initiated(self):
        person = Person('Jordan')
        self.assertEqual(person.name, 'Jordan')


if __name__ == '__main__':
    unittest.main()

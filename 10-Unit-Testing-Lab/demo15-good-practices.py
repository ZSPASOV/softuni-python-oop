# Assertion Messages
# Assertions can show messages
    # Helps with diagnostics

def test_get_info(self):
    result = self.person.get_info()
    expected_result = "Luc Peterson is 25 years old" # assertion message
    self.assertEqual(result, expected_result)


# DRY: Don't Repeat Yourself

class DogTests(unittest.TestCase):
    def setUp(self):
        self.dog = Dog("Pug", 4) # executes before each test

    def test_init(self):
        self.assertEqual(self.dog.species, "Pug")
        self.assertEqual(self.dog.age, 4)

    def test_get_full_info(self):
        result = self.dog.get_full_info()
        expected_result = "Dog: Pug, 4 years old"
        self.assertEqual(result, expected_result)


# Naming Tests
# Test names
    # Should use business domain terminology
    # Should be descriptive and readable

# not okay:
# test_increment_Number(self): …
# test_Test1(self): …
# testTransfer(self): …


# okay:

# test_deposit_Xleva_should_increase_balance_with_Xleva(self): …
# test_deposit_negativeLeva__should_not_increase_balance(self): …

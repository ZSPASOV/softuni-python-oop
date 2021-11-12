# Test fixture
    # A baseline for running tests to ensure there is a fixed environment
    # in which tests are run so that results are repeatable
# Test case
    # A set of conditions used to determine if a system works correctly
# Test suite
    # A collection of testcases used to test a software if it has some specified set of behaviors
# Test runner
    # A component which sets up the execution of tests and provides the outcome to the user

import unittest
class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

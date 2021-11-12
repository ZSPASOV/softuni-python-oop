# da vidq za context manager
# Since Python 2.7 you can use context manager to get ahold of the actual Exception object thrown:
import unittest

def broken_function():
    raise Exception('This is broken')

class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            broken_function()

        self.assertTrue('This is broken' in context.exception)

if __name__ == '__main__':
    unittest.main()
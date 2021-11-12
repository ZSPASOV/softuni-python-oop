import mock_example
import unittest
from unittest import mock


class MockExampleTests(unittest.TestCase):
    def test_get_my_daily_tasks(self):
        mock_value = {'completed': False, 'id': 1, 'title': 'delectus aut autem', 'userId': 1}
        with unittest.mock.patch('mock_example.get_task', return_value=mock_value):
            daily_tasks = mock_example.my_daily_todo()
        self.assertEqual(daily_tasks, [{
            'userId': 1,
            'id': 1,
            'title': 'delectus aut autem',
            'completed': False
        }])


if __name__ == '__main__':
    unittest.main()
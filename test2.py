import unittest
from test.view import test_view


class TestMethods(unittest.TestCase):
    def test_add(self):
        results = test_view(1, 2)
        self.assertEqual(results, -1)


if __name__ == '__main__':
    unittest.main()

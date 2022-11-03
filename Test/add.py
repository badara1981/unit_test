import unittest

from math_operation import add


class TestAddition(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(20, 20), 40)

if __name__ == '__main__':
    unittest.main()


